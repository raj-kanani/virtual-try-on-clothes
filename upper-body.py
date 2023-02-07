import numpy as np
import cv2

cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

imgPath = 'human.jpeg'
img = cv2.imread(imgPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

body = cascade.detectMultiScale(
    gray,
    scaleFactor=2.1,
    minNeighbors=10,
    minSize=(50, 50),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in body:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Upper Body', img)
cv2.imshow('Upper gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
