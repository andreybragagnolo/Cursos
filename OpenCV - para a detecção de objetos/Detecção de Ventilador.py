# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:16:02 2021

@author: andy_
"""
import cv2

imagem = cv2.imread('eletrodomesticos2.jpg')

classificador = cv2.CascadeClassifier('ventiladorFrontal.xml')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccao = classificador.detectMultiScale(imagemCinza)
print(deteccao)

print(len(deteccao))
#[ponto em x, ponto em y, largura , altura]

for(x,y,l,a) in deteccao:
    cv2.rectangle(imagem, (x,y),(x + l, y+a), (0,255,0),2)

cv2.imshow('Detectou ', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

#CMDER
#automatiza criação das positivas
#λ opencv_createsamples -img ventilador.jpg -bg negativas/bg.txt -info positivas/positivas.lst -maxxangle 0.5 -maxyangle 0.5 -num 1800 -bgcolor 255
#cria o vetor
#λ opencv_createsamples -info positivas/positivas.lst -num 1800 -w 18 -h 18 -vec positivas.vec
#treina
#λ opencv_traincascade -data classificador -vec positivas.vec -bg.txt -numPos 1600 -numNeg 800 -numStages 10 -w 18 -h 18 -precalcBufSize 1024 -precalcIdxBufSize 1024