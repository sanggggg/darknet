
./darknet detector test ./data/blade-detection.data ./cfg/yolov4-blade-detection-multi-gpu.cfg ./backup/yolov4-blade-detection-multi-gpu_best.weights -dont_show -out result_$1.json < ./data/inference.txt
