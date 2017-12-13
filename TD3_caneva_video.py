# -*- coding: latin-1 -*-
#########################################################
#Author: Jean-Baptiste Fasquel, ISTIA, Angers University, France
#Copyright (C) 2014 Jean-Baptiste Fasquel
#########################################################

import cv2
import numpy as np
import helper
##################################
#REFERENCE IMAGE
cap = cv2.VideoCapture('video_damier.m4v') #0 webcam integre
pattern_size=(5,8) #Connaissance geometrie damier: nombre de cases en ligne et colonne
while(cap.isOpened()): #e.g. cam unplugged
    ret, image = cap.read()
    if ret==True:
        #Automatic detection of corners
        retval,corners2d=cv2.findChessboardCorners(image, pattern_size)
        if retval:
            corners2d=corners2d.reshape(-1,2)
            cv2.drawChessboardCorners(image, pattern_size, corners2d, patternWasFound=retval)
            text="text "+ str(10.0)
            cv2.putText(image,text,(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
            circle_center=(100,400)
            cv2.circle(image,circle_center, 20, (0, 0, 255), thickness=10)
            
            cv2.imshow('frame',image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

#Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()