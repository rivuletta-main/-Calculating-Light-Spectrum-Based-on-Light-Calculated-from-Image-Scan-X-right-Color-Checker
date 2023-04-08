from PIL import Image
import numpy as np
import sys
import os 
import csv
from csv import writer


ilkdoysa="ornek.csv"
def file_write(deger,index):
    with open(ilkdoysa, 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    
    data[index] = data[index] + "," + deger
    h_deger=data[index]
    if(h_deger[0] == ","):
        data[index] = h_deger[1:]


    with open(ilkdoysa, 'w') as file:

        file.writelines( data )


    
    return

file="ornek.jpg"

print(file)
img_file=Image.open(file)
width,height=img_file.size
format=img_file.format
##mode=img_file.node

sunset_resized = img_file.resize((400, 50))
sunset_resized.save('sunset_400.jpeg')
sunset_resized=sunset_resized.convert('L')

#print(sunset_resized.size)  
pix = sunset_resized.load()
#print (pix[4, 10])
#pix[4, 4] = (0, 0, 0)
#print (pix[399, 1])
count = 0;
for s in range(399):
    for i in range(49):
        #print(pix[70, i])
        if(count < 399):
            count += 1

            deger = pix[s, i]
            f = open("ornek.csv", "a")

            #print("samet")
            deger = pix[s, i]
            f = open(ilkdoysa, "a")

            f.writelines(str(deger) +","+ "\n")
            f.close()
        else:
            count += 1
            deger = pix[s, i]
            #print("else")
            file_write(str(deger),s)

    