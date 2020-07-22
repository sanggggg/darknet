sudo mkdir /media/volume3/darknet_results/$1

sudo cp ./backup/yolov4-blade-detection-multi-gpu_best.weights /media/volume3/darknet_results/$1/
sudo cp ./cfg/yolov4-blade-detection-multi-gpu.cfg /media/volume3/darknet_results/$1/
sudo cp ./data/train.txt /media/volume3/darknet_results/$1/
sudo cp ./data/test.txt /media/volume3/darknet_results/$1/
