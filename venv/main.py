import numpy as np
# Why isn't it open-python???
import cv2 as cv
from cv2 import *
# Nice, easy import game
from playsound import playsound

# # Can we play audio? Yes
# input("Is this instant?")
# playsound('./audio/noice.mp3')

# Can we we display the Webcam?
window_name = 'window_1'

# We can set the resolution of the camera with these settings
# It also matters for image overlays
WIDTH = 1000
HEIGHT = 1000

# This allows us to manually set the resolution
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# When the camera's broke, Python will let us know
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Set our named window to be full screen on startup, this doesn't affect the camera resolution
cv.namedWindow(window_name, cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty(window_name, cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# Read an image that's in a directory
im1 = cv.imread('./images/gandm.png')
# IT MUST BE THE SAME SIZE AS THE CAMERA
# As long as WIDTH and HEIGHT are used this should never break.
# Images will be stretched to fit the camera though, so we need to decide:
# Permanent RESOLUTION and native IMAGE_SIZE
im1 = cv.resize(im1, (WIDTH, HEIGHT))

# Begin the while loop for capturing video
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Overlay an image, not sure exactly how we'll choose the image for display just yet
    # added_image = cv.addWeighted(frame, 0.4, im1, 0.6, 0)
    # Add a color coding to the frame
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    # Tell it to flip the resulting color matrix
    rotate = cv.rotate(color, 0)

    # Display the resulting frame
    cv.imshow(window_name, rotate)

    # Here's an example of how to run commands while the code is running
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()



