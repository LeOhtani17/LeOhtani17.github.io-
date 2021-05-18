#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 14:58:50 2020

@author: reo
"""

import random
import tkinter
import pygame
import time

    
def start():
    global x
    x=0
    button_start.destroy()
    button_next.place_forget()
    button_change.place_forget()
    for i in range(22):
        img3.append(tkinter.PhotoImage(file="./Media/Start"+str(number[i])+".png",master=win))
    cvs.create_image(320,300,image=img3[x],tag="im")
    for i in range(20):
        cvs.update()
        time.sleep(0.12)
        cvs.delete("im")
        x=x+1
        cvs.create_image(320,300,image=img3[x],tag="im")
    for i in range(21,22):
        cvs.update()
        time.sleep(1.5)
        cvs.delete("im")
        cvs.create_image(320,300,image=img3[i],tag="im")
    pygame.mixer.init(frequency=48000)
    pygame.mixer.music.load("./Media/Start.wav")
    pygame.mixer.music.play(1)
    for i in range(22,23):
        cvs.update()
        time.sleep(3.0)
        cvs.delete("im")
        cvs.create_image(320,300,image=img3[i-1],tag="im")
        button_change.place(x=250,y=230)
        button_next.place(x=250,y=230)
        button_change.lift()
        cvs.delete("im")
    poker_main()
    
def deal():
    global card,my_cardimage,com_cardimage,deck
    deck=list(range(53))
    random.shuffle(deck)
    for i in range(5):
        my_card.append(deck.pop(0))
        com_card.append(deck.pop(0))
    my_cardimage=[card_image[my_card[i]] for i in range(5)]
    com_cardimage=["z01"]*5
    open_card(my_cardimage,my_im,80,370)
    open_card(com_cardimage,com_im,80,100)

def open_card(cardimg,im,xx,yy):
    im.clear()
    for i in range(5):
        im.append(tkinter.PhotoImage(file="./11820289 card/"+cardimg[i]+".png",master=win))
        cvs.create_image(i*120+xx,yy,image=im[i],tag="ci")
    
def selection(event):
    if event.widget["text"]==u"select1":
        s=0
    elif event.widget["text"]==u"select2":
        s=1   
    elif event.widget["text"]==u"select3":
        s=2
    elif event.widget["text"]==u"select4":
        s=3
    elif event.widget["text"]==u"select5":
        s=4
    if select_list[s]==0:
        cvs.create_rectangle(120*s+30,295,120*s+130,445,tag="sl"+str(s+1),outline="red",width="5")
        select_list[s]=1
        pygame.mixer.init(frequency=48000)
        pygame.mixer.music.load("./Media/select_on.wav")
        pygame.mixer.music.play(1)
                
    else:
        cvs.delete("sl"+str(s+1))
        select_list[s]=0
        pygame.mixer.init(frequency=48000)
        pygame.mixer.music.load("./Media/select_off.wav")
        pygame.mixer.music.play(1)
        
def change():
    global x
    x=0
    pygame.mixer.init(frequency=48000)
    pygame.mixer.music.load("./Media/Change.wav")
    pygame.mixer.music.play(1)
    for s in range(5):
        if select_list[s]==1:
            cvs.delete("s1"+str(s+1))
            my_card[s]=deck.pop(0)
    cvs.delete("ci")
    my_cardimage.clear()
    com_cardimage.clear()
    for i in range(5):
        my_cardimage.append(card_image[my_card[i]]) 
        com_cardimage.append(card_image[com_card[i]])
    open_card(my_cardimage,my_im,80,370)
    open_card(com_cardimage,com_im,80,100)
    judge(my_card,my_hand)
    judge(com_card,com_hand)
    button_next.lift()
    button_change.lower()
    button_next.place_forget()
    button_change.place_forget()
    for i in range(0,5):
        button_select[i].place_forget()
    for i in range(13):
        img.append(tkinter.PhotoImage(file="./Media/Change"+str(number[i])+".png",master=win))
    cvs.create_image(320,240,image=img[x],tag="im")
    button_change.place_forget()
    for i in range(12):
        cvs.update()
        time.sleep(0.2)
        cvs.delete("im")
        x=x+1
        cvs.create_image(320,240,image=img[x],tag="im")
    if x==12:
        time.sleep(2.0)
        button_next.place(x=250,y=230)
        cvs.delete("im")
        vs(my_hand,com_hand,hand_str)
        finish()
    
    for i in range(5):
        button_select[i].lower()

def judge(j_card,j_hand):
    joker=0
    for i in range(5):
        if j_card[i]==0:
            joker=1
            j_card[i]=-99
            
    pair=0
    hi_pair=[]
    
    hi_card=[0]*5
    for i in range(5):
        if j_card[i]!=-99:
            if j_card[i]%13==0:
                hi_card[i]=13
            else:
                hi_card[i]=j_card[i]%13
        else:
            hi_card[i]=-99
    
    for i in range(5):
        if hi_card[i]==1:
            hi_card[i]=14
    
    for j in range(4):
        for k in range(1+j,5):
            if hi_card[j]==hi_card[k]:
                pair+=1
                hi_pair.append(hi_card[j])
            
    if pair==0:
        if joker==1:
            j_hand[9]=max(hi_card)
        else:
            j_hand[10]=max(hi_card)
            
    if pair==1:
        if joker==1:
            j_hand[7]=max(hi_pair)
        else:
            j_hand[9]=max(hi_pair)
    
    if pair==2:
        if joker==1:
            j_hand[4]=max(hi_pair)
        else:
            j_hand[8]=max(hi_pair)
    
    if pair==3:
        if joker==1:
            j_hand[3]=max(hi_pair)
        else:
            j_hand[7]=max(hi_pair)
    
    if pair==4:
        if hi_pair.count(hi_pair[0])>1:
            j_hand[4]=hi_pair[0]
        else:
            j_hand[4]=hi_pair[1]
            
    if pair==6:
        if joker==1:
            j_hand[0]=max(hi_pair)
        else:
            j_hand[3]=max(hi_pair)
            
    fl_card=[]
    for i in j_card:
        fl_card.append((i-1)//13)
    
    if joker==1:
        fl_card.sort()
        if fl_card[1]==fl_card[4]:
            j_hand[5]=max(hi_card)
    else:
        if max(fl_card)==min(fl_card):
            j_hand[5]=max(hi_card)
            
    if pair==0:
        if joker==1:
            hi_card.sort()
            if hi_card[4]-hi_card[1]==3 or hi_card[4]-hi_card[1]==4:
                j_hand[6]=max(hi_card)
            else:
                for i in range(5):
                    if hi_card[i]==14:
                        hi_card[i]=1
                hi_card.sort()
                if hi_card[4]-hi_card[1]==3 or hi_card[4]-hi_card[1]==4:
                    j_hand[6]=max(hi_card)
                        
        else:
            if max(hi_card)-min(hi_card)==4:
                j_hand[6]=max(hi_card)
            else:
                for i in range(5):
                    if hi_card[i]==14:
                        hi_card[i]=1
                if max(hi_card)-min(hi_card)==4:
                    j_hand[6]=max(hi_card)

def retry():
    global wcnt,lcnt,dcnt
    pygame.mixer.init(frequency=48000)
    pygame.mixer.music.load("./Media/Retry.wav")
    pygame.mixer.music.play(1)
    wcnt=0
    lcnt=0
    dcnt=0
    cvs.delete("im")
    button_retry.place_forget()
    poker_main()
    
def finish():
    global y
    if wcnt==3 or wcnt==2 and lcnt==1 and dcnt==2 or wcnt==2 and dcnt==3 or wcnt==1 and dcnt==4:
        y=0
        pygame.mixer.init(frequency=48000)
        pygame.mixer.music.load("./Media/congrats_win.wav")
        pygame.mixer.music.play(1)
        for i in range(22):
            button_next.place_forget()
            img1.append(tkinter.PhotoImage(file="./Media/おめでとう"+str(number[i])+".png",master=win))
        cvs.create_image(320,240,image=img1[y],tag="im")
        for i in range(20):
            cvs.update()
            time.sleep(0.25)
            cvs.delete("im")
            y=y+1
            cvs.create_image(320,240,image=img1[y],tag="im")
        cvs.update()
        time.sleep(0.25)
        cvs.delete("im")
        cvs.create_image(320,240,image=img1[y+1],tag="im")
        button_retry.place(x=400,y=350)
        
    if lcnt==3 or lcnt==2 and wcnt==1 and dcnt==2 or lcnt==2 and dcnt==3 or lcnt==1 and dcnt==4:
        y=0
        pygame.mixer.init(frequency=48000)
        pygame.mixer.music.load("./Media/lose_completely.wav")
        pygame.mixer.music.play(1)
        for i in range(8):
            button_next.place_forget()
            img2.append(tkinter.PhotoImage(file="./Media/負け"+str(number[i])+".png",master=win))
        cvs.create_image(320,240,image=img2[y],tag="im")
        for i in range(6):
            cvs.update()
            time.sleep(0.4)
            cvs.delete("im")
            y=y+1
            cvs.create_image(320,240,image=img2[y],tag="im")
        
   
        cvs.update()
        time.sleep(0.4)
        cvs.delete("im")
        cvs.create_image(320,240,image=img2[y+1],tag="im")
        button_retry.place(x=400,y=350)

def vs(m_hand,c_hand,h_str):
    global wcnt,lcnt,dcnt
    for i in range(11):
        if m_hand[i]!=0:
            cvs.create_text(100,250,text="you:"+h_str[i],font=("Helvetica",16),tag="la")
            break
    for j in range(11):
        if c_hand[j]!=0:
            cvs.create_text(100,220,text="com:"+h_str[j],font=("Helvetica",16),tag="lb")
            break
    for k in range(11):
        if m_hand[k]!=0 or c_hand[k]!=0:
            if m_hand[k]>c_hand[k]:
                cvs.create_text(500,230,text="You win!",font=("Helvetica",16),tag="lc")
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("./Media/congrats_per1.wav")
                pygame.mixer.music.play(1)
                wcnt+=1      
                break
            elif m_hand[k]<c_hand[k]:
                cvs.create_text(500,230,text="You lose...",font=("Helvetica",16),tag="lc")
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("./Media/lose_per1.wav")
                pygame.mixer.music.play(1)
                lcnt+=1
                break
            elif m_hand[k]==c_hand[k]:
                cvs.create_text(500,230,text="Draw",font=("Helvetica",16),tag="lc")
                pygame.mixer.init(frequency=48000)
                pygame.mixer.music.load("./Media/Draw.wav")
                pygame.mixer.music.play(1)
                dcnt+=1
                break
    cvs.create_text(510,250,text="win:"+str(wcnt)+" lose:"+str(lcnt)+" draw:"+str(dcnt),font=("Helvetica",16),tag="lc")

def poker_main():
    global deck,my_card,com_card,my_cardimage,com_cardimage,select_list,games,my_hand,com_hand
    button_change.place(x=250,y=230)
    button_change.lift()
    button_next.lower()
    button_select.clear()
    cvs.delete("ci","la","lb","lc")   
    deck.clear()
    my_card.clear()
    com_card.clear()
    my_cardimage.clear()
    com_cardimage.clear()
    select_list=[0]*5
    my_hand=[0]*11
    com_hand=[0]*11
    if wcnt!=0 or lcnt!=0 or dcnt!=0:
        pygame.mixer.init()
        pygame.mixer.music.load("./Media/Next Game.wav")
        pygame.mixer.music.play(1)
    
    for i in range(5):
        button_select.append(tkinter.Button(win,text=u"select"+str(i+1),width=10))
        button_select[i].bind("<Button-1>",selection)
        button_select[i].place(x=i*120+33,y=450)
    
    deal()

if __name__ == "__main__":
    win=tkinter.Tk()
    win.geometry("640x480")
    cvs=tkinter.Canvas(win,width=640,height=480)
    cvs.pack()
    cvs.create_rectangle(0,0,640,480,fill="brown")
    card_suit=["c","d","h","s"]
    card_rank=[str(i).zfill(2) for i in range(1,14)]
    card_image=["x01"]+[s+r for s in card_suit for r in card_rank]

    hand_str=['5 of a Kind','Royal Flush','Straight Flush',
              '4 of a Kind','Full House','Flush','Straight',
              '3 of a Kind','Two Pair','One Pair','High Cards']
    img=[]
    img1=[]
    img2=[]
    img3=[]
    number=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    deck=[]
    my_card=[]
    com_card=[]
    my_cardimage=[]
    com_cardimage=[]
    my_im=[]
    com_im=[]
    wcnt=0
    lcnt=0
    dcnt=0
    button_select=[]
    
    button_change=tkinter.Button(win,text=u"Change&Open",command=change,width=15)
    button_change.place(x=250,y=230)
    button_next=tkinter.Button(win,text=u"Next Game",command=poker_main,width=15)
    button_next.place(x=250,y=230)
    button_start=tkinter.Button(win,text=u"Game Start",command=start,width=15)
    button_start.place(x=250,y=230)
    button_retry=tkinter.Button(win,text=u"Retry",command=retry,width=15)
win.mainloop()
