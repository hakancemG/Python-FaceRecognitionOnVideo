# Author : Hakan Cem Gerçek / hkncm-github.
# Face recognition by input video

#import 'OpenCV' & 'face recognition' libraries.
import cv2
import face_recognition_models

#Get a reference to video.
video_capture = cv2.VideoCapture('videoname.mp4')

#Declare path of Haarcascade.
face_cascade = cv2.CascadeClassifier('C:\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')

while True:

    #Grab a single frame of video.
    ret, frame = video_capture.read()

    #In OpenCV, frames usually turn into grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5)

    #Display results.
    for(x,y,w,h) in faces:        

        color = (0, 127, 255)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

    #Display the result of video.
    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#End.
video_capture.release()
cv2.destroyAllWindows()

# Author : Hakan Cem Gerçek / hkncm-github.
