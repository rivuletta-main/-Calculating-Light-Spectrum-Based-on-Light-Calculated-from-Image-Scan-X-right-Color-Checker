# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:08:41 2022

@author: rhaen
"""

import numpy as np
import sys
import os 
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path


im1 = Image.open("5000.png")
img = np.array(im1)
im = im1.resize((499, 324))

y=0
x=0
h=75
w=75

image_list = []

#while(x != im.size[0]):
#for x in range(0,im.size[0]):
while(x <= im.size[0]):
    y = 0
    while(y <=im.size[1]):
        #ymin, xmin, ymax, xmax
        l = (x) # ymin
        r = (x + w) # ymin + w
        t = (y) # xmin
        b = (y + h) # xmin + h
       
        
        #cropping
        img = im.crop((l,t,r,b))
        im1 = np.array(img)
        image_list.append(im1)
        
        #cropping save
        filename = 'savedImage' + str(x) +'_'+ str(y) + '.png'
        img.save("out_5000/" + filename)
        
        y += 83
        # height + kaydırma oranı
        print(y)
    x += 85
    # width + kaydırma oranı
            
#crop_image = image[x:w, y:h]
rgb_deger = []
#r_deger = []
#g_deger = []
#b_deger = []

for i in range(len(image_list)):
    ch1 = 0
    ch2 = 0
    ch3 = 0
    for y in range(len(image_list[0])):
        ch1 += image_list[i][0][y][0]
        ch1_ort = int(ch1/(75))
        
        ch2 += image_list[i][0][y][1]
        ch2_ort = int(ch2/(75))
        
        ch3 += image_list[i][0][y][2]
        ch3_ort = int(ch3/(75))
        
    rgb_deger.append([ch1_ort, ch2_ort, ch3_ort])
df = pd.DataFrame(rgb_deger, columns =['r', 'g','b'])
    
filepath = Path('out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath,index=False)

#      r_deger.append(ch1_ort)
#    g_deger.append(ch2_ort)
#    b_deger.append(ch3_ort)
