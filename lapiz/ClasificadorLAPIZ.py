import cv2
import matplotlib as plt
import numpy as np
import os
from PIL import Image
#Imagen original
lapiz0 = cv2.imread('lapiz0.png', 0) #lectura en escala de grises
lapiz1 = cv2.imread('lapiz1.png', 0) #lectura en escala de grises
lapiz2 = cv2.imread('lapiz2.png', 0) #lectura en escala de grises
lapiz3 = cv2.imread('lapiz3.png', 0) #lectura en escala de grises
lapiz4 = cv2.imread('lapiz4.png', 0) #lectura en escala de grises
goma4 = cv2.imread('goma4.png', 0) #lectura en escala de grises

 

Mlapiz0 = cv2.moments(lapiz0)
Mlapiz1 = cv2.moments(lapiz1)
Mlapiz2 = cv2.moments(lapiz2)
Mlapiz3 = cv2.moments(lapiz3)
Mlapiz4 = cv2.moments(lapiz4)
Mgoma4 = cv2.moments(goma4)
Mlapiz = []
Mlapiz.append([min(Mlapiz0['m21'], Mlapiz1['m21'], Mlapiz2['m21'], Mlapiz3['m21']), 
              max(Mlapiz0['m21'], Mlapiz1['m21'], Mlapiz2['m21'], Mlapiz3['m21'])])
Mlapiz.append([min(Mlapiz0['m01'], Mlapiz1['m01'], Mlapiz2['m01'], Mlapiz3['m01']), 
              max(Mlapiz0['m01'], Mlapiz1['m01'], Mlapiz2['m01'], Mlapiz3['m01'])])
Mlapiz.append([min(Mlapiz0['m11'], Mlapiz1['m11'], Mlapiz2['m11'], Mlapiz3['m11']), 
              max(Mlapiz0['m11'], Mlapiz1['m11'], Mlapiz2['m11'], Mlapiz3['m11'])])
print(Mlapiz)

 

if Mlapiz[0][0] <= Mgoma4['m21'] and Mgoma4['m21'] <= Mlapiz[0][1]:
    print('Es una lapiz')
else:
    print('No es una lapiz')

 

if Mlapiz[1][0] <= Mgoma4['m01'] and Mgoma4['m01'] <= Mlapiz[1][1]:
    print('Es una lapiz')
else:
    print('No es una lapiz')

 

if Mlapiz[2][0] <= Mgoma4['m11'] and Mgoma4['m11'] <= Mlapiz[2][1]:
    print('Es una lapiz')
else:
    print('No es una lapiz')