import numpy as np
import cv2
from matplotlib import pyplot as plt

imge=cv2.imread("3500.png")
imge=cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
_,mask=cv2.threshold(imge,230,255,cv2.THRESH_BINARY)
kernel=np.ones((3,3),np.uint8)
dilation=cv2.dilate(mask,kernel)
erosion=cv2.erode(mask,kernel)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

titles=["image","mask","dilation","erosion","opening","closing"]
images=[imge,mask,dilation,erosion,opening,closing]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()