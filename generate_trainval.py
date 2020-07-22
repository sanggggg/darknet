import glob
import argparse
import os
import xml.etree.ElementTree as ET
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_dirs", nargs="+", help="txt file directory")
parser.add_argument("-o", "--output_dir", default="./data", help="directory for train.txt, test.txt")
parser.add_argument("-r", "--ratio", default=0.2, type=float, help="test set ratio")
parser.add_argument("-x", "--inference", default=False, type=bool, help="want to data for inference")

args = parser.parse_args()

input_dirs = args.input_dirs
output_dir = args.output_dir
ratio = args.ratio
isinference = args.inference


img_dirs = list(map(lambda path: os.path.join(path, "labels"), input_dirs))
train_txt = os.path.join(output_dir, "train.txt")
validation_txt = os.path.join(output_dir, "test.txt")
inference_txt = os.path.join(output_dir, "inference.txt")

if not isinference and os.path.isfile(train_txt):
    print("output file '%s' already exists" % train_txt)
    ans1 = input("want to overwrite? : ") in ["y", "Y", "yes"]
    if not ans1:
        print("converting canceled")
        exit(0)

if not isinference and os.path.isfile(validation_txt):
    print("output file '%s' already exists" % validation_txt)
    ans = input("want to overwrite? : ").lower()
    if not ans1 in ["y", "yes"]:
        print("converting canceled")
        exit(0)

if isinference and os.path.isfile(inference_txt):
    print("output file '%s' already exists" % inference_txt)
    ans = input("want to overwrite? : ").lower()
    if not ans1 in ["y", "yes"]:
        print("converting canceled")
        exit(0)

filenames = []

for i in img_dirs:
    if not os.path.isdir(i):
        print("input dir not exists: '%d'" % i)
        exit(0)
    filenames += list(map(lambda x: x.replace("txt", "jpg").replace("labels", "JPEGImages"), glob.glob(os.path.join(i, "*.txt"))))


print("Get %d dirs" % len(input_dirs))


if isinference:
    inference_list = filenames

    print("Total file number %d" % len(filenames))
    print("Inference set size <%d>" % len(inference_list))

    with open(inference_txt, "w") as f:
        f.truncate(0)
        f.writelines("\n".join(inference_list))

    print("Inference set saved at %s." % output_dir)

else:
    train_list, validation_list = train_test_split(filenames, test_size=ratio, random_state=11)

    print("Total file number %d" % len(filenames))
    print("Train set size <%d>" % len(train_list))
    print("Test set size <%d>" % len(validation_list))

    with open(train_txt, "w") as f:
        f.truncate(0)
        f.writelines("\n".join(train_list))

    with open(validation_txt, "w") as f:
        f.truncate(0)
        f.writelines("\n".join(validation_list))

    print("Train & Test set saved at %s." % output_dir)
