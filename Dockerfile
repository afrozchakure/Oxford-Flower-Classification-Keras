# refernce: https://hub.docker.com/_/ubuntu
FROM ubuntu:16.04

MAINTAINER Afroz Chakure <aaaanchakure@gmail.com>

# Copy all the files
COPY inference.py /
COPY classifier_4373per.h5 /
COPY imagelabels.mat /
COPY setid.mat /
COPY jpg_valid jpg_valid/

# install build utilities
RUN apt-get update
RUN apt-get install -y python3-pip python3-dev 
RUN apt-get install -y build-essential cmake git unzip pkg-config libopenblas-dev liblapack-dev 
# RUN update-alternatives --config python
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5.2
RUN alias python="python3.5.2"
RUN pip3 install tensorflow==1.14.0
RUN pip3 install keras
RUN apt-get install -y python-opencv 

# Installing python dependencies
COPY requirements.txt /
RUN pip3 install -r requirements.txt

RUN python --version
# Running Python Application
CMD ["python3", "./inference.py"]
