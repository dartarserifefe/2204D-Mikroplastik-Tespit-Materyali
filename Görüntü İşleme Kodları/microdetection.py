import cv2
from cv2.cv2 import VideoCapture

cap: VideoCapture = cv2.VideoCapture(1)
#cap: VideoCapture = cv2.VideoCapture('cekim.mp4')

microplast_cascade = cv2.CascadeClassifier('microplastik.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    microplastiks = microplastik_cascade.detectMultiScale(gray, 1.9, 1)
    
    # Display the resulting frame
    for (x,y,w,h) in microplastiks:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
         cv2.putText(frame, "hedef", (x + 20, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
         

    cv2.imshow('frame',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
