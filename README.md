# AD-VEDD
Automated Driving - Visual Evaluation of Drone Data

This repo holds the software designed and built for the code competition [Automatisiertes Fahren – GUI zur visuellen Auswertung von Drohnendaten](https://www.it-talents.de/foerderung/code-competition/code-competition-05-2020).

The objective of the software is to provide a GUI for analysis of images recorded from a drone footage for vehicles in a parking-lot. For the first phase, images are read into the GUI and analysis is performed using a combination of OpenCV and Tensorflow to detect vehicles and lane markings in the image. 

For the second part further analysis is to be done to extract useful information from the image e.g. distance and orientation of the vehicles with respect to the lane markings etc.

The figure below shows the current UI of the application.

![Image Analysis Output](https://github.com/ahmadhmirza/AD-VEDD/raw/master/_doc/screenshots/Screenshot%20from%202020-05-27%2011-05-10.png)


## Installation Instructions:
### Prerequisites
    * Python 3+ (3.7 recommended)
    * virtualenv Package (pip install virtualenv)
### Steps:
    * Clone the repository  
        * git clone https://github.com/ahmadhmirza/AD-VEDD.git
    * Navigate to directory : _AD-VEDD/src/application/assets/_
        * Extract tf_model.zip to the same directory
        * After this step following file should be available in your local directory:
            * AD-VEDD/src/application/assets/tf_model/frozen_inference_graph.pb
    * Create a virtual environment 
        * virtualenv venv
    * Install library dependencies 
        * pip install -r requirements.txt
### Starting the application
    * Navigate to the directory: _AD-VEDD/src/application/_
    * Run the command `python Main.py` in the terminal 
    * The main window of AD-VEDD should show up.

## UI-Documentation
### Tabs:
* **Image Analysis Tab** : Tab for processing image inputs
* **Video Analysis Tab** : Tab for processing video inputs. Functionality not available in ver 1.0
### Functionality Buttons:
* **Load Image** : Button to read in the image for further processing
* **Start Analysis**: Begins the analysis process (lane detection & vehicle detection)
* **Generate Report**: Saves the report shown in the Analysis Summary section as .csv file.

*----------*----------*
