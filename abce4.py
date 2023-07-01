from tkinter import *
import random
from tkinter.simpledialog import *
import datetime

def button(x=0,y=0,siz=0,text='',sid=0,id=0,cnvs=None,function=None,scrn=None):
    global screen
    if sid == id:
        cnvs.create_rectangle(x-2, y, siz+x+2,
                         siz+y,
                         fill="white")
        cnvs.create_text(x+round(siz*0.5),y+round(siz*0.5),fill="black",font=f"Arial {round(siz*0.2)}",
                            text=text)
        x2 = root.winfo_pointerx() - root.winfo_rootx()
        y2 = root.winfo_pointery() - root.winfo_rooty()
        clicked = ((x2 > x and x2 < x + siz) and (y2 > y and y2 < y + siz)) and left_click
        if clicked and function:
            exec(function)
        elif clicked and scrn != None:
            print(f'Setting screen to {scrn}')
            screen = scrn
        if ((x2 > x and x2 < x + siz) and (y2 > y and y2 < y + siz)):
            if customcursor:
                cnvs.config(cursor="@Cursor_15.cur")
        return clicked
def text(x,y,cnvs,text,color="#1C1C1C"):
    cnvs.create_text(x,y,fill=color,
                            text=text)
def change():
    global clicks
    clicks += 1
def change2():
    global times
    times += 1
times = 0
clicks = 0
screen = 0
left_click = False
def click_start(event):
    global left_click
    left_click = True

def click_stop(event):
    global left_click
    left_click = False
def thing():
    global kext
    kext=random.choice(['yes','no'])
root = Tk()
root.title('pywin98')
root.resizable(False, False)
root.bind("<Button-1>", click_start)
root.bind("<B1-ButtonRelease>", click_stop)
C = Canvas(bg='darkcyan', highlightthickness=0,
           borderwidth=0,height=300,width=400)
customcursor = True # Disable if you dislike windows 95 cursor
kext = ''
def changebg(clr):
    C.config(bg=clr)
def update():
    print('Updating screen.')
    C.delete('all')
    if customcursor:
        C.config(cursor="@arrow.cur")
    # Desktop
    button(10,10,30,'Shutdown',cnvs=C,scrn=5, id=0,sid=screen)
    button(10,45,30,'Explorer',cnvs=C,scrn=1, id=0,sid=screen)
    button(10,80,30,'Helloworld',cnvs=C,scrn=2, id=0,sid=screen)
    button(10,115,30,'Clicker',cnvs=C,scrn=3, id=0,sid=screen)
    button(10,150,30,'Catch me',cnvs=C,scrn=4, id=0,sid=screen)
    button(10,185,30,'BSOD',cnvs=C,scrn=6, id=0,sid=screen)
    button(10,220,30,'Clock',cnvs=C,scrn=7, id=0,sid=screen)
    button(50,10,30,'Magic ball',cnvs=C,scrn=8, id=0,sid=screen)
    button(50,45,30,'Background',cnvs=C,scrn=9, id=0,sid=screen)
    # add other background to other screens
    if screen > 0:
        C.create_rectangle(0, 0, 400,
                         300,
                         fill="lightgrey")
    # Other screens
    if screen == 9:
        button(0,0,50,cnvs=C,text='lightgrey',function="changebg('lightgrey')")
        button(50,0,50,cnvs=C,text='grey',function="changebg('grey')")
        button(100,0,50,cnvs=C,text='darkcyan',function="changebg('darkcyan')")
        button(150,0,50,cnvs=C,text='red',function="changebg('red')")
        button(200,0,50,cnvs=C,text='blue',function="changebg('blue')")
        button(250,0,50,cnvs=C,text='green',function="changebg('green')")
        button(300,0,50,cnvs=C,text='darkblue',function="changebg('darkblue')")
        button(300,0,50,cnvs=C,text='lightcyan',function="changebg('lightcyan')")
        button(350,0,50,cnvs=C,text='cyan',function="changebg('cyan')")
        button(400,0,50,cnvs=C,text='darkred',function="changebg('darkred')")
    elif screen == 1:
        text(random.randint(-1,1)+200,random.randint(-1,1)+150,C,"Sorry but i am lazy to make explorer")
    elif screen == 5:
        text(random.randint(-10,10)+200,random.randint(-10,10)+150,C,"Dont be lazy, shutdown it myself")
    elif screen == 2:
        text(200,150,C,"Hello, World! And what did you except here?")
    elif screen == 3:
        text(200,130,C,str(clicks))
        button(175,150,50,cnvs=C,text="click me",function="change(); print(clicks)")
    elif screen == 4:
        text(50,50,C,"Catched times: "+str(times))
        button(random.randrange(0,150,40)+60,random.randrange(0,150,40)+60,40,cnvs=C,text="Catch me!!!!",function="change2(); print(times)")
    elif screen == 7:
        text(200,150,C,datetime.datetime.now().strftime("%I:%M %p"))
    elif screen == 8:
        button(200-25,100,50,cnvs=C,text="Ask",function="thing()")
        text(200,200,C,kext)
    C.create_rectangle(0, 300-30, 400,
                         300,
                         fill="white")
    button(2,300-30,30,'Desktop',cnvs=C,scrn=0)
    text(400-40,300-15,C,datetime.datetime.now().strftime("%I:%M %p"))
    if screen == 6:
        C.create_rectangle(0, 0, 400,
                         300,
                         fill="blue")
        text(200,100,C,"Your pc ran into problem","white")
        text(200,150,C,"Please restart it","white")
        text(200,200,C,"Or litterally press bottom left corner","white")
    root.after(100,update)

update()
C.pack()
mainloop()
