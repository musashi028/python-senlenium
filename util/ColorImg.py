from PIL import Image

img = Image.open(r"C:\Users\musaxi\Desktop\1.png")#读取系统的内照片

width = img.size[0]#长度
height = img.size[1]#宽度
img_array = img.load()
for x in range(1, width - 1):
    for y in range(1, height - 1):
        count = 0
        if img_array[x, y] == img_array[x - 1, y + 1]:
            count += 1
        if img_array[x, y] == img_array[x, y + 1]:
            count += 1
        if img_array[x, y] == img_array[x + 1, y + 1]:
            count += 1
        if img_array[x, y] == img_array[x - 1, y]:
            count += 1
        if img_array[x, y] == img_array[x + 1, y]:
            count += 1
        if img_array[x, y] == img_array[x - 1, y - 1]:
            count += 1
        if img_array[x, y] == img_array[x, y - 1]:
            count += 1
        if img_array[x, y] == img_array[x + 1, y - 1]:
            count += 1
        if count <= 3 and count > 0:
            img.putpixel((x,y),(255,255,255))
img = img.convert("RGB")#把图片强制转成RGB
img.save(r"C:\Users\musaxi\Desktop\2.png")#保存修改像素点后的图片