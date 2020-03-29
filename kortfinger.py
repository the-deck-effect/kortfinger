import os
import cv2

image = cv2.imread(os.path.join(os.getcwd(), 'm19-94-duress.jpg'))

cv2.imshow('Durress', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)

edges = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)