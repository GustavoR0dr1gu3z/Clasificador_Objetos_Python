import cv2
import matplotlib as plt
import numpy as np
import os
from PIL import Image
#Imagen original
pinzas0 = cv2.imread('pinzas0.png', 0) #lectura en escala de grises
pinzas1 = cv2.imread('pinzas1.png', 0) #lectura en escala de grises
pinzas2 = cv2.imread('pinzas2.png', 0) #lectura en escala de grises
pinzas3 = cv2.imread('pinzas3.png', 0) #lectura en escala de grises
pinzas4 = cv2.imread('pinzas4.png', 0) #lectura en escala de grises
tuerca4 = cv2.imread('tuerca4.png', 0) #lectura en escala de grises

 

Mpinzas0 = cv2.moments(pinzas0)
Mpinzas1 = cv2.moments(pinzas1)
Mpinzas2 = cv2.moments(pinzas2)
Mpinzas3 = cv2.moments(pinzas3)
Mpinzas4 = cv2.moments(pinzas4)
Mtuerca4 = cv2.moments(tuerca4)
Mpinzas = []
Mpinzas.append([min(Mpinzas0['m21'], Mpinzas1['m21'], Mpinzas2['m21'], Mpinzas3['m21']), 
              max(Mpinzas0['m21'], Mpinzas1['m21'], Mpinzas2['m21'], Mpinzas3['m21'])])
Mpinzas.append([min(Mpinzas0['m01'], Mpinzas1['m01'], Mpinzas2['m01'], Mpinzas3['m01']), 
              max(Mpinzas0['m01'], Mpinzas1['m01'], Mpinzas2['m01'], Mpinzas3['m01'])])
Mpinzas.append([min(Mpinzas0['m11'], Mpinzas1['m11'], Mpinzas2['m11'], Mpinzas3['m11']), 
              max(Mpinzas0['m11'], Mpinzas1['m11'], Mpinzas2['m11'], Mpinzas3['m11'])])
print(Mpinzas)

 

if Mpinzas[0][0] <= Mtuerca4['m21'] and Mtuerca4['m21'] <= Mpinzas[0][1]:
    print('Es una pinza')
else:
    print('No es una pinza')

 

if Mpinzas[1][0] <= Mtuerca4['m01'] and Mtuerca4['m01'] <= Mpinzas[1][1]:
    print('Es una pinza')
else:
    print('No es una pinza')

 

if Mpinzas[2][0] <= Mtuerca4['m11'] and Mtuerca4['m11'] <= Mpinzas[2][1]:
    print('Es una pinza')
else:
    print('No es una pinza')