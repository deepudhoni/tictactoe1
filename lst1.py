from tkinter import *
from tkinter import messagebox
import random

count = 0
count1 = 0
x=0
y=0
root = Tk()

frame=Frame(root)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)


def s1():
    global count
    count+=1  
    if count%2 == 0:
       btn1.configure(bg="red")
       btn1.configure(state="disabled")
       
    else:  
       btn1.configure(bg = "green")
       btn1.configure(state="disabled")
    check()
    second()
def s2():
    global count
    count+=1  
    if count%2 == 0:
       btn2.configure(bg="red")
       btn2.configure(state="disabled")
    else:
       btn2.configure(bg = "green")
       btn2.configure(state="disabled")
    check()
    second()
def s3():
    global count
    count+=1 
    if count%2 == 0:
       btn3.configure(bg="red")
       btn3.configure(state="disabled")
    else:
       btn3.configure(bg = "green")
       btn3.configure(state="disabled")
    check()
    second()
def s4():
    global count
    count+=1 
    if count%2 == 0:
       btn4.configure(bg="red")
       btn4.configure(state="disabled")
    else:
       btn4.configure(bg = "green")
       btn4.configure(state="disabled")
    check()
    second()
def s5():
    global count
    count+=1 
    if count%2 == 0:
       btn5.configure(bg="red")
       btn5.configure(state="disabled")
    else:
       btn5.configure(bg = "green")
       btn5.configure(state="disabled")
    check()
    second()
def s6():
    global count
    count+=1 
    if count%2 == 0:
       btn6.configure(bg="red")
       btn6.configure(state="disabled")
    else:
       btn6.configure(bg = "green")
       btn6.configure(state="disabled")
    check()
    second()
def s7():
    global count
    count+=1 
    if count%2 == 0:
       btn7.configure(bg="red")
       btn7.configure(state="disabled")
    else:
       btn7.configure(bg = "green")
       btn7.configure(state="disabled")
    check()
    second()
def s8():
    global count
    count+=1 
    if count%2 == 0:
       btn8.configure(bg="red")
       btn8.configure(state="disabled")
    else:
       btn8.configure(bg = "green")
       btn8.configure(state="disabled")
    check()
    second()
def s9():
    global count
    count+=1 
    if count%2 == 0:
       btn9.configure(bg="red")
       btn9.configure(state="disabled")
    else:
       btn9.configure(bg = "green")
       btn9.configure(state="disabled")
    check()
    second()




btn1 = Button(frame,command=s1)
btn1.grid(column=0, row=0, sticky=N+S+E+W)
btn2 = Button(frame,command=s2)
btn2.grid(column=1, row=0, sticky=N+S+E+W)
btn3 = Button(frame,command=s3)
btn3.grid(column=2, row=0, sticky=N+S+E+W)
btn4 = Button(frame,command=s4)
btn4.grid(column=0, row=1, sticky=N+S+E+W)
btn5 = Button(frame,command=s5,bg="red",state="disabled")
btn5.grid(column=1, row=1, sticky=N+S+E+W)
btn6 = Button(frame,command=s6)
btn6.grid(column=2, row=1, sticky=N+S+E+W)
btn7 = Button(frame,command=s7)
btn7.grid(column=0, row=2, sticky=N+S+E+W)
btn8 = Button(frame,command=s8)
btn8.grid(column=1, row=2, sticky=N+S+E+W)
btn9 = Button(frame,command=s9)
btn9.grid(column=2, row=2, sticky=N+S+E+W)

def second():
    
    global count,x,y
    
    if count == 1:
       if btn1['bg'] != "green" and btn3['bg'] != "green" and btn7['bg'] != "green" and btn9['bg'] != "green":
          if btn2['bg']=="green":
              x=1
              y=2
              random.choice([s1,s3])()
          elif btn4['bg']=="green":
               x=1
               y=4
               random.choice([s7,s1])()
          elif btn6['bg']=="green":
               x=1
               y=6
               random.choice([s3,s9])()
          elif btn8['bg']=="green":
               x=1
               y=8
               random.choice([s7,s9])()
            
       
       if btn1['bg']=="green":
          x=2
          y=1
          random.choice( [ s3,s7 ] )()
          
       elif btn3['bg']=="green":
            x=2
            y=3
            random.choice([s1,s9])()
       elif btn7['bg']=="green":
            x=2
            y=7
            random.choice([s1,s9])()
       elif btn9['bg']=="green":
            x=2
            y=9
            random.choice([s7,s3])()
    count3()
    checkwin()
def count3():
    global x,y
    
    if count==3:
       if x==1 and y==2:
          
          if btn1['bg']=="red":
             s7()
          else: s9()
          checkwin()
       if x==1 and y==4:
           if btn1['bg']=="red":
               s3()
           else: s9()
       if x==1 and y==6:
           if btn3['bg']=="red":
               s1()
           else: s7()
       if x==1 and y==8: 
          if btn7['bg']=="red":
             s1()
          else: s3()
       rule1=[ x==2 and y==1,
               x==2 and y==9
              ]
       rule2=[ x==2 and y==3,
               x==2 and y==7
              ]
       

       if any(rule1):
          if btn3['bg']=="red":
             s8()
          else: s6()
       if any(rule2):
          if btn1['bg']=="red":
             s8()
          else: s6()
               
     
        
          
    

    
def checkwin():
    if count==5:
        if btn3['bg']== "red" and btn7['bg'] != "green":
           s7() 
        if btn7['bg']== "red" and btn3['bg'] != "green":
           s3()
        if btn1['bg']== "red" and btn9['bg'] != "green":
           s9() 
        if btn9['bg']== "red" and btn1['bg'] != "green":
          s1()
        if btn1['bg']== "red" and btn2['bg'] == "red":
            s3()
        if btn1['bg']== "red" and btn3['bg'] == "red":
            s2()
        if btn2['bg']== "red" and btn3['bg'] == "red":
           s1()
        if btn4['bg']== "red" and btn5['bg'] == "red":
            s6()
        if btn5['bg']== "red" and btn6['bg'] == "red":
            s4()
        if btn4['bg']== "red" and btn6['bg'] == "red":
            s5()
        if btn7['bg']== "red" and btn8['bg'] == "red":
            s9()
        if btn8['bg']== "red" and btn9['bg'] == "red":
            s7()
        if btn9['bg']== "red" and btn7['bg'] == "red":
            s8()
        if btn1['bg']== "red" and btn4['bg'] == "red":
            s7()
        if btn4['bg']== "red" and btn7['bg'] == "red":
            s1()
        if btn1['bg']== "red" and btn7['bg'] == "red":
            s4()
        if btn2['bg']== "red" and btn5['bg'] == "red":
            s8()
        if btn5['bg']== "red" and btn8['bg'] == "red":
            s2()
        if btn8['bg']== "red" and btn5['bg'] == "red":
            s2()
        if btn6['bg']== "red" and btn9['bg'] == "red":
            s3()
        if btn3['bg']== "red" and btn9['bg'] == "red":
            s6()
        if btn6['bg']== "red" and btn3['bg'] == "red":
            s9()     


def check():
    global count1
    count1 += 1
    rules =[ btn1['bg']=="red" and btn2['bg']=="red" and btn3['bg']=="red",
             btn4['bg']=="red" and btn5['bg']=="red" and btn6['bg']=="red",
             btn7['bg']=="red" and btn8['bg']=="red" and btn9['bg']=="red",
             btn7['bg']=="red" and btn4['bg']=="red" and btn1['bg']=="red",
             btn8['bg']=="red" and btn5['bg']=="red" and btn2['bg']=="red",
             btn9['bg']=="red" and btn6['bg']=="red" and btn3['bg']=="red",
             btn7['bg']=="red" and btn5['bg']=="red" and btn3['bg']=="red",
             btn1['bg']=="red" and btn5['bg']=="red" and btn9['bg']=="red"
             ]
    if any(rules):
        messagebox.showinfo("red won the game")
        reset()

    rule = [ btn1['bg']=="green" and btn2['bg']=="green" and btn3['bg']=="green",
             btn4['bg']=="green" and btn5['bg']=="green" and btn6['bg']=="green",
             btn7['bg']=="green" and btn8['bg']=="green" and btn9['bg']=="green",
             btn7['bg']=="green" and btn4['bg']=="green" and btn1['bg']=="green",
             btn8['bg']=="green" and btn5['bg']=="green" and btn2['bg']=="green",
             btn9['bg']=="green" and btn6['bg']=="green" and btn3['bg']=="green",
             btn7['bg']=="green" and btn5['bg']=="green" and btn3['bg']=="green",
             btn1['bg']=="green" and btn5['bg']=="green" and btn9['bg']=="green"
             ]
    if any(rule):
        messagebox.showinfo("green won the game")
        reset()
    else:
        if count1 == 8:
           
           messagebox.showwarning("match drawn")
           reset()
        
def reset():
    btn1.configure(state="normal",bg="white")
    btn2.configure(state="normal",bg="white")
    btn3.configure(state="normal",bg="white")
    btn4.configure(state="normal",bg="white")
    btn5.configure(state="normal",bg="red")
    btn6.configure(state="normal",bg="white")
    btn7.configure(state="normal",bg="white")
    btn8.configure(state="normal",bg="white")
    btn9.configure(state="normal",bg="white")
    global count1,count
    count = 0
    count1 = 0



for x in range(10):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
  Grid.rowconfigure(frame, y, weight=1)

    


root.mainloop()
