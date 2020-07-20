import glob
import argparse
import os
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split

object_enum = {'blade':0, 'nose':1, 'pole':2}

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_dirs", nargs="+", help="xml directory")
parser.add_argument("-o", "--output_dir", default="./data", help="directory for train.txt, test.txt")
parser.add_argument("-r", "--ratio", default=0.2, type=float, help="test set ratio")

args = parser.parse_args()

input_dirs = args.input_dirs
output_dir = args.output_dir
ratio = args.ratio

filenames = []

for i in input_dirs:
    if not os.path.isdir(i):
        print(f"input dir not exists: '{i}'")
        exit(0)
    filenames += list(map(lambda x: x.replace("txt", "jpg").replace("labels", "JPEGImages"), glob.glob(os.path.join(i, "*.txt"))))

train_list, validation_list = train_test_split(filenames, test_size=ratio, random_state=11)


train_txt = os.path.join(output_dir, "train.txt")
validation_txt = os.path.join(output_dir, "test.txt")

with open(train_txt, "w") as f:
    f.writelines("\n".join(train_list))

with open(validation_txt, "w") as f:
    f.writelines("\n".join(validation_list))

print("Train & Test set saved at %s." % "./data")
