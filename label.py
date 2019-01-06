import cv2
import label_image
import time
import pygame
import os


    
#faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
#cap.set(3,640) # set Width
#cap.set(4,480) # set Height
pygame.mixer.init()



size = 4


# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#classifier = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
counter = 0
#/cap = cv2.VideoCapture(0) #Using default WebCam connected to the PC.
oldtext = "Sad"
while True:        # we'll assume that the pot didn't move
    (rval, im) = cap.read()
    print(rval)
    #im = cv2.imread("fam.jpg")
    im=cv2.flip(im,1,0) #Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))
    gray = cv2.cvtColor(mini, cv2.COLOR_BGR2GRAY)
    # detect MultiScale / faces 
    faces = classifier.detectMultiScale(gray,1.2,5)
    #im = faces
    
    
    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        
        #Save just the rectangle faces in SubRecFaces
        sub_face = im[y:y+h, x:x+w]

        FaceFileName = "test.jpg" #Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        
        text = label_image.main(FaceFileName)# Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()# Title Case looks Stunning.
        
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)
        print(counter)   
        if(text !=None):
            if(text == oldtext):
                print("euqual")
                counter+=1
            else:
                counter = 0
                oldtext = text
            if(counter >0 and counter <2):
                if text == "Sad":
                    print("sadddddd")
                    pygame.mixer.music.load("Sad S1wav.wav")
                    pygame.mixer.music.play()
                elif text == "Anger":
                    pygame.mixer.music.load("Angry S1_01.wav")
                    pygame.mixer.music.play()
                    print("anger")
                elif text == "Happy":
                    print("happyp")
                    pygame.mixer.music.load("Happy.wav")
                    pygame.mixer.music.play()
                elif text == "neutral":
                    print("neutrall")
                    pygame.mixer.music.load("Neutral S1.wav")
                    pygame.mixer.music.play()
                counter = 0
            
        else:
            print("No face detected  ")
            counter = 0
   # time.sleep(3)            
        # Show the image
    cv2.namedWindow('Capture', cv2.WINDOW_NORMAL)
    cv2.imshow('Capture',   im)
    key = cv2.waitKey(30)
    # if Esc key is press then break out of the loop 
    if key == 27: #The Esc key
       break
    time.sleep(0.5)
cap.release()
cv2.destroyAllWindows()
