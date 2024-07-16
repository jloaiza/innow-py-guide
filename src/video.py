#!/usr/bin/env python3

from cv2 import VideoCapture, imshow, waitKey, destroyAllWindows

cam_port = 0
vid = VideoCapture(cam_port)

while(True):
  ret, frame = vid.read()

  imshow('frame', frame)

  # the 'q' button is set as the quitting button
  if waitKey(1) & 0xFF == ord('q'):
    break

vid.release()
destroyAllWindows()
