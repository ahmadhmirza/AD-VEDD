import cv2 
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import os
import sys
import tarfile
import zipfile
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

import Config as APP_CONFIG

# TensorFlow Object_Detection imports
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util



def load_DetGraph_and_Map(PATH_TO_FROZEN_GRAPH,PATH_TO_LABELS):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        try:
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        except Exception as e:
            print(str(e))
    ### LOAD THE LABEL MAP
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
    return detection_graph, category_index
"""
Function to load image file into a numpy array for further processing
@param  : image
@return : numpy array
"""
def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

"""
Perform detection on a image/frame,
@param: image(numpy array), frozen inference graph
@return: dict with detections.
"""
def run_inference_for_single_image(image, graph):
  with graph.as_default():
    with tf.Session() as sess:
      # Get handles to input and output tensors
      ops = tf.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
      ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
              tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[0], image.shape[1])
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

      # Run inference
      output_dict = sess.run(tensor_dict,
                             feed_dict={image_tensor: np.expand_dims(image, 0)})

      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.uint8)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
  return output_dict

def analyseImage(image,detection_graph,category_index):
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    #image_np = load_image_into_numpy_array(image)
    image_np = image
    height, width, channels = image_np.shape
    if height <=500 and widht <=500:
        print("Resolution: " + str(height)+", " + str(width))
        BOUNDING_BOX_LINE_THICKNESS = 2
    else:
        print("Resolution: " + str(height)+", " + str(width))
        BOUNDING_BOX_LINE_THICKNESS = 8
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    #image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
    image_np,
    output_dict['detection_boxes'],
    output_dict['detection_classes'],
    output_dict['detection_scores'],
    category_index,
    instance_masks=output_dict.get('detection_masks'),
    use_normalized_coordinates=True,
    line_thickness=BOUNDING_BOX_LINE_THICKNESS,
    min_score_thresh=0.9)

    #co-ordinates of all detection boxes
    boxes = output_dict['detection_boxes']
    # get all boxes from an array
    max_boxes_to_draw = boxes.shape[0]
    # get scores to get a threshold
    scores = output_dict['detection_scores']
    # this is set as a default but feel free to adjust it to your needs
    min_score_thresh=.9
    # iterate over all objects found
    outBoundingBox = []
    boundingBoxData = {
        "Box" : None,
        "Class": None,
        "Score": None
    }

    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores is None or scores[i] > min_score_thresh:
            # boxes[i] is the box which will be drawn
            class_name = category_index[output_dict['detection_classes'][i]]['name']
            #print ("This box is gonna get used", boxes[i], output_dict['detection_classes'][i])
            #outBoundingBox.append(boxes[i])
            boundingBoxData["Box"] = [boxes[i][0],boxes[i][1],boxes[i][2],boxes[i][3]]
            boundingBoxData["Class"] = class_name
            boundingBoxData["Score"] = scores[i]
            outBoundingBox.append(boundingBoxData)

    return image_np,outBoundingBox

def detectVehicles(inputImage):
    print("VehicleDetector: Starting analysis...")
    PATH_TO_FROZEN_GRAPH    = APP_CONFIG.TENSOR_FLOW_MODEL
    PATH_TO_LABELS          = APP_CONFIG.LABEL_MAP
    #detection_graph, category_index= load_DetGraph_and_Map(PATH_TO_FROZEN_GRAPH,PATH_TO_LABELS)
    outputImage,detectionBoxes = analyseImage(inputImage,detection_graph,category_index)
    print("VehicleDetector: Analysis complete.")
    print("[ymin, xmin, ymax, xmax]")
    print(detectionBoxes)
    return outputImage

PATH_TO_FROZEN_GRAPH    = APP_CONFIG.TENSOR_FLOW_MODEL
PATH_TO_LABELS          = APP_CONFIG.LABEL_MAP

detection_graph, category_index= load_DetGraph_and_Map(PATH_TO_FROZEN_GRAPH,PATH_TO_LABELS)