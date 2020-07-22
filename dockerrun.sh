sudo nvidia-docker run -itd \
    -v /media/volume3/darknet_datasets:/media/volume3/darknet_datasets \
    -v /home/sangmin/darknet:/app \
    --net="host" \
    --name darknet-train \
    sanggggg/darknet-opencv:0.1
