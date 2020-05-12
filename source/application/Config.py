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
TENSOR_FLOW_MODEL_NAME  = "frozen_inference_graph.pb"

#Path to assets directory
ASSETS_DIR          = os.path.join(SCRIPT_PATH,ASSETS_DIR_NAME)
#Path to trained_inference_graph
TENSOR_FLOW_MODEL   = os.path.join(ASSETS_DIR,TENSOR_FLOW_MODEL_NAME)
