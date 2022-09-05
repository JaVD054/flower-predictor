import cv2
import numpy as np
import matplotlib.pyplot as plt

#Read Image

img = cv2.imread('default.jpg')

# Convert from BGR to RGB

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Convert from RGB to HSV

img_HSV = cv2.cvtColor(img , cv2.COLOR_RGB2HSV)

# HSV Ranges for DIfferent Colors

redlower = np.array([0,150,50])
redupper = np.array([10,255,255])

yellowlower = np.array([25,150,50])
yellowupper = np.array([35,255,255])

greenlower = np.array([35,100,50])
greenupper = np.array([70,255,255])

bluelower = np.array([95,150,0])
blueupper = np.array([110,255,255])

orangelower = np.array([15,150,0])
orangeupper = np.array([25,255,255])

blacklower = np.array([0,0,0])
blackupper = np.array([250,255,30])

whitelower = np.array([0,0,168])
whiteupper = np.array([172,111,255])


colors = []


# Creating Masks for Colors

redmask = cv2.inRange(img_HSV,redlower,redupper)
yellowmask = cv2.inRange(img_HSV,yellowlower,yellowupper)
greenmask = cv2.inRange(img_HSV,greenlower,greenupper)
bluemask = cv2.inRange(img_HSV,bluelower,blueupper)
orangemask = cv2.inRange(img_HSV,orangelower,orangeupper)
blackmask = cv2.inRange(img_HSV,blacklower,blackupper)
whitemask = cv2.inRange(img_HSV,whitelower,whiteupper)




if cv2.countNonZero(redmask) > 0 :
    colors += ["red"]

if cv2.countNonZero(yellowmask) > 0 :
    colors+= ["yellow"]

if cv2.countNonZero(greenmask) > 0 :
    colors+=["green"]

if cv2.countNonZero(bluemask) > 0 :
    colors+=["blue"]

if cv2.countNonZero(orangemask) > 0 :
    colors+=["orange"]

if cv2.countNonZero(blackmask) > 0 :
    colors+=["black"]

if cv2.countNonZero(whitemask) > 0 :
    colors+=["white"]

print(colors)


plt.imshow(img)
plt.show()



