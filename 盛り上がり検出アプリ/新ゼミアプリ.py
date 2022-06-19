#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 03:23:55 2021

@author: macbookleo
"""

import cv2
import pygame

if __name__=="__main__":
    threshold = 800 # 変化の敷居値
    cap = cv2.VideoCapture(0) # 動画ファイルのキャプチャ
    cap.set(cv2.CAP_PROP_FPS, 30) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) 
    ret, previous = cap.read() # 最初のフレームを背景画像に設定
    counter=0

def binarization(img, threshold=100): # ２値化
    ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return img

def getDiff(img1, img2): # 差分を数値化
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # グレースケール変換
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    mask = cv2.absdiff(img1, img2) # 差分取得
    mask = binarization(mask) # ２値化
    return cv2.countNonZero(mask) # 白の要素数

while cap.isOpened():
    ret, frame = cap.read() #フレームの取得
    cv2.imshow("Motion", frame)    
    diff = getDiff(previous, frame) # 差分計算
    if diff < threshold:
        counter=0
        ret, previous = cap.read()
    else:
        counter+=1
        if counter>=15 and counter<30:
            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
            cv2.imshow("Motion", frame)
            if counter==15:
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("/Users/macbookleo/Desktop/ゼミ/アプリ/スタジアム1.mp3")
                pygame.mixer.music.play(1)
        if counter>=30 and counter<45:
            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            cv2.imshow("Motion", frame)
            if counter==30:
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("/Users/macbookleo/Desktop/ゼミ/アプリ/スタジアム2.mp3")
                pygame.mixer.music.play(1)
        if counter>=45:
            cv2.imshow("Motion", previous)
            if counter == 45:
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("/Users/macbookleo/Desktop/ゼミ/アプリ/スタジアム3.mp3")
                pygame.mixer.music.play(1)
    ret, previous = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        pygame.mixer.music.stop()
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()

