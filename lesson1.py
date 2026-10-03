import cv2

image = cv2.imread("lesson 1-intro/images/pika.png",1)
cv2.imshow("pika",image)
#cv2.waitKey(0)
cv2.imwrite("pika_black+white.jpeg",image)
B,G,R = cv2.split(image)
cv2.imshow("blue channel",R)
cv2.waitKey(0)