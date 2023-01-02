import sys
import socket
import os
import time


lhost = sys.argv[1]
lport = int(sys.argv[2])
file_path = sys.argv[3]


def get_image_bytes(path):
    with open(path, "rb") as file_bytes_object:
        file_bytes = file_bytes_object.read()
        file_size = file_bytes_object.seek(0, os.SEEK_END)

    file_name = path.split("/")[-1]
    return file_bytes, file_size, file_name
