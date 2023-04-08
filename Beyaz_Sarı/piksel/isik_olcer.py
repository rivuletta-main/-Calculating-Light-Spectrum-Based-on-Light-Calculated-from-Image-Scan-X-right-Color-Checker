import numpy as np
import cv2
from PIL import Image, ImageStat



cap = cv2.VideoCapture(0)
count=0
while True: #sonsuz döngü
  ret, frame = cap.read()
  image2 = cv2.imshow('Video', frame) # resim göster yakalanan resmi gösterir.
  cv2.imwrite("frame%d.jpg" % count, frame)     # yakalanan resmi yazar.      
  im = Image.open("frame%d.jpg" % count).convert('L') #yazılan dosyaları okudu ve renklerı grıye çevırdı
  stat = ImageStat.Stat(im) # griye çevrilen resmin stadını aldı.
  print(stat.rms[0]) # griye çevrilen resmin stadını aldı.
  if cv2.waitKey(1) & 0xFF == ord("q"): break # uygulamayı sonsuz dongu yapacak şekılde çalıştırır esc ye basana kadar.
   

