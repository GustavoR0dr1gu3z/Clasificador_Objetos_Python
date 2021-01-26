import cv2
import matplotlib as plt
import numpy as np
import os
from PIL import Image
#Imagen original
goma0 = cv2.imread('goma0.png', 0) #lectura en escala de grises
goma1 = cv2.imread('goma1.png', 0) #lectura en escala de grises
goma2 = cv2.imread('goma2.png', 0) #lectura en escala de grises
goma3 = cv2.imread('goma3.png', 0) #lectura en escala de grises
goma4 = cv2.imread('goma4.png', 0) #lectura en escala de grises
lapiz4 = cv2.imread('lapiz4.png', 0) #lectura en escala de grises

 

Mgoma0 = cv2.moments(goma0)
Mgoma1 = cv2.moments(goma1)
Mgoma2 = cv2.moments(goma2)
Mgoma3 = cv2.moments(goma3)
Mgoma4 = cv2.moments(goma4)
Mlapiz4 = cv2.moments(lapiz4)
MGOMA = []
MGOMA.append([min(Mgoma0['m21'], Mgoma1['m21'], Mgoma2['m21'], Mgoma3['m21']), 
              max(Mgoma0['m21'], Mgoma1['m21'], Mgoma2['m21'], Mgoma3['m21'])])
MGOMA.append([min(Mgoma0['m01'], Mgoma1['m01'], Mgoma2['m01'], Mgoma3['m01']), 
              max(Mgoma0['m01'], Mgoma1['m01'], Mgoma2['m01'], Mgoma3['m01'])])
MGOMA.append([min(Mgoma0['m11'], Mgoma1['m11'], Mgoma2['m11'], Mgoma3['m11']), 
              max(Mgoma0['m11'], Mgoma1['m11'], Mgoma2['m11'], Mgoma3['m11'])])
print(MGOMA)

 

if MGOMA[0][0] <= Mlapiz4['m21'] and Mlapiz4['m21'] <= MGOMA[0][1]:
    print('Es una goma')
else:
    print('No es una goma')

 

if MGOMA[1][0] <= Mlapiz4['m01'] and Mlapiz4['m01'] <= MGOMA[1][1]:
    print('Es una goma')
else:
    print('No es una goma')

 

if MGOMA[2][0] <= Mlapiz4['m11'] and Mlapiz4['m11'] <= MGOMA[2][1]:
    print('Es una goma')
else:
    print('No es una goma')