import os
#Get the path to the current script:
#This will facilitate in geting the rest of the path programatically.
SCRIPT_PATH = os.path.dirname(__file__)

MAIN_WINDOW_TITLE = "VEd²" # Visual Evaluation of Drone Data - VEDD

#Initial UI Size
LEFT    =   400
TOP     =   400
WIDTH   =   630
HEIGHT  =   530

#ImageHolder size
IMG_X       =   10
IMG_Y       =   10
IMG_WIDTH   =   500
IMG_HEIGHT  =   500

#Push Button Size
BTN_WIDTH  = 100
BTN_HEIGHT = 100
#Push Button Strings
LOAD_DATA       = "Select File"
PROCESS_IMAGE    = "Analyse Image"


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