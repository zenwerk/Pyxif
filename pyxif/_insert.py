"""
"""

import io
import struct

from ._common import *


def insert(exif_bytes, image, new_file=""):
    """Inserts exif bytes to JPEG file
    insert(exif_bytes, image, new_file[optional])
    When "new_file" is not given, "image" file is overwritten.
    """
    if exif_bytes[0:6] != b"\x45\x78\x69\x66\x00\x00":
        raise ValueError("Given data is not exif data")
    exif_bytes = b"\xff\xe1" + struct.pack(">H", len(exif_bytes) + 2) + exif_bytes

    output_file = False
    if image[0:2] == b"\xff\xd8":
        image_data = image
    else:
        with open(image, 'rb') as f:
            image_data = f.read()
        if image_data[0:2] != b"\xff\xd8":
            raise ValueError
        output_file = True
    segments = split_into_segments(image_data)
    image_exif = get_exif(segments)

    if image_exif:
        new_data = image_data.replace(image_exif, exif_bytes)
    else:
        p = image_data.find(b"\xff\xdb")
        new_data = image_data[0:p] + exif_bytes + image_data[p:]

    if isinstance(new_file, io.BytesIO):
        new_file.write(new_data)
        new_file.seek(0)
    elif new_file:
        with open(new_file, "wb+") as f:
            f.write(new_data)
    elif output_file:
        with open(image, "wb+") as f:
            f.write(new_data)
    else:
        raise ValueError("Give a 3rd argment to 'insert' to output file")