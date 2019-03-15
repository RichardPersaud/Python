import cv2

web_cam = cv2.VideoCapture(0)

cv2.namedWindow('web_cam', cv2.WINDOW_NORMAL)


while (web_cam.isOpened()):
    ret, frame = web_cam.read()
    if ret == True:
     cv2.imshow('web_cam',frame)
     if cv2.waitKey(10) & 0xFF == ord('q'):
        break


web_cam.release()

cv2.destroyAllWindows()