import cv2
import matplotlib as plt
import numpy as np
import os
from PIL import Image
#Imagen original
tornillo0 = cv2.imread('tornillo0.png', 0) #lectura en escala de grises
tornillo1 = cv2.imread('tornillo1.png', 0) #lectura en escala de grises
tornillo2 = cv2.imread('tornillo2.png', 0) #lectura en escala de grises
tornillo3 = cv2.imread('tornillo3.png', 0) #lectura en escala de grises
tornillo4 = cv2.imread('tornillo4.png', 0) #lectura en escala de grises
pinzas4 = cv2.imread('pinzas4.png', 0) #lectura en escala de grises

 

Mtornillo0 = cv2.moments(tornillo0)
Mtornillo1 = cv2.moments(tornillo1)
Mtornillo2 = cv2.moments(tornillo2)
Mtornillo3 = cv2.moments(tornillo3)
Mtornillo4 = cv2.moments(tornillo4)
Mpinzas4 = cv2.moments(pinzas4)
Mtornillo = []
Mtornillo.append([min(Mtornillo0['m21'], Mtornillo1['m21'], Mtornillo2['m21'], Mtornillo3['m21']), 
              max(Mtornillo0['m21'], Mtornillo1['m21'], Mtornillo2['m21'], Mtornillo3['m21'])])
Mtornillo.append([min(Mtornillo0['m01'], Mtornillo1['m01'], Mtornillo2['m01'], Mtornillo3['m01']), 
              max(Mtornillo0['m01'], Mtornillo1['m01'], Mtornillo2['m01'], Mtornillo3['m01'])])
Mtornillo.append([min(Mtornillo0['m11'], Mtornillo1['m11'], Mtornillo2['m11'], Mtornillo3['m11']), 
              max(Mtornillo0['m11'], Mtornillo1['m11'], Mtornillo2['m11'], Mtornillo3['m11'])])
print(Mtornillo)

 

if Mtornillo[0][0] <= Mpinzas4['m21'] and Mpinzas4['m21'] <= Mtornillo[0][1]:
    print('Es un tornillo')
else:
    print('No es un tornillo')

 

if Mtornillo[1][0] <= Mpinzas4['m01'] and Mpinzas4['m01'] <= Mtornillo[1][1]:
    print('Es un tornillo')
else:
    print('No es un tornillo')

 

if Mtornillo[2][0] <= Mpinzas4['m11'] and Mpinzas4['m11'] <= Mtornillo[2][1]:
    print('Es un tornillo')
else:
    print('No es un tornillo')