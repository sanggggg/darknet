FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04
COPY . /app


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    vim \
    build-essential \
    cmake \
    git


RUN git clone https://github.com/sanggggg/darknet.git

