FROM nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
    vim \
    build-essential \
    cmake \
    git \
    wget \
    unzip

RUN apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev \
    && apt-get install -y libqt4-dev \
    && apt-get install -y libatlas-base-dev gfortran libeigen3-dev \
    && apt-get install -y python2.7-dev python3-dev python-numpy python3-numpy \
    && wget -O opencv.zip https://github.com/opencv/opencv/archive/3.2.0.zip \
    && unzip opencv.zip \
    && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.2.0.zip \
    && unzip opencv_contrib.zip \
    && cd opencv-3.2.0 \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=Release -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_QT=ON -D WITH_PTHREADS_PF=ON -D WITH_OPENNI2=OFF -D WITH_OPENNI=OFF -D WITH_OPENGL=ON -D WITH_IPP=ON -D WITH_CSTRIPES=ON -D WITH_CUBLAS=ON -D WITH_V4L=ON -D WITH_CUDA=ON -D WITH_GDAL=ON -D WITH_XINE=ON -D WITH_NVCUVID=OFF -D WITH_CUFFT=ON -D WITH_EIGEN=ON -D WITH_LAPACK=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D BUILD_EXAMPLES=ON -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_opencv_legacy=ON -D BUILD_TIFF=ON -D BUILD_opencv_java=ON -D USE_GStreamer=ON -D FORCE_VTK=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D ENABLE_FAST_MATH=1 -D CUDA_FAST_MATH=1 -D CUDA_GENERATION=Auto -D CUDA_ARCH_BIN=6.1 -D CUDA_NVCC_FLAGS="-D_FORCE_INLINES" -D CMAKE_C_COMPILER=$(which gcc) -D CMAKE_CXX_COMPILER=$(which g++) -D PYTHON_INCLUDE_DIR=/usr/include/python2.7 -D PYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python2.7 -D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so -D BUILD_opencv_freetype=OFF .. \
    && make -j9 \
    && make install -j9 \
    && cd ../../

# RUN git clone https://github.com/sanggggg/darknet.git

