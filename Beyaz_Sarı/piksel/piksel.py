import numpy as np
import pandas as pd
from PIL import Image,ImageStat


im = Image.open('deneme1.jpg').convert('L')
stat = Imagestat = ImageStat.Stat(im)
print(stat.mean[0])

import cv2
cap = cv2.VideoCapture('http://192.168.1.21:8080/shot.jpg')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == 27:
    exit(0)