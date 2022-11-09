
#Ariana Mondiri
#11/7/2022
#Try to reproduce the game TowerOfHanoi from scratch

from tkinter import *
import tkinter as tk
from tkinter import ttk


root = Tk()
root.title("Game")
root.geometry("1300x700") 

mycanvas = Canvas(root, width=1400, height=900, bg="old lace")
mycanvas.pack(pady=20)


#set up 
mycanvas.create_rectangle(210,550,490,545, fill = "black")
mycanvas.create_rectangle(347.5,300,352.5,545, fill = "black")

mycanvas.create_rectangle(535,550,815,545,fill = "black")
mycanvas.create_rectangle(672.5,300,677.5,545, fill = "black")

mycanvas.create_rectangle(860,550,1140,545, fill = "black")
mycanvas.create_rectangle(997.5,300,1002.5,545, fill = "black")

mycanvas.create_line(180,0,180,600, fill="black")


rec3 = mycanvas.create_rectangle(290, 545, 410, 515, fill = "dark goldenrod")
rec2 = mycanvas.create_rectangle(310, 515, 390, 485, fill = "dark goldenrod")
rec1 = mycanvas.create_rectangle(330, 485, 370, 455, fill = "dark goldenrod")

level = 1
win_already = "no"
text_win = "no"


victory = Label(mycanvas, text=" ", bg ="old lace", fg = "black")
victory.config(font=("Helvetica bold",20))
victory.place(x=400,y=250)

title= Label(mycanvas, text="Tower of Hanoi", bg ="old lace", fg = "black")
title.config(font=("Helvetica bold",20))
title.place(x=560,y=50)

level_played = Label(mycanvas, text="level: " + str(level), bg ="old lace", fg ="black")
level_played.config(font=("Helvetica bold",15))
level_played.place(x=630,y=83)

movement = 0
num_move = Label(mycanvas, text="Number of moves: " + str(movement), bg="old lace", fg = "black")
num_move.config(font=("Helvetica bold",15))
num_move.place(x=560,y=110)


min_move = Label(mycanvas, text="Minimum moves: 7 ", bg= "old lace", fg = "black")
min_move.config(font=("Helvetica bold",15))
min_move.place(x=565,y=135)

select_level = Label(mycanvas, text="Levels", bg= "old lace", fg = "black")
select_level.config(font=("Helvetica bold",30))
select_level.place(x=35,y=100)


#create the initial stacks
left_stack = []
left_stack.append("3")
left_stack.append("2")
left_stack.append("1")

middle_stack = []
right_stack = []

stacks_level = "no"
delete = "no"

def clear_stacks():
    right_stack.clear()
    middle_stack.clear()
    left_stack.clear()
    
def append_function(level):
    
    if level == 1:
        left_stack.append("3")
        left_stack.append("2")
        left_stack.append("1")
        
    if level == 2:
        left_stack.append("4")
        left_stack.append("3")
        left_stack.append("2")
        left_stack.append("1")

    if level == 3:
        left_stack.append("5")
        left_stack.append("4")
        left_stack.append("3")
        left_stack.append("2")
        left_stack.append("1")
   
    if level == 4:
        left_stack.append("6")
        left_stack.append("5")
        left_stack.append("4")
        left_stack.append("3")
        left_stack.append("2")
        left_stack.append("1")

def stacks_level4():
    global level, rec1, rec2, rec3, rec4, rec5, rec6, win_already, delete, text_win, victory

    win_already = "no"
    delet= "yes"

    if text_win == "yes":
        victory.config(text = " ")
        text_win = "no"
    
    num_blocks = len(left_stack) + len(middle_stack) + len(right_stack)
    
    if num_blocks == 3:
        mycanvas.delete(rec1, rec2, rec3)
    if num_blocks == 4:
        mycanvas.delete(rec1, rec2, rec3, rec4)
    if num_blocks == 5:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5)
    if num_blocks == 6:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5, rec6)
        
    rec6 = mycanvas.create_rectangle(230, 545, 470, 515, fill = "dark goldenrod")   
    rec5 = mycanvas.create_rectangle(250, 515, 450, 485, fill = "dark goldenrod")
    rec4 = mycanvas.create_rectangle(270, 485, 430, 455, fill = "dark goldenrod")
    rec3 = mycanvas.create_rectangle(290, 455, 410, 425, fill = "dark goldenrod")
    rec2 = mycanvas.create_rectangle(310, 425, 390, 395, fill = "dark goldenrod")
    rec1 = mycanvas.create_rectangle(330, 395, 370, 365, fill = "dark goldenrod")
    
    level = 4
    level_played.config(text="level: 4")
    min_move.config(text="Minimum  moves: 63")
    victory.config(text="    ")
    num_move.config(text = "               moves: 0")
    clear_stacks()
    append_function(4)
    
def stacks_level3():
    global rec1, rec2, rec3, rec4, rec5, win_already, delete, text_win, victory
    

    win_already = "no"
    delete = "yes"
    
    if text_win == "yes":
        victory.config(text="")
        text_win = "no"
    
    
    num_blocks = len(left_stack) + len(middle_stack) + len(right_stack)
    
    if num_blocks == 3:
        mycanvas.delete(rec1, rec2, rec3)
    if num_blocks == 4:
        mycanvas.delete(rec1, rec2, rec3, rec4)
    if num_blocks == 5:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5)
    if num_blocks == 6:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5, rec6)
        
    rec5 = mycanvas.create_rectangle(250, 545, 450, 515, fill = "dark goldenrod")
    rec4 = mycanvas.create_rectangle(270, 515, 430, 485, fill = "dark goldenrod")
    rec3 = mycanvas.create_rectangle(290, 485, 410, 455, fill = "dark goldenrod")
    rec2 = mycanvas.create_rectangle(310, 455, 390, 425, fill = "dark goldenrod")
    rec1 = mycanvas.create_rectangle(330, 425, 370, 395, fill = "dark goldenrod")
    level = 3
    level_played.config(text="level: 3")
    min_move.config(text="Minimum  moves: 31")
    victory.config(text="    ")
    num_move.config(text = "            moves: 0")
    clear_stacks()
    append_function(3)
    stacks_level = "yes"

def stacks_level2():
    global level, stacks_level, rec1, rec2, rec3, rec4, win_already, delete#e, text_win, victory

    win_already = "no"
    delete = "yes"

    num_blocks = len(left_stack) + len(middle_stack) + len(right_stack)
    if num_blocks == 3:
        mycanvas.delete(rec1, rec2, rec3)
    if num_blocks == 4:
        mycanvas.delete(rec1, rec2, rec3, rec4)
    if num_blocks == 5:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5)
    if num_blocks == 6:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5, rec6)
        
    rec4 = mycanvas.create_rectangle(270, 545, 430, 515, fill = "dark goldenrod")
    rec3 = mycanvas.create_rectangle(290, 515, 410, 485, fill = "dark goldenrod")
    rec2 = mycanvas.create_rectangle(310, 485, 390, 455, fill = "dark goldenrod")
    rec1 = mycanvas.create_rectangle(330, 455, 370, 425, fill = "dark goldenrod")
    
    level = 2
    level_played.config(text="level: 2")
    min_move.config(text="Minimum  moves: 15")
    victory.config(text="    ")
    num_move.config(text = "            moves: 0")
    clear_stacks()
    append_function(2)


def stacks_level1():
    global rec1, rec2, rec3, level, win_already, delete, victory

    win_already = "no"
    delete = "yes"
    
    num_blocks = len(left_stack) + len(middle_stack) + len(right_stack)
    
    if num_blocks == 3:
        mycanvas.delete(rec1, rec2, rec3)
    if num_blocks == 4:
        mycanvas.delete(rec1, rec2, rec3, rec4)
    if num_blocks == 5:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5)
    if num_blocks == 6:
        mycanvas.delete(rec1, rec2, rec3, rec4, rec5, rec6)
    

    rec3 = mycanvas.create_rectangle(290, 545, 410, 515, fill = "dark goldenrod")
    rec2 = mycanvas.create_rectangle(310, 515, 390, 485, fill = "dark goldenrod")
    rec1 = mycanvas.create_rectangle(330, 485, 370, 455, fill = "dark goldenrod")

    level = 1
    level_played.config(text="level: 1")
    min_move.config(text="Minimum  moves: 7")
    victory.config(text="    ")
    num_move.config(text = "            moves: 0")
    clear_stacks()
    append_function(1)
    
level_1= Button(mycanvas, text ="level 1", bg='old lace',width= 20, height=2, command= stacks_level1)
level_2= Button(mycanvas, text ="level 2", bg='old lace',width= 20, height=2, command= stacks_level2)
level_3= Button(mycanvas, text ="level 3", bg='old lace',width= 20, height=2, command= stacks_level3)
level_4= Button(mycanvas, text ="level 4", bg='old lace',width= 20, height=2, command= stacks_level4)

level_1.place(x= 15, y=180)
level_2.place(x= 15, y=240)
level_3.place(x= 15, y=300)
level_4.place(x= 15, y=360)


def update_stack(event, add, state, x0):
    global movement
    
    if unchanged == "no":
        movement += 1
        num_move.config(text='Number of moves:' + str(movement))
        if x0 <=535:
            left_stack.pop()
        if 535 < x0 < 815:
            middle_stack.pop()
        if x0 >= 860:
            right_stack.pop()
        if event.x < 480:
            left_stack.append(add)
        if 480 < event.x < 950:
            middle_stack.append(add)
        if 950 < event.x:
            right_stack.append(add)

    win()
    

def win():
    global win_already, victory
    if level == 1:
        if len(right_stack) == 3:
            num_move.config(text = "You won! moves: " + str(movement))
            win_already = "yes"
    if level == 2:
        if len(right_stack) == 4:
            num_move.config(text = "You won! moves: " + str(movement))
            win_already= "yes"
    if level == 3:
        if len(right_stack) == 5:
            num_move.config(text = "You won! moves: " + str(movement))
            win_already= "yes"
    if level == 4:
        if len(right_stack) == 6:
            num_move.config(text = "You won! moves: " + str(movement))
            win_already = "yes"
    if win_already == "yes":
        victory.config(text = "You won! To keep playing please select a level " )
        victory.place(x=400,y=250)
       

         


#to identify next move
def nextmove(event):
    global stacks_level, stacks_level_release

    if 0 < event.x < 140:
        stacks_level_release = "no"
    else:
        stacks_level_release = "yes"
        win()
        if win_already == "yes":
            pass
        else:
            print("activated")
            if 230< event.x<= 535 and 365< event.y <545:
                if left_stack[-1] == "1":
                    coordinate_stack = mycanvas.coords(rec1)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec1, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))     
                if left_stack[-1] == "2":
                    coordinate_stack = mycanvas.coords(rec2)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec2, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))  
                if left_stack[-1] == "3":
                    coordinate_stack = mycanvas.coords(rec3)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec3, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if left_stack[-1] == "4":
                    coordinate_stack = mycanvas.coords(rec4)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec4, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if left_stack[-1] == "5":
                    coordinate_stack = mycanvas.coords(rec5)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec5, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))   
                if left_stack[-1] == "6":
                    coordinate_stack = mycanvas.coords(rec6)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec6, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
          
            if 555 < event.x < 795 and 365< event.y <545:
                if middle_stack[-1] == "1":
                    coordinate_stack = mycanvas.coords(rec1)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec1, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if middle_stack[-1] == "2":
                    coordinate_stack = mycanvas.coords(rec2)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec2, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if middle_stack[-1] == "3":
                    coordinate_stack = mycanvas.coords(rec3)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec3, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if middle_stack[-1] == "4":
                    coordinate_stack = mycanvas.coords(rec4)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec4, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if middle_stack[-1] == "5":
                    coordinate_stack = mycanvas.coords(rec5)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec5, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if middle_stack[-1] == "6":
                    coordinate_stack = mycanvas.coords(rec6)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec6, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
        
            if 880< event.x < 1120 and 365< event.y <545:
                if right_stack[-1] == "1":
                    coordinate_stack = mycanvas.coords(rec1)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec1, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if right_stack[-1] == "2":
                    coordinate_stack = mycanvas.coords(rec2)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec2, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if right_stack[-1] == "3":
                    coordinate_stack = mycanvas.coords(rec3)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec3, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if right_stack[-1] == "4":
                    coordinate_stack = mycanvas.coords(rec4)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec4, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if right_stack[-1] == "5":
                    coordinate_stack = mycanvas.coords(rec5)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec5, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))
                if right_stack[-1] == "6":
                    coordinate_stack = mycanvas.coords(rec6)
                    x0_stack, x_stack, y0_stack, y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
                    root.bind('<B1-Motion>', lambda event, stack= rec6, x0 = x0_stack, x = x_stack, y0 = y0_stack, y = y_stack: move_rec(event, stack, x0, x, y0, y))        

#to make the rectangles move
def move_rec(event, stack, x0, y0, x, y):
    global unchanged
    unchanged = "no"

    if win_already == "yes":
        pass
    else:
    
        coordinate_stack = mycanvas.coords(stack)
        forlength_x0_stack, forlength_x_stack, forlength_y0_stack, forlength_y_stack = coordinate_stack[0], coordinate_stack[2], coordinate_stack[3], coordinate_stack[1]
        length_stack = forlength_x_stack - forlength_x0_stack
 
        coordinates = mycanvas.coords(stack)
        mycanvas.coords(stack, event.x - ((coordinates[2]-coordinates[0])/2), event.y + 15, event.x + ((coordinates[2] - coordinates[0])/2), event.y - 15)
        if length_stack == 40:
            root.bind('<ButtonRelease-1>', lambda event, stack=stack, x0 = x0, y0 = y0, x = x, y = y: release_rec1(event, stack, x0, y0, x, y)) 
        if length_stack == 80:
            root.bind('<ButtonRelease-1>', lambda event, stack=stack, x0=x0, y0 = y0, x = x, y = y: release_rec2(event, stack, x0, y0, x, y))
        if length_stack == 120:
            root.bind('<ButtonRelease-1>', lambda event, stack = stack, x0=x0, y0 = y0, x = x, y = y: release_rec3(event, stack, x0, y0, x, y))         
        if length_stack == 160:
            root.bind('<ButtonRelease-1>', lambda event, stack=stack, x0=x0, y0 = y0, x = x, y = y: release_rec4(event, stack, x0, y0, x, y))
        if length_stack == 200:
            root.bind('<ButtonRelease-1>', lambda event, stack=stack, x0=x, y0 = y0, x = x, y = y0: release_rec5(event, stack, x0, y0, x, y))
        if length_stack == 240:
            root.bind('<ButtonRelease-1>', lambda event, stack=stack, x0=x0, y0=yo, x=x, y=y: release_rec6(event, stack, x0, y0, x, y))

#create_rec -> when rec is from stack 
#create_rec_bis -> when rec is not from stack of origin

def create_rec1():
    global rec1, delete
    if len(origin) == 1:
            rec1 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec1 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec1 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 4:
            rec1 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")
    if len(origin) == 5:
            rec1 = mycanvas.create_rectangle(left_end, 425, right_end, 395,  fill = "dark goldenrod")
    if len(origin) == 6:
            rec1 = mycanvas.create_rectangle(left_end, 395, right_end, 365,  fill = "dark goldenrod")
    if delete == "yes":
            mycanvas.delete(rec1)
            delete = "no"
   

def create_rec1_bis():
    global rec1
    print("issue")
    if len(origin) == 0:
            rec1 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 1:
            rec1 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec1 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec1 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")
    if len(origin) == 4:
            rec1 = mycanvas.create_rectangle(left_end, 425, right_end, 395,  fill = "dark goldenrod")
    if len(origin) == 5:
            rec1 = mycanvas.create_rectangle(left_end, 395, right_end, 365,  fill = "dark goldenrod")

def create_rec2():
    global rec2
    print(len(origin))
    if len(origin) == 1:
            rec2 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec2 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec2 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 4:
            rec2 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")
    if len(origin) == 5:
            rec2 = mycanvas.create_rectangle(left_end, 425, right_end, 395,  fill = "dark goldenrod")

def create_rec2_bis():
    global rec2
    if len(origin) == 0:
            rec2 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 1:
            rec2 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec2 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec2 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")
    if len(origin) == 4:
            rec2 = mycanvas.create_rectangle(left_end, 425, right_end, 395,  fill = "dark goldenrod")
        
def create_rec3():
    global rec3
    if len(origin) == 1:
            rec3 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec3 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec3 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 4:
            rec3 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")

def create_rec3_bis():
    global rec3
    if len(origin) == 0:
            rec3 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 1:
            rec3 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec3 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec3 = mycanvas.create_rectangle(left_end, 455, right_end, 425,  fill = "dark goldenrod")

def create_rec4():
    global rec4
    if len(origin) == 1:
            rec4 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec4 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 3:
            rec4 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")

def create_rec4_bis():
    global rec4
    if len(origin) == 0:
            rec4 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 1:
            rec4 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec4 = mycanvas.create_rectangle(left_end, 485, right_end, 455,  fill = "dark goldenrod")

def create_rec5():
    global rec5
    if len(origin) == 1:
            rec5 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 2:
            rec5 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")

def create_rec5_bis():
    global rec5
    if len(origin) == 0:
            rec5 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")
    if len(origin) == 1:
            rec5 = mycanvas.create_rectangle(left_end, 515, right_end, 485,  fill = "dark goldenrod")

def create_rec6():
    global rec6
    if len(origin) == 1:
            rec6 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")

def create_rec6_bis():
    global rec6
    if len(origin) == 0:
            rec6 = mycanvas.create_rectangle(left_end, 545, right_end, 515,  fill = "dark goldenrod")

    
def release_rec1(event, stack, x0, y0, x, y):
    global unchanged, origin, left_end, right_end, stacks_level_release
    if stacks_level_release == "no" or win_already == "yes":
        pass
    else:
        origin = " " 
        unchanged = "no"
        if event.x<480:
            origin = left_stack   
            left_end = 330
            right_end = 370
        if 480<event.x<950:
            origin = middle_stack
            left_end = 655
            right_end = 695
        if event.x>950:
            origin = right_stack
            left_end = 980
            right_end = 1020
   
        if event.x < 480:
            if "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec1()
            else:
            
                mycanvas.delete(stack)
                create_rec1_bis()
            
        if 480 < event.x < 950:
            if "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec1()
            else:
                mycanvas.delete(stack)
                create_rec1_bis()      
       
        if event.x > 950:
             if "1" in right_stack:
                 mycanvas.delete(stack)
                 unchanged = "yes"
                 create_rec1()
             else:
                 mycanvas.delete(stack)
                 create_rec1_bis()
             
        update_stack(event, "1", unchanged, x0)

             
def release_rec2(event, stack, x0, y0, x, y):
    global unchanged, origin, left_end, right_end, rec2
    if stacks_level_release == "no":
        pass
    else:
        origin = " " 
        unchanged = "no"
        if event.x<480:
            origin = left_stack
            left_end = 310
            right_end = 390
        if 480<event.x< 950:
            origin = middle_stack
            left_end = 635
            right_end = 715
        if event.x>950:
            origin = right_stack
            left_end = 960
            right_end = 1040
    
        if event.x < 480:
            if "2" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec2()
            if "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec2 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec2_bis()
        
        if 480 < event.x < 950:
            if "2" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec2()
            if "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec2 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec2_bis()
            
        if event.x > 950:
            if "2" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec2()
            if "1" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec2 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec2_bis()
            
    update_stack(event, "2", unchanged, x0)
    
    
def release_rec3(event, stack, x0, y0, x, y):
    global unchanged, origin, left_end, right_end, rec3
    if stacks_level_release == "no":
        pass
    else:
        
        origin = " " 
        unchanged = "no"
        if event.x<=535:
            origin = left_stack
            left_end = 290
            right_end = 410
        if 535<event.x<950:
            origin = middle_stack
            left_end = 615
            right_end = 735
        if event.x>950:
            origin = right_stack
            left_end = 940
            right_end = 1060
        
        if event.x < 480:
            if "3" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec3()
            if "2" in left_stack or "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec3 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec3_bis()
           
        if 480 < event.x < 950:
            if "3" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec3()
            if "2" in middle_stack or "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec3 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec3_bis()
       
        if event.x > 950:
            if "3" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec3()
            if "2" in right_stack or "1" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec3 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec3_bis()

    update_stack(event, "3", unchanged, x0)

def release_rec4(event,stack,  x0, y0, x, y):
    global unchanged, origin, left_end, right_end, rec4
    if stacks_level_release == "no":
        pass
    else:
        origin = " "
        unchanged = "no"
        if event.x<480:
            origin = left_stack
            left_end = 270
            right_end = 430
        if 480<event.x<950:
            origin = middle_stack
            left_end = 595
            right_end = 755
        if event.x>950:
            origin = right_stack
            left_end = 920
            right_end = 1080
    
        if event.x < 480:
            if "4" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec4()
            if "3" in left_stack or "2" in left_stack or "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec4 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec4_bis()
            
        if 480 < event.x < 950:
        
             if "4" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec4()
             if "3" in middle_stack or "2" in middle_stack or "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec4 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
             else:
                mycanvas.delete(stack)
                create_rec4_bis()
        
        if event.x > 950:
        
            if "4" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec4()
            if "3" in right_stack or "2" in right_stack or "1" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec4 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                print("all gooood") 
                mycanvas.delete(stack)
                create_rec4_bis()
            
    update_stack(event, "4", unchanged, x0)
        

def release_rec5(event, stack, x0, y0, x, y):
    global unchanged, origin, left_end, right_end, rec5
    if stacks_level_release == "no":
        pass
    else:
        origin = " " 
        unchanged = "no"
        if event.x<480:
            origin = left_stack
            left_end = 250
            right_end = 450
        if 480<event.x<950:
            origin = middle_stack
            left_end = 575
            right_end = 775
        if event.x>950:
            origin = right_stack
            left_end = 900
            right_end = 1100
    
        if event.x < 480:
            if "5" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec5()
            if "4" in left_stack or "3" in left_stack or "2" in left_stack or "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec5 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec5_bis()
            
        if 480 < event.x < 950:
             if "5" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec5()
             
             if "4" in middle_stack or "3" in middle_stack or "2" in middle_stack or "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec5 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
             else:
                 mycanvas.delete(stack)
                 create_rec5_bis()
        if event.x > 950:
             if "5" in right_stack:
                 mycanvas.delete(stack)
                 unchanged = "yes"
                 create_rec5()
             if "4" in right_stack or "3" in right_stack or "2" in right_stack or "1" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec5 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
             else:
                 mycanvas.delete(stack)
                 create_rec5_bis()

    update_stack(event, "5", unchanged, x0)
        

def release_rec6(event, stack, x0, y0, x, y):
    global unchanged, origin, left_end, right_end, rec6
    if stacks_level_release == "no":
        pass
    else:
        origin = " "
        unchanged = "no"
        if event.x<480:
            origin = left_stack
            left_end = 230
            right_end = 470
        if 480<event.x<950:
            origin = middle_stack
            left_end = 555
            right_end = 795
        if event.x>950:
            origin = right_stack
            left_end = 880
            right_end = 1120
    
        if event.x < 480:
            if "6" in left_stack: 
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec6()
            if "5" in left_stack or "4" in left_stack or "3" in left_stack or "2" in left_stack or "1" in left_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec6 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec6_bis()
       
        if 480 < event.x < 950:
            if "6" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                create_rec6()
            if "5" in middle_stack or "4" in middle_stack or "3" in middle_stack or "2" in middle_stack or "1" in middle_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec6 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                mycanvas.delete(stack)
                create_rec6_bis()
        
        if event.x > 950:
            if "6" in right_stack:
                 mycanvas.delete(stack)
                 unchanged = "yes"
                 create_rec6()
            
            if "5" in right_stack or "4" in right_stack or "3" in right_stack or "2" in right_stack or "1" in right_stack:
                mycanvas.delete(stack)
                unchanged = "yes"
                rec6 = mycanvas.create_rectangle(x0, x, y0, y, fill = "dark goldenrod")
            else:
                 mycanvas.delete(stack)
                 create_rec6_bis()
        
    update_stack(event, "6", unchanged, x0)
 
def activate():
    if win_already == "yes":
        pass
    else:
        print("works")
        root.bind('<Button-1>', nextmove)

activate()

