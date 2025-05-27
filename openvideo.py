import cv2
cap=cv2.VideoCapture('video_2025-04-01_09-17-56.mp4')
while True:
    #ret,frame=cap.read()
    frame=cv2.imread('cadr9.jpg')
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()