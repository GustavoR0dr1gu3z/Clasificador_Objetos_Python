import cv2
import matplotlib as plt
import numpy as np
import os
from PIL import Image
#Imagen original
tuerca0 = cv2.imread('tuerca0.png', 0) #lectura en escala de grises
tuerca1 = cv2.imread('tuerca1.png', 0) #lectura en escala de grises
tuerca2 = cv2.imread('tuerca2.png', 0) #lectura en escala de grises
tuerca3 = cv2.imread('tuerca3.png', 0) #lectura en escala de grises
tuerca4 = cv2.imread('tuerca4.png', 0) #lectura en escala de grises
goma4 = cv2.imread('goma4.png', 0) #lectura en escala de grises

 

Mtuerca0 = cv2.moments(tuerca0)
Mtuerca1 = cv2.moments(tuerca1)
Mtuerca2 = cv2.moments(tuerca2)
Mtuerca3 = cv2.moments(tuerca3)
Mtuerca4 = cv2.moments(tuerca4)
Mgoma4 = cv2.moments(goma4)
Mtuerca = []
Mtuerca.append([min(Mtuerca0['m21'], Mtuerca1['m21'], Mtuerca2['m21'], Mtuerca3['m21']), 
              max(Mtuerca0['m21'], Mtuerca1['m21'], Mtuerca2['m21'], Mtuerca3['m21'])])
Mtuerca.append([min(Mtuerca0['m01'], Mtuerca1['m01'], Mtuerca2['m01'], Mtuerca3['m01']), 
              max(Mtuerca0['m01'], Mtuerca1['m01'], Mtuerca2['m01'], Mtuerca3['m01'])])
Mtuerca.append([min(Mtuerca0['m11'], Mtuerca1['m11'], Mtuerca2['m11'], Mtuerca3['m11']), 
              max(Mtuerca0['m11'], Mtuerca1['m11'], Mtuerca2['m11'], Mtuerca3['m11'])])
print(Mtuerca)

 

if Mtuerca[0][0] <= Mgoma4['m21'] and Mgoma4['m21'] <= Mtuerca[0][1]:
    print('Es una tuerca')
else:
    print('No es una tuerca')

 

if Mtuerca[1][0] <= Mgoma4['m01'] and Mgoma4['m01'] <= Mtuerca[1][1]:
    print('Es una tuerca')
else:
    print('No es una tuerca')

 

if Mtuerca[2][0] <= Mgoma4['m11'] and Mgoma4['m11'] <= Mtuerca[2][1]:
    print('Es una tuerca')
else:
    print('No es una tuerca')