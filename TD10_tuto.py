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
image = cv2.imread('reference_image_logo.png')

##################################
#FEATURES
detector = cv2.xfeatures2d.SURF_create()
keypoints, descriptors = detector.detectAndCompute(image,None)

first_point=keypoints[0]
print("First point ((x,y) coordinates): ", first_point.pt)
first_descriptor=descriptors[0]
print("First descriptor:\n", first_descriptor)

##################################
#DISPLAY
image=cv2.drawKeypoints(image,keypoints,image)
cv2.imshow('frame',image)
cv2.imwrite("ex0.png",image)
cv2.waitKey()
cv2.destroyAllWindows()

