'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-05 23:26:13
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-06 00:01:19
FilePath: /Project1/test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2

lena = cv2.imread('lena.png') # import the lena picture
print(type(lena))

import numpy as np
import sys
import cv2
from ReadBMP import ImageFile

# 命令行传入的文件路径
# filePath = sys.argv[1]
filePath = "lena.bmp"
# 读取 BMP 文件
bmpFile = ImageFile()
img = bmpFile.getBMP(filePath)
# img = bmpFile.ndarry2image(bmp)
print(type(img))
cv2.imshow("bmpFile", img)
cv2.waitKey(0)
