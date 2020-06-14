FROM python:3.7

# install build utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get -y upgrade

#Create a datavolume as external interface
VOLUME /datavol

#Copy contents of the current directory into the image
ADD . /WorkingDir

# install pip
RUN apt-get update
RUN apt-get install -y git 
#RUN apt-get install -y python-pip
RUN pip install --upgrade pip

#Install tensor-flow and dependencies
RUN pip install tensorflow==1.15

RUN apt-get install -y protobuf-compiler python-pil python-lxml
RUN pip install PyQt5==5.9.2
RUN pip install numpy==1.16
RUN pip install OpenCV-Python
RUN pip install lxml
RUN pip install matplotlib
RUN pip install pathlib
RUN pip install pillow
RUN pip install Cython
RUN pip install contextlib2
RUN pip install pandas
RUN pip install tensorflow-object-detection-api
RUN pip install pyexiv2

#Change working directory to workspace
WORKDIR /WorkingDir/application/

#Define entry point to be the model training script
ENTRYPOINT ["python", "Main.py"]
