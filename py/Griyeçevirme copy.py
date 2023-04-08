import cv2
img = cv2.imread("5500.jpg")
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("5500.png",gray_image)