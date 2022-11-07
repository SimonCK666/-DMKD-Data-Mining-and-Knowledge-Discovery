'''
Author: SimonCK666 SimonYang223@163.com
Date: 2022-11-05 23:27:11
LastEditors: SimonCK666 SimonYang223@163.com
LastEditTime: 2022-11-06 12:56:51
FilePath: /Project1/readBMP.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: UTF-8 -*-
import numpy as np
import struct
from PIL import Image

class ImageFile():

    def getBMP(self, filepath):
        f = open(filepath,'rb')             
        f_type = str(f.read(2))             
        file_size_byte = f.read(4)          
        f.seek(f.tell()+4)                  
        file_ofset_byte = f.read(4)         
        f.seek(f.tell()+4)                  
        file_wide_byte = f.read(4)          
        file_height_byte = f.read(4)        
        f.seek(f.tell()+2)                  
        file_bitcount_byte = f.read(4)      

        f_size, = struct.unpack('i', file_size_byte)
        f_ofset, = struct.unpack('i', file_ofset_byte)
        f_wide, = struct.unpack('i', file_wide_byte)
        f_height, = struct.unpack('i', file_height_byte)
        f_bitcount, = struct.unpack('i', file_bitcount_byte)
        print("Type:", f_type, "Size:", f_size, "Bitmap data offset:", f_ofset, "Width:", f_wide, "Height:", f_height, "Bitmap:", f_bitcount)

        color_table = np.empty(shape=[256, 4], dtype=int)
        f.seek(54) 
        for i in range(0, 256):
            b=struct.unpack('B', f.read(1))[0]
            g = struct.unpack('B', f.read(1))[0]
            r = struct.unpack('B', f.read(1))[0]
            alpha = struct.unpack('B', f.read(1))[0]
            color_table[i][0] = r
            color_table[i][1] = g
            color_table[i][2] = b
            color_table[i][3] = 255

        f.seek(f_ofset)
        img = np.empty(shape=[f_height, f_wide, 4], dtype=int)
        cout = 0

        for y in range(0, f_height):
            for x in range(0,f_wide):
                cout = cout + 1
                index = struct.unpack('B', f.read(1))[0]
                img[f_height - y - 1, x] = color_table[index]
            while cout % 4 != 0:
                f.read(1)
                cout = cout+1
        f.close()
        
        fimg = self.ndarry2image(img)
        
        return fimg

    def ndarry2image(self, ndarry):
        # ndarray to image
        ndarry = ndarry.astype("uint8")
        # ndarry = cv2.cvtColor(ndarry, cv2.COLOR_BGR2RGB)
        # ndarry = Image.fromarray(ndarry)
        # ndarry = ndarry.toqpixmap()
        return ndarry
    
    