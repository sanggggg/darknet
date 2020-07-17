sudo nvidia-docker run -itd \
    -v /home/sanggggg/dataset/blade_detection/darknet/20191107_siwha/191107_133745_8633:/dataset \
    -v /home/sanggggg/repos/darknet:/app \
    -p 8080:80 \
    --name darknet-train \
    darknet-opencv:0.0