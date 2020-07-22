import glob
import argparse
import os
import xml.etree.ElementTree as ET
import shutil

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_dir", nargs="+", help="directory which contains JPEGImages & Annotations")

args = parser.parse_args()

target_dirs = args.input_dir

def annotate_directory(target):
    input_dir = os.path.join(target, "Annotations")
    image_dir = os.path.join(target, "JPEGImages")
    output_dir = os.path.join(target, "labels")

    if not os.path.isdir(input_dir):
        print("input dir not exists: %s" % input_dir)
        exit(0)

    if os.path.isdir(output_dir):
        print("output dir '%s' already exists" % output_dir)
        ans = input("want to overwrite? : ").lower()
        if ans in ["y", "yes"]:
            shutil.rmtree(output_dir, ignore_errors=True)
        else:
            print("converting canceled")
            return
    
    os.mkdir(output_dir)


    filenames = glob.glob(os.path.join(input_dir, "*.xml"))

    # pole is not used yet
    # object_enum = {'blade':0, 'nose':1, 'pole':2}
    object_enum = {'blade':0, 'nose':1}

    process_count = 0

    for filename in filenames:
    
        tree = ET.parse(filename)
        root = tree.getroot()
    
        jpgname = tree.find('filename').text
        txtname = tree.find('filename').text.split(".")[0] + ".txt"

        if not os.path.exists(os.path.join(image_dir, jpgname)):
            continue

        img_width = float(tree.find('.//width').text)
        img_height = float(tree.find('.//height').text)

    
        with open(os.path.join(output_dir, txtname), "w") as f:
            process_count += 1
            f.truncate(0)

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
    
    print("converting complete")

for target in target_dirs:
    print("Processing %s..." % target)	
    annotate_directory(target)

