#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 07:50:18 2020

@author: macbookleo
"""

import cv2
import tkinter as tk
from PIL import Image, ImageTk

win=tk.Tk()
win.geometry("1280x720")

image1 = Image.open("background.png")
background = ImageTk.PhotoImage(file="background.png")
bg = tk.Label(win, image=background)
bg.pack()
btn = tk.Button(text="START")
btn.place(x=640, y=360)
def button_event(self):
    win.destroy()
btn.bind("<Button-1>",button_event)
win.mainloop()
# ２値化
def binarization(img, threshold=100):
    ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return img

# 差分を数値化
def getDiff(img1, img2):
    # グレースケール変換
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 差分取得
    mask = cv2.absdiff(img1, img2)
    # ２値化
    mask = binarization(mask)
    return cv2.countNonZero(mask) # 白の要素数


span = 50  # 静止間隔
threshold = 8000 # 変化の敷居値

# 動画ファイルのキャプチャ
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
video = cv2.VideoCapture("Fire.mp4")
gif = cv2.VideoCapture("Fire.gif")

# 最初のフレームを背景画像に設定
ret, previous = cap.read()

counter=0

while cap.isOpened():
    # フレームの取得
    ret, frame = cap.read()

    # 差分計算    
    diff = getDiff(previous, frame)

    if diff < threshold:
        counter+=1
    else:
        ret, fire = video.read()
        cv2.imshow("Motion", fire)
        cv2.waitKey(1)

        counter=0
        
        
    # 一定以下の変化量が、一定時間続いたら描画する
    if span < counter:
        counter = 0

    # フレームを表示
    cv2.imshow("Motion", frame)

    # 今回のフレームを１つ前として保存する
    previous = frame

    if cv2.waitKey(30) == 13:
        break

cap.release()
cv2.destroyAllWindows()
