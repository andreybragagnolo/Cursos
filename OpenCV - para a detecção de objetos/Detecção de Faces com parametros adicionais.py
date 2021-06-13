# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:36:43 2021

@author: andy_
"""

import cv2

imagem = cv2.imread('pessoas2.jpg')

classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccao = classificador.detectMultiScale(imagemCinza, scaleFactor=1.01, 
                                          minNeighbors=10, 
                                          minSize= (10,10),
                                          maxSize= (15,15))#scalefactor redimensiona um objeto
#quantos vizinhos cada retângulo candidadto deve ter para manter -> minNeighbors
print(deteccao)

print(len(deteccao))
#[ponto em x, ponto em y, largura , altura]

for(x,y,l,a) in deteccao:
    cv2.rectangle(imagem, (x,y),(x + l, y+a), (0,255,0),2)

cv2.imshow('Detectou çaporra', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()