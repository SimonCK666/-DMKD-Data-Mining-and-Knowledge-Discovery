'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-05 23:25:00
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-06 13:06:00
FilePath: /Project1/transformBins.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ReadBMP import ImageFile

'''
change the image to 1 bit image (binary image)
the func complete the bin number is 2 operation
'''
def to_bin(lena2):
    # transform the picture into array type
    arr_lena = np.asarray(lena2) 
    for row in range(len(arr_lena)):
        for column in range(len(arr_lena[row])):
            if (arr_lena[row][column] >= 255 / 2).any():  
                # if this pixel's value is less than 127.5, make it white
                arr_lena[row][column] = 255
            else:  
                # otherwise, make it black
                arr_lena[row][column] = 0
    plt.subplot(2, 3, 1)
    plt.title("2 Bins")
    plt.imshow(arr_lena)


def to_x_bins(lena, bins):
    if (bins == 2):
        to_bin(lena)
        return
    arr_lena = np.asarray(lena)
    for row in range(len(arr_lena)):
        for column in range(len(arr_lena[row])):
            for x in range(1, bins):
                # spilt = half of a bin
                split = 255 * (1 / bins) / 2  
                if (arr_lena[row][column] < split).any():  
                    # the first bin
                    arr_lena[row][column] = 0
                elif (arr_lena[row][column] >= 255 * (x / bins) - split).any():
                    # if this pixel is in this bin
                    if (arr_lena[row][column] < 255 * (x / bins) + split).any():  
                        # change value
                        arr_lena[row][column] = 255 * (x / bins)  
                elif (arr_lena[row][column] >= 255 - split).any():  
                    # the last bin
                    arr_lena[row][column] = 255
    plt.subplot(2, 3, bins - 1)
    plt.imshow(arr_lena)
    plt.title("%s Bins" % bins)

'''
Visualize 2 to 7 bins
'''
for bin in range(2, 8):
    print(bin)
    # load bmp image
    bmpFile = ImageFile()
    lena2 = bmpFile.getBMP('lena.bmp')
    lena2 = cv2.cvtColor(lena2, cv2.COLOR_BGR2RGB)
    to_x_bins(lena2, bin)
plt.show()
