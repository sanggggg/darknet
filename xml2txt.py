import glob
import argparse
import os
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_dir", help="xml directory")
parser.add_argument("-o", "--output_dir", help="labels directory")

args = parser.parse_args()

input_dir, output_dir = args.input_dir, args.output_dir

if not os.path.isdir(input_dir):
    print(f"input dir not exists: '{input_dir}'")
    exit(0)

if not os.path.isdir(output_dir):
    print(f"output dir not exists: '{output_dir}'")
    exit(0)


filenames = glob.glob(os.path.join(input_dir, "*.xml"))

object_enum = {'blade':0, 'nose':1, 'pole':2}

process_count = 0

for filename in filenames:
    
    tree = ET.parse(filename)
    root = tree.getroot()
    
    jpgname = tree.find('filename').text
    txtname = tree.find('filename').text.split(".")[0] + ".txt"

    img_width = float(tree.find('.//width').text)
    img_height = float(tree.find('.//height').text)

    
    with open(os.path.join(output_dir, txtname), "w") as f:
        process_count += 1
        f.truncate(0)

        print(f"processing {process_count}/{len(filenames)} : {txtname}")
        for bbox in root.findall('object'):
            cid = object_enum[bbox.findtext('name')]
            xmin = float(bbox.findtext('.//xmin'))
            ymin = float(bbox.findtext('.//ymin'))
            xmax = float(bbox.findtext('.//xmax'))
            ymax = float(bbox.findtext('.//ymax'))

            bbox_width_ratio = (xmax - xmin) / img_width
            bbox_height_ratio = (ymax - ymin) / img_height

            bbox_x_center_ratio = (xmax + xmin) / 2 / img_width
            bbox_y_center_ratio = (ymax + ymin) / 2 / img_height

            f.write("%d %f %f %f %f" % (cid, bbox_x_center_ratio, bbox_y_center_ratio, bbox_width_ratio, bbox_height_ratio))
