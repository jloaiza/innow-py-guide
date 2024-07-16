#!/usr/bin/env python3

# CSpell:locale es

# Importar únicamente los módulos requeridos

from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow

cam_port = 0
cam = VideoCapture(cam_port)
result, image = cam.read()

if result:
  imwrite("INNOWimage.png", image)
  imshow("INNOWimage", image)
  waitKey(0)
  destroyWindow("INNOWimage")

else:
  print("No image detected. Please! try again")
