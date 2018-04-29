#!/usr/bin/python3

import cv2
import glob
import os
import sys
import piexif
import json
import datetime


def get_exif_meta_data(file_name):
    exif_data = {}
    exif_dict = piexif.load(file_name)
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            key = piexif.TAGS[ifd][tag]["name"]
            exif_data[key] = str(exif_dict[ifd][tag])
    return exif_data


def write_image_meta_data(file_name, img_meta_data):
    with open(file_name + ".json", 'w') as outfile:
        json.dump(img_meta_data, outfile)


def create_thumbnail(file_name):
    image = cv2.imread(file_name)
    thumbnail = cv2.resize(image, (120, 120))
    cv2.imwrite(image_dir + "/thumbs/thumb_%s" % basename, thumbnail)


def get_creation_timestamp(exif_data):
    date_created = exif_data['DateTime']
    cleaned_creation_date = date_created.replace("b", '').replace("'", '')
    as_date = datetime.datetime.strptime(cleaned_creation_date, "%Y:%m:%d %H:%M:%S")
    return as_date


image_dir = sys.argv[1]
print("Scanning directory " + image_dir)
path = image_dir + '/*.jpg'
files = glob.glob(path)
images = []
for file in files:
    if not os.path.exists(image_dir + '/thumbs'):
        os.makedirs(image_dir + '/thumbs')

    basename = os.path.basename(file)
    print("Found image: " + basename)

    img_exif_data = get_exif_meta_data(file)
    write_image_meta_data(file, img_exif_data)
    create_thumbnail(file)
    images.append((file, img_exif_data))


images.sort(key=lambda img_tpl: get_creation_timestamp(img_tpl[1]).timestamp())
sorted_file_names = []
for img in images:
    sorted_file_names.append(os.path.basename(img[0]))

with open(image_dir + "/sort-order.json", 'w') as outfile:
    json.dump(sorted_file_names, outfile)
