# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:28:01 2021

@author: Z!!V
"""

'''About the project : Make a Real-time/ live Sketch making script using OpenCV
in Python. OpenCV makes it very easy for us to work with images and videos on
the computer. Will also make use of Numpy and Matplotlib to make this live
sketch app.'''

# importing opencv library
import cv2
import numpy as np

def sketch(image):
    #height and width of the image
    heigth = int(image.shape[0])
    width = int(image.shape[1])

    #storing the image dimension
    dim = (width,heigth)

    # resizing the image into my own dimension
    resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # applying kernel
    '''Kernels in computer vision are matrices, used to perform some kind of
    convolution in our data.
    Convolutions are mathematical operations between two functions that create
    a third function. In image processing, it happens by going through each
    pixel to perform a calculation with the pixel and its neighbours.
    The kernels will define the size of the convolution, the weights applied
    to it, and an anchor point usually positioned at the center.'''

    kernel=np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])

    #sharpning the resized image
    '''Applying the sharpening filter will sharpen the edges in the image.
    This filter is very useful when we want to enhance the edges in an image
    that's not crisp.'''
    sharp = cv2.filter2D(resize, -1, kernel)

    #converting the image into rescale
    gray = cv2.cvtColor(sharp, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray

    # blurring the image
    '''In Gaussian Blur operation, the image is convolved with a Gaussian filter
    instead of the box filter. The Gaussian filter is a low-pass filter that
    removes the high-frequency components are reduced.'''
    blur = cv2.GaussianBlur(src=inv, ksize=(15,15), sigmaX=0, sigmaY=0)

    #build sketch
    s = cv2.divide(gray, 255-blur, scale=256)

    return s

'''cap = cv.VideoCapture(0)

VideoCapture() Function is used to capture video either from the camera or
already recorded video. cap variable returns a boolean value (True if able to
retrieve/capture video successfully, False if not able to successfully capture
the video). It takes one parameter:
    0 – Front Camera
    1 – Rear Camera

If the Cap returns True, then read() function is applied to it and it
returns two things:
    Boolean Value (Was it successfully able to read the frame, If yes)
    Returns the frame of the video.

Each Frame is sent to a sketch() function that takes frame as input parameter
and manipulates it to return sketch of the frame.

Don’t forget to release the captured video at the end of the while loop.
Otherwise, it will consume all your machine’s memory.'''

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Sketch', sketch(frame))
    cv2.imshow('Live_image', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
