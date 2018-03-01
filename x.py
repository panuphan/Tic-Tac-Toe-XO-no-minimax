from tkinter import *
from tkinter.font import Font
import random

turn = 'X'
Bot = False
Step = []
def bot(button,x,y):
    global Step
    if Step == []:
        for y in range(3):
                 print('at ',1,y,'have >',button[1,y]['text'])
                 if button[1,y]['text'] ==  'X':
                    r=random.randint(0,1)
                    if r==1:
                        r+=1
                    button[r,y]['text'] =  'O'
                    print('at ',r,y,'have >',button[r,y]['text'])
                    Step.append(True)
                    return
                 elif button[y,1]['text'] ==  'X':
                    print('at ',y,1,'have >',button[y,1]['text'])
                    r=random.randint(0,1)
                    if r==1:
                        r+=1
                    button[y,r]['text'] =  'O'
                    print('at ',y,r,'have >',button[y,r]['text'])
                    return
                
        if button[1,1]['text'] == ' ':
             button[1,1]['text'] = 'O'

        else:
            r1=random.randint(0,1)
            if r1==1:
                r1+=1
            r2=random.randint(0,1)
            if r2==1:
                r2+=1
            button[r1,r2]['text'] ='O'

        Step.append(True)


    elif not check(button):
        c = check(button,True)
        if c :
            print("C>>",c)
            for x,y in c:
                if button[x,y]['text'] == ' ':
                    button[x,y]['text'] ='O'
                    return

        else:
            temp = False
            for x in range(0,3,2):
                for y in range(0,3,2):
                    if button[x,y]['text'] == ' ':
                        temp = True
                        break
                                   
            while(temp):
                        r1=random.randint(0,1)
                        if r1==1:
                            r1+=1
                        r2=random.randint(0,1)
                        if r2==1:
                            r2+=1
                        if button[r1,r2]['text'] == ' ':
                            button[r1,r2]['text'] ='O'
                            print('random >',r1,r2)
                            return
            temp = False
            for x,y in button:
                if button[x,y]['text'] == ' ':
                        temp = True
                        break
                                   
            while(temp):
                        r1=random.randint(0,2)
                        r2=random.randint(0,2)
                        if button[r1,r2]['text'] == ' ':
                            button[r1,r2]['text'] ='O'
                            print('random >',r1,r2)
                            return
            
                        


def swap(x):
    if x != 1 :
        x+=2
        if x>2:
            x=0
    return x


def check_plus(button,symbol,Botmode):
    
    for r in range(4):
        win = []
        for y in range(3):
            if r < 2 :
                win = []
                for x in range(3):

                    if r== 0 and button[x,y]['text'] == symbol:
                        win.append((x,y))
                    if r==1  and button[y,x]['text'] == symbol:
                        win.append((y,x))

            else :
                if r==2 and button[y,y]['text'] == symbol:
                    win.append((y,y))
                if r==3 and button[3-1-y,y]['text'] == symbol:
                    win.append((3-1-y,y))
   
            if Botmode == False:
                if len(win) == 3 :
                    return win
                
            elif Botmode == True:
                
                if len(win) > 1 :
                    temp = 0
                    for i in range(2):
                            if r < 2:
                                temp += (win[i][r])
                            else:
                                temp += ( win[i][0]*3+ win[i][1] )
                    N = 3-temp
                    if r==0 and (button[N,win[0][1]]['text'] == ' '):
                        return [(N,win[0][1])]
                    if r==1 and (button[win[0][0],N]['text'] == ' '):
                        return [(win[0][0],N)]
                    N = 12-temp
                    xt = N//3
                    yt = N - (3*xt)
                    if r==2 and (button[xt,yt]['text'] == ' '):
                        return [(xt,yt)]
                    if r==3 and (button[xt,yt]['text'] == ' '):
                        return [(xt,yt)]
                    
    
    



def check(button,Botmode = False):
        
        
    # horizontal # vertical
    #O เหนือ X คือ จะเน้น ทำคะแนน ข้อเสีย เมื่อเวลา คน ชนะ แต่ตาต่อไปคอมก็จะชนะเช่นกัน คอมจะทำงานแล้วบอกว่ามันอ่ะชนะ
    #
    c = check_plus(button,'O',Botmode)
    if c:
        return c
    c = check_plus(button,'X',Botmode)
    if c:
        print('Cx>>',c)
        return c
                

    return None

    

    

def update(button,x,y):
    global turn
    global Bot
    print(x,y)

    if Bot == False :
        if button[x,y]["text"] == ' ' and button[x,y]['state'] == 'normal':
            button[x,y]["text"] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    elif Bot == True:
        if turn == 'X' and button[x,y]["text"] == ' ' and button[x,y]['state'] == 'normal':
            button[x,y]["text"] = 'X'
            turn = 'O'
        if turn == 'O':
            bot(button,x,y)
            turn = 'X'

    win = check(button)
    if win:
        for x,y in win:
            button[x,y]['disabledforeground'] = 'green'
        for x,y in button:
            button[x,y]['state'] = 'disabled'
        
            
        
    

    
def reset(button):
    global turn
    global Bot
    global Step
    for x,y in button:
            button[x,y]["text"] = ' '
            button[x,y]['state'] = 'normal'
            button[x,y]['disabledforeground'] = 'black'
    turn = 'X'
    Step = []
    Bot = False
            
def BotMode(button):
    global Bot
    reset(button)
    Bot= True
    
    
            

root = Tk()
root.title("Tic Tac Toe XO")
buttons = {}
bt = {}

for x in range(3):
    for y in range(3):
        click = lambda x=x,y=y :update(bt,x,y)
        button = Button(root,command=click,text = ' ',font= Font(size=20), width=6, height=2)
        button.grid(row=x, column=y)
        bt[x,y]= button
        
click = lambda : reset(bt)
button = Button(root, text='Reset',font= Font(size=10), command=click)
button.grid(columnspan=3, sticky="WE")

click = lambda : BotMode(bt)
button = Button(root, text='BoT',font= Font(size=10), command=click)
button.grid(columnspan=3, sticky="WE")



root.resizable(width=False, height=False)
root.mainloop()
#N = y * 3 + x
#x = N//3
#y = N -(3*x)
