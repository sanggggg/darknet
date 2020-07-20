sudo nvidia-docker run -itd \
    -v /home/sanggggg/dataset/blade_detection/darknet/:/home/sanggggg/dataset/blade_detection/darknet \
    -v /home/sanggggg/repos/darknet:/app \
    -p 8080:80 \
    --name darknet-train \
    darknet-opencv:0.0
