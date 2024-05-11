import cv2
from pyzbar.pyzbar import decode
import time
cap=cv2.VideoCapture(0)#for capturing image from camera
cap.set(3,640) # 3 is the width of the frame
cap.set(4,480)  #4 is the height of the frame
camera = True
while camera==True:
    success,frame=cap.read()#frame = image
    
    for code in decode(frame):
        print(code.type)
        print(code.data.decode("utf-8"))
        time.sleep(2)
    cv2.imshow("testing",frame)#opening a new window for opening a window showing camera
    cv2.waitKey(1)