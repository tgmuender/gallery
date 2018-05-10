#!/usr/bin/python3

import cv2
import glob
import os
import sys
import piexif
import json
import datetime


class GalleryImage:

    def __init__(self, name):
        self.name = name


def get_exif_meta_data(file_name):
    exif_data = {}
    exif_dict = piexif.load(file_name)
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            key = piexif.TAGS[ifd][tag]["name"]
            exif_data[key] = str(exif_dict[ifd][tag])
    return exif_data


def write_image_meta_data(file_name, img_meta_data):
    image_name = os.path.basename(file_name)
    with open(image_dir + '/metadata/' + image_name + ".json", 'w') as outfile:
        json.dump(img_meta_data, outfile)


def create_thumbnail(file_name):
    image = cv2.imread(file_name)

    height, width = image.shape[:2]
    thumbnail_max_width = 250
    thumbnail_max_height = 250

    if thumbnail_max_height < height or thumbnail_max_width < width:
        scaling_factor = thumbnail_max_height / float(height)
        if thumbnail_max_width/float(width) < scaling_factor:
            scaling_factor = thumbnail_max_width / float(width)
    thumbnail = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    cv2.imwrite(image_dir + "/thumbs/thumb_%s" % basename, thumbnail)


def get_creation_timestamp(exif_data):
    date_created = exif_data['DateTime']
    cleaned_creation_date = date_created.replace("b", '').replace("'", '')
    as_date = datetime.datetime.strptime(cleaned_creation_date, "%Y:%m:%d %H:%M:%S")
    return as_date


image_dir = sys.argv[1]
print("Scanning directory " + image_dir)
path = image_dir + '/*'
files = glob.glob(path)
images = []
for file in files:
    if not file.endswith((".JPG", ".jpg")):
        continue

    if not os.path.exists(image_dir + '/thumbs'):
        os.makedirs(image_dir + '/thumbs')

    if not os.path.exists(image_dir + '/metadata'):
        os.makedirs(image_dir + '/metadata')

    basename = os.path.basename(file)
    print("Found image: " + basename)

    img_exif_data = get_exif_meta_data(file)
    write_image_meta_data(file, img_exif_data)
    create_thumbnail(file)
    images.append((file, img_exif_data))


images.sort(key=lambda img_tpl: get_creation_timestamp(img_tpl[1]).timestamp())
sorted_file_names = []
for img in images:
    sorted_file_names.append(GalleryImage(os.path.basename(img[0])))

with open(image_dir + "/images.json", 'w') as outfile:
    json.dump(sorted_file_names, outfile, default=lambda x: x.__dict__)


