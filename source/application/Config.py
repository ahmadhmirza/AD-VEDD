import os
#Get the path to the current script:
#This will facilitate in geting the rest of the path programatically.
SCRIPT_PATH = os.path.dirname(__file__)

MAIN_WINDOW_TITLE = "VEd²" # Visual Evaluation of Drone Data - VEDD

#Initial UI Size
LEFT    =   500
TOP     =   500
WIDTH   =   500
HEIGHT  =   500

#Push Button Strings
LOAD_DATA = "Select File"


#ASSETS
ASSETS_DIR_NAME         = "assets"
TF_MODELS_DIR_NAME      = "tf_model"
TENSOR_FLOW_MODEL_NAME  = "frozen_inference_graph.pb"
LABEL_MAP_NAME          = "label_map.pbtxt"

#Path to assets directory
ASSETS_DIR          = os.path.join(SCRIPT_PATH,ASSETS_DIR_NAME)
#Path to trained_inference_graph
TF_MODELS_DIR       = os.path.join(ASSETS_DIR,TF_MODELS_DIR_NAME)
TENSOR_FLOW_MODEL   = os.path.join(TF_MODELS_DIR,TENSOR_FLOW_MODEL_NAME)
#Path to label_map.pbtxt file
LABEL_MAP           = os.path.join(ASSETS_DIR,LABEL_MAP_NAME)