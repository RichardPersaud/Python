import cv2

image1 = cv2.imread('FD_image.jpg',1)

#image_gray = 0.11+image2[:,:,0]+0.59+image2[:,:,1]+0.3*image2[:,:,2]

cv2.namedWindow('window1', cv2.WINDOW_NORMAL)
cv2.imshow('window1', image1)

image2 = cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)





cv2.namedWindow('hue', cv2.WINDOW_NORMAL)
cv2.imshow('hue',image2[:,:,0])

cv2.namedWindow('saturation', cv2.WINDOW_NORMAL)
cv2.imshow('saturation',image2[:,:,1])

cv2.namedWindow('value', cv2.WINDOW_NORMAL)
cv2.imshow('value',image2[:,:,2])

cv2.waitKey(0)


#need to run through the project folder terminal (imageProcessing folder)