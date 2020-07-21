import cv2 
import numpy as np

cap = cv2.VideoCapture(0) 

while(1): 
	ret, frame = cap.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	lower_yellow = np.array([18, 94, 140]) 
	upper_yellow = np.array([48, 255, 255]) 
	mask = cv2.inRange(hsv, lower_yellow, upper_yellow) 
	res = cv2.bitwise_and(frame,frame, mask= mask) 
	cv2.imshow('Original',frame) 
	edges = cv2.Canny(frame,100,200)
	lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=150)
	cv2.imshow('Edges',edges) 
	k = cv2.waitKey(5) & 0xFF
	if k == 27: 
		break
	
cap.release() 

cv2.destroyAllWindows() 
