import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

imge=cv2.imread("3500.png")
imge=cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)
_,mask=cv2.threshold(imge,230,255,cv2.THRESH_BINARY)
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",closing)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

