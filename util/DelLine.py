from PIL import Image
import numpy as np
class demo():

    def __init__(self, path):
        self.image = Image.open(path)
        self.image = self.image.convert('L')

    def test(self):
        threshold = 127
        table = []
        red=[200,20,20]
        i=0
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        self.image = self.image.point(table, '1')
        self.img_array = self.image.load()
        self.image.save(r'C:\Users\musaxi\Desktop\1.jpg')

