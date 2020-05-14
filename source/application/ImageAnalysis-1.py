import tensorflow as tf
import tensornets as nets
import cv2
import numpy as np
import time


inputs = tf.placeholder(tf.float32, [None, 416, 416, 3]) 
model = nets.YOLOv3COCO(inputs, nets.Darknet19)
img_path = "/home/ahmad/Desktop/test_2.jpg"
outimg_path = "/home/ahmad/Desktop/Situation_1_fern_out.JPG"

classes={'2':'car','3':'bike','5':'bus','7':'truck'}
list_of_classes=[2,3,5,7]#to display other detected #objects,change the classes and list of classes to their respective #COCO indices available in their website. Here 0th index is for #people and 1 for bicycle and so on. If you want to detect all the #classes, add the indices to this list
with tf.Session() as sess:
    sess.run(model.pretrained())
    
    
    img = cv2.imread(img_path)
    img=cv2.resize(img,(416,416))
    imge=np.array(img).reshape(-1,416,416,3)
    start_time=time.time()
    preds = sess.run(model.preds, {inputs: model.preprocess(imge)})
        
    boxes = model.get_boxes(preds, imge.shape[1:3])
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 700,700)
            
    boxes1=np.array(boxes)
    for j in list_of_classes: #iterate over classes
        count =0
        if str(j) in classes:
            lab=classes[str(j)]
        if len(boxes1) !=0:
#iterate over detected vehicles
            for i in range(len(boxes1[j])): 
                box=boxes1[j][i] 
                #setting confidence threshold as 40%
                if boxes1[j][i][4]>=.40: 
                    count += 1    
 
                    cv2.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,255,0),3)
                    cv2.putText(img, lab, (box[0],box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), lineType=cv2.LINE_AA)
        print(lab,": ",count)
    
        #Display the output
        cv2.imwrite(outimg_path, img)     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break