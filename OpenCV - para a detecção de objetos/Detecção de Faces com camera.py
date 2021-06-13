# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:55:48 2021

@author: andy_
"""


import cv2

video = cv2.VideoCapture(0)


classificador = cv2.CascadeClassifier('ovelhas.xml')

while True:
    conectado, frame = video.read()
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    deteccao = classificador.detectMultiScale(imagemCinza)
    
    #[ponto em x, ponto em y, largura , altura]
    

    
    for(x,y,l,a) in deteccao:
        cv2.rectangle(frame, (x,y),(x + l, y+a), (0,255,0),2)
    cv2.imshow('Detectou çaporra', frame)   
        
    if cv2.waitKey(1)==ord('j'):
        break

video.release()
cv2.destroyAllWindows()

#CMDER
# Ajustes de parâmetros : Aumentar o tamanho da imagem criada (Exemplo: 20x20; 48x48)
#
#
#
#automatiza criação das positivas
#opencv_createsamples -img ovelha4.jfif -bg negativas/bg.txt -info OvelhasPositivas4/OvelhasPositivas4.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -w 48 -h 48 -num 1800 -bgcolor 255 -bgthresh 8
#cria o vetor final
#λ opencv_createsamples -info positivas/positivas.lst -num 1800 -w 18 -h 18 -vec positivas.vec
#cria o vetor final unindo os vetores de mais de uma imagem de treinamento
#python mergevec.py -v vetores/ -o vetores_final.vec -> Codigo para mergevec pra juntar todos os vetores
#treina
#λ opencv_traincascade -data classificador -vec vetores_final.vec -bg.txt -numPos 800 -numNeg 400 -numStages 15 -w 48 -h 48 -precalcBufSize 2048 -precalcIdxBufSize 2048