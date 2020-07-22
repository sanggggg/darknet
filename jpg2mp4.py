import cv2
import argparse
import os
import re
import json
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_dir", help="target directory, which contains 'JPEGImages'")
parser.add_argument("-b", "--bbox_file_json", default="./result.json", help="json bbox file")
parser.add_argument("-o", "--output_file_mp4", default="./result.mp4", help="output file")

args = parser.parse_args()

path_jpgs = os.path.join(args.input_dir, "JPEGImages")
path_json = args.bbox_file_json
path_mp4 = args.output_file_mp4

if not os.path.isdir(path_jpgs):
    print("%s is not directory" % path_jps)
    print("converting canceled")
    exit(0)

if os.path.isfile(path_mp4):
    print("output file '%s' already exists" % path_mp4)
    ans = input("want to overwrite? : ").lower()
    if not ans in ["y", "yes"]:
        print("converting canceled")
        exit(0)
    else:
        os.remove(path_mp4)

path_jpgs = [os.path.join(path_jpgs, i) for i in os.listdir(path_jpgs) if re.search(".jpg$", i)]
path_jpgs.sort()



def xywh2points(coord, width, height):
    rx, ry, rw, rh = coord['center_x'], coord['center_y'], coord['width'], coord['height']
    p1 = int(width * rx - (width * rw) / 2), int(height * ry - (height * rh) / 2)
    p2 = int(width * rx + (width * rw) / 2), int(height * ry + (height * rh) / 2)
    return p1, p2

fps = 30
class2color = {0:(255,0,0), 1:(0,255,0)}
dict_bbox = {}
frames = []


with open(path_json) as json_file:
    json_data = json.load(json_file)
    for frame_item in json_data:
        dict_bbox[frame_item["filename"]] = frame_item["objects"]

for idx, path in enumerate(path_jpgs):
    _img = cv2.imread(path)
    img = np.copy(_img)

    height, width, layers = img.shape
    size = (width, height)
    
    if path in dict_bbox:
        bboxs = dict_bbox[path]
        for bbox in bboxs:
            coord = bbox['relative_coordinates']
            class_id = bbox['class_id']
            label = bbox['name'] + "-" + str(bbox['confidence'])
            p1, p2 = xywh2points(coord, width, height)
            
            cv2.rectangle(img, p1, p2, class2color[class_id], 1)
            cv2.putText(img, label, (p1[0] + 5, p1[1] + 5), cv2.FONT_HERSHEY_PLAIN, 0.6, class2color[class_id], 2, bottomLeftOrigin=True)
    
    frames.append(img)

out = cv2.VideoWriter(path_mp4, cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
for frame in frames:
    out.write(frame)
out.release()
