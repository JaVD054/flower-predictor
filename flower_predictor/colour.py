import cv2
import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image


# Kmeans color segmentation
def kmeans_color_quantization(image, clusters=8, rounds=1):
    h, w = image.shape[:2]
    samples = np.zeros([h*w,3], dtype=np.float32)
    count = 0

    for x in range(h):
        for y in range(w):
            samples[count] = image[x][y]
            count += 1

    compactness, labels, centers = cv2.kmeans(samples,
            clusters, 
            None,
            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
            rounds, 
            cv2.KMEANS_RANDOM_CENTERS)

    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    return res.reshape((image.shape))

#Read Image
def show_colours(path):
    img = cv2.imread(path)
    original = img.copy()
    kmeans = kmeans_color_quantization(img, clusters=4)



    # Convert to grayscale, Gaussian blur, adaptive threshold
    gray = cv2.cvtColor(kmeans, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,2)


    # Draw largest enclosing circle onto a mask
    mask = np.zeros(original.shape[:2], dtype=np.uint8)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        ((x, y), r) = cv2.minEnclosingCircle(c)
        cv2.circle(img, (int(x), int(y)), int(r), (36, 255, 12), 2)
        cv2.circle(mask, (int(x), int(y)), int(r), 255, -1)
        break


    # Bitwise-and for result
    result = cv2.bitwise_and(original, original, mask=mask)
    result[mask==0] = (255,255,255)


# Convert from BGR to RGB

    img=cv2.cvtColor(result,cv2.COLOR_BGR2RGB)

    # Convert from RGB to HSV

    img_HSV = cv2.cvtColor(img , cv2.COLOR_RGB2HSV)

# HSV Ranges for DIfferent Colors

    redlower = np.array([0,150,50])
    redupper = np.array([10,255,255])

    yellowlower = np.array([25,150,50])
    yellowupper = np.array([35,255,255])

    greenlower = np.array([35,100,50])
    greenupper = np.array([70,255,255])

    bluelower = np.array([100,150,0])
    blueupper = np.array([140,255,255])

    orangelower = np.array([15,150,0])
    orangeupper = np.array([25,255,255])

    blacklower = np.array([0,0,0])
    blackupper = np.array([250,255,30])

    whitelower = np.array([0,0,168])
    whiteupper = np.array([172,111,255])


    cyanlower = np.array([85,150,0])
    cyanupper = np.array([95,255,255])


    colors = []


# Creating Masks for Colors

    redmask = cv2.inRange(img_HSV,redlower,redupper)
    yellowmask = cv2.inRange(img_HSV,yellowlower,yellowupper)
    greenmask = cv2.inRange(img_HSV,greenlower,greenupper)
    bluemask = cv2.inRange(img_HSV,bluelower,blueupper)
    orangemask = cv2.inRange(img_HSV,orangelower,orangeupper)
    blackmask = cv2.inRange(img_HSV,blacklower,blackupper)
    whitemask = cv2.inRange(img_HSV,whitelower,whiteupper)
    cyanmask = cv2.inRange(img_HSV,cyanlower,cyanupper)




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

    return colors
    plt.imshow(img)
    plt.show()
