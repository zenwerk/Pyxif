import os

import pyxif
from PIL import Image


def load_sample(input_file):
    zeroth_dict, exif_dict, gps_dict = pyxif.load(input_file)

    print("******************************")
    print("0th IFD: {0}".format(len(zeroth_dict)))
    for key in sorted(zeroth_dict):
        print(key, zeroth_dict[key])

    print("\nEXIF IFD: {0}".format(len(exif_dict)))
    for key in sorted(exif_dict):
        if isinstance(exif_dict[key][1], (str, bytes)) and len(exif_dict[key][1]) > 30:
            print(key, exif_dict[key][0], exif_dict[key][1][:10] + b"...", len(exif_dict[key][1]))
        else:
            print(key, exif_dict[key])

    print("\nGPS IFD: {0}".format(len(gps_dict)))
    for key in sorted(gps_dict):
        if isinstance(gps_dict[key][1], (str, bytes)) and len(gps_dict[key][1]) > 30:
            print(key, gps_dict[key][0][:10], gps_dict[key][1][:10] + b"...", len(exif_dict[key][1]))
        else:
            print(key, gps_dict[key])


def dump_sample(input_file, output_file):
    zeroth_ifd = {pyxif.ImageGroup.Make: "foo",
                  pyxif.ImageGroup.XResolution: (96, 1),
                  pyxif.ImageGroup.YResolution: (96, 1),
                  pyxif.ImageGroup.Software: "paint.net 4.0.3",
                  }

    exif_bytes = pyxif.dump(zeroth_ifd=zeroth_ifd)
    im = Image.open(input_file)
    im.thumbnail((100, 100), Image.ANTIALIAS)
    im.save(output_file, exif=exif_bytes)


def remove_sample():
    pyxif.remove(os.path.join("samples", "01.jpg"),
                 "remove_sample.jpg")


def thumbnail_sample():
    pyxif.thumbnail(os.path.join("samples", "01.jpg"),
                    "thumbnail_sample.jpg",
                    (80, 80))


def transplant_sample():
    pyxif.transplant(os.path.join("samples", "01.jpg"),
                     os.path.join("samples", "02.jpg"),
                     "transplant_sample.jpg")


def insert_sample():
    zeroth_ifd = {282: (96, 1),
                  283: (96, 1),
                  296: 2,
                  305: 'paint.net 4.0.3'}
    exif_bytes = pyxif.dump(zeroth_ifd)
    pyxif.insert(exif_bytes,
                 "remove_sample.jpg",
                 "insert_sample.jpg")


if __name__ == "__main__":
    load_sample(os.path.join("samples", "01.jpg"))
    dump_sample(os.path.join("samples", "01.jpg"), "dump_sample.jpg")
    remove_sample()
    thumbnail_sample()
    transplant_sample()
    insert_sample()