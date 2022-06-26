import os
import time
import datetime

import cv2
from PIL import Image
import easyocr
reader = easyocr.Reader(['ch_sim', 'en'],gpu=False)
path=r"C:\Users\musaxi\Desktop\test"
def read_directory(directory_name):
    for filename in os.listdir(directory_name):
        result = reader.readtext(directory_name + "\\" + filename,detail=0)
        print(result)
read_directory(path)