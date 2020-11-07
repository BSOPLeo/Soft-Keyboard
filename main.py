import tkinter as tk
import random
import pyautogui as p
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import sys
root = tk.Tk()
root.geometry("1500x1100")
root.title("软键盘")
root.wm_attributes('-topmost',1)
root.resizable(width=False,height=False)
li = []
ten = False
def change_ten():
    global ten
    if ten == True:
        ten = False
    else:
        ten == True
def p2(letter,x,y):
    letter.place(x=x,y=y,width=100,height=100)
def camera():
    capture = cv2.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        frame = cv2.flip(frame,1)
        cv2.imshow("Camera(Press 'Q' to exit)", frame)
        key = cv2.waitKey(50)
        if key  == ord('q'):
            break
    cv2.destroyAllWindows()
def co(c):
    global a
    a = c
    d = random.choice(li)
    for i in li:
        i["bg"] = a
    if d["bg"] == "white":
        for i in li:
            i["fg"] = "black"
    elif d["bg"] == "black":
        for i in li:
            i["fg"] = "white"
    else:
        pass
def co2(c):
    global b
    b = c
    d = random.choice(li)
    for i in li:
        i["fg"] = b
    if d["bg"] == "white" and d["fg"] == "white":
        for t in li:
            t["fg"] = "black"
    elif d["bg"] == "black" and d["fg"] == "black":
        for x in li:
            x["fg"] = "white"
def pr(letter):
    p.hotkey("alt","tab")
    sleep(0.2)
    p.press(letter)
def hot(a,b):
    p.hotkey("alt","tab")
    sleep(0.2)
    p.hotkey(a,b)
def hot2(a,b,c):
    p.hotkey(a,b,c)
def pr2(letter):
    p.hotkey("alt","tab")
    for i in range(10):
        p.press(letter)
def together(letter):
    if ten == False:
        pr(letter)
    else:
        pr2(letter)
def do(letter):
    l = tk.Button(root,text=letter,command=lambda:together(letter))
    return l
def show(pic,title):
    picture = mpimg.imread(pic)
    plt.imshow(picture)
    plt.title(title)
    plt.axis("off")
    plt.show()
tab = tk.Button(root,text="TAB",command=lambda:together("tab"))
tab.place(x=0,y=300,width=200,height=100)
li.append(tab)
caps = tk.Button(root,text="CAPS LOCK",command=lambda:p.press("capslock"))
caps.place(x=0,y=400,width=250,height=100)
li.append(caps)
enter = tk.Button(root,text="ENTER",command=lambda:together("enter"))
enter.place(x=1350,y=400,width=150,height=100)
li.append(enter)
back = tk.Button(root,text="BACKSPACE",command=lambda:together("backspace"))
back.place(x=1300,y=100,width=200,height=100)
li.append(back)
back2 = tk.Button(root,text="BACKSPACE",command=lambda:together("backspace"))
back2.place(x=1300,y=200,width=200,height=100)
li.append(back2)
shift1 = tk.Button(root,text="SHIFT",command=lambda:p.press("shift"))
shift1.place(x=0,y=500,width=200,height=100)
li.append(shift1)
shift2 = tk.Button(root,text="SHIFT",command=lambda:p.press("shift"))
shift2.place(x=1300,y=500,width=200,height=100)
li.append(shift2)
PRTSC = tk.Button(root,text="PRTSC",command=lambda:p.press("PRTSC"))
PRTSC.place(x=1300,y=0,width=100,height=100)
li.append(PRTSC)
delete = tk.Button(root,text="DELETE",command=lambda:together("delete"))
delete.place(x=1400,y=0,width=100,height=100)
li.append(delete)
space = tk.Button(root,text="SPACE",command=lambda:together("space"))
space.place(x=400,y=600,width=600,height=100)
li.append(space)
up = tk.Button(root,text="↑",command=lambda:together("up"))
up.place(x=1200,y=500,width=100,height=100)
li.append(up)
left = tk.Button(root,text="←",command=lambda:together("left"))
left.place(x=1000,y=600,width=200,height=100)
li.append(left)
down = tk.Button(root,text="↓",command=lambda:together("down"))
down.place(x=1200,y=600,width=100,height=100)
li.append(down)
right = tk.Button(root,text="→",command=lambda:together("right"))
right.place(x=1300,y=600,width=200,height=100)
li.append(right)
minus = ['ESC','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']
v = 0
for i in minus:
    letter = do(i)
    p2(letter,(100*v),0)
    v += 1
    li.append(letter)
zero = ['`','1','2','3','4','5','6','7','8','9','0','-','=',]
w = 0
for i in zero:
    letter = do(i)
    p2(letter,(100*w),100)
    w += 1
    li.append(letter)
middle = ['~','!','@','#','$','%','^','&','*','(',')','_','+']
a = 0
for i in middle:
    letter = do(i)
    p2(letter,(100*a),200)
    a += 1
    li.append(letter)
first = ['Q','W','E','R','T','Y','U','I','O','P',"[","]",'|']
x = 1
for i in first:
    letter = do(i)
    p2(letter,(100*x+100),300)
    x += 1
    li.append(letter)
second = ['A','S','D','F','G','H','J','K','L',';',"'"]
y = 1
for i in second:
    letter = do(i)
    p2(letter,(100*y+150),400)
    y += 1
    li.append(letter)
third = ['Z','X','C','V','B','N','M',',','.','?']
z = 1
for i in third:
    letter = do(i)
    p2(letter,(100*z+100),500)
    z += 1
    li.append(letter)
fourth = ['CTRL','FN','WIN','ALT']
b = 0
for i in fourth:
    letter = do(i)
    p2(letter,(100*b),600)
    b += 1
    li.append(letter)
others = ['{','}','\\',':','''"''','<','>','/']
c = 0
for i in others:
    letter = do(i)
    p2(letter,(100*c),700)
    c += 1
    li.append(letter)
copy = tk.Button(root,text="COPY",command=lambda:hot("ctrl","c"))
copy.place(x=800,y=700,width=100,height=100)
li.append(copy)
paste = tk.Button(root,text="PASTE",command=lambda:hot("ctrl","v"))
paste.place(x=900,y=700,width=100,height=100)
li.append(paste)
desktop = tk.Button(root,text="DESKTOP",command=lambda:p.hotkey("win","d"))
desktop.place(x=1000,y=700,width=100,height=100)
li.append(desktop)
left2 = tk.Button(root,text="LEFT",command=lambda:hot("shift","left"))
left2.place(x=1100,y=700,width=100,height=100)
li.append(left2)
right2 = tk.Button(root,text="RIGHT",command=lambda:hot("shift","right"))
right2.place(x=1200,y=700,width=100,height=100)
li.append(right2)
down2 = tk.Button(root,text="DOWN",command=lambda:hot("shift","down"))
down2.place(x=1300,y=700,width=100,height=100)
li.append(down2)
up2 = tk.Button(root,text="UP",command=lambda:hot("shift","up"))
up2.place(x=1400,y=700,width=100,height=100)
li.append(up2)
turn = tk.Button(root,text="BACK",command=lambda:hot("ctrl","z"))
turn.place(x=0,y=800,width=100,height=100)
li.append(turn)
al = tk.Button(root,text="ALL",command=lambda:hot("ctrl","a"))
al.place(x=100,y=800,width=100,height=100)
li.append(al)
emoji = tk.Button(root,text="EMOJI",command=lambda:hot("win","."))
emoji.place(x=200,y=800,width=100,height=100)
li.append(emoji)
word = tk.Button(root,text="WORD",command=lambda:hot2("ctrl","alt","w"))
word.place(x=300,y=800,width=100,height=100)
li.append(word)
chrome = tk.Button(root,text="CHROME",command=lambda:hot2("ctrl","alt","g"))
chrome.place(x=400,y=800,width=100,height=100)
li.append(chrome)
ie = tk.Button(root,text="IE",command=lambda:hot2("ctrl","alt","i"))
ie.place(x=500,y=800,width=100,height=100)
li.append(ie)
clip = tk.Button(root,text="CLIPBOARD",command=lambda:hot("win","v"))
clip.place(x=600,y=800,width=200,height=100)
li.append(clip)
file = tk.Button(root,text="FILE EXPLORER",command=lambda:hot("win","e"))
file.place(x=800,y=800,width=200,height=100)
li.append(file)
dance = tk.Button(root,text="DANCE",command=lambda:show("D:\Leo Yu\各种图片\搞笑\小人跳舞1.jpg","Dance"))
dance.place(x=1000,y=800,width=100,height=100)
li.append(dance)
cam = tk.Button(root,text="CAMERA",command=lambda:camera())
cam.place(x=1100,y=800,width=100,height=100)
li.append(cam)
ten_b = tk.Button(root,text="TEN",command=lambda:change_ten())
ten_b.place(x=1200,y=800,width=100,height=100)
li.append(ten_b)
a = "white"
b = "black"
white = tk.Button(root,text="WHITE",bg="white",command=lambda:co("white"))
white.place(x=0,y=900,width=250,height=100)
blue = tk.Button(root,text="BLUE",bg="deep sky blue",command=lambda:co("deep sky blue"))
blue.place(x=250,y=900,width=250,height=100)
red = tk.Button(root,text="RED",bg="coral",command=lambda:co("coral"))
red.place(x=500,y=900,width=250,height=100)
green = tk.Button(root,text="GREEN",bg="lawn green",command=lambda:co("lawn green"))
green.place(x=750,y=900,width=250,height=100)
purple = tk.Button(root,text="PURPLE",bg="plum",command=lambda:co("plum"))
purple.place(x=1000,y=900,width=250,height=100)
black = tk.Button(root,text="BLACK",bg="black",fg="white",command=lambda:co("black"))
black.place(x=1250,y=900,width=250,height=100)
white = tk.Button(root,text="WHITE",bg="white",command=lambda:co2("white"))
white.place(x=0,y=1000,width=750,height=100)
black = tk.Button(root,text="BLACK",bg="black",fg="white",command=lambda:co2("black"))
black.place(x=750,y=1000,width=750,height=100)
for i in li:
    i["bg"] = a
    i["fg"] = b
tk.mainloop()
