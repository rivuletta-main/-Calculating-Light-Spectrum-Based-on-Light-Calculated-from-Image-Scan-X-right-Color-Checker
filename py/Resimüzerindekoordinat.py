import numpy as np
import sys
import os 
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path  
  

# Import an image from directory:
im = Image.open("ornek.jpg")


coordinate = x, y = 0, 0
print(im.getpixel(coordinate));
img = im.convert('L')
print(img.getpixel(coordinate));
img = img.resize((400,50))
print(img.size)
nparray = np.array(img)


max_coords = []

for y in range(0,img.size[0]):
    maximum_value=0
    for x in range(0,img.size[1]):
        if(nparray[x,y] > maximum_value):
            maximum_value = nparray[x,y]
            max_val_coord_x = y
            max_val_coord_y = x
    print(maximum_value)
    max_coords.append([max_val_coord_x,max_val_coord_y])

df = pd.DataFrame(max_coords, columns = ['x','y'])

filepath = Path('ornek.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath,index=False)
print(img.size)