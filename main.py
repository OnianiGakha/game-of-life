import time
import os
import math
import pygame
import numpy as np
import keyboard
#from paint import startpygame



alivecolor = (255,255,255)
bgcolor = (0,0,0)
gridcolor = (30,30,30)





paused = False
turns = 0
speed = input("speed of simulation (base value = 1) CT if you wanna control time yourself: ")
xgrid = input("width: ")
ygrid = input("height: ")

SCREEN_HEIGHT = int(ygrid) * 80
SCREEN_WIDTH = int(xgrid) * 80

properlayout = ""
gridlayout = []
newgridlayout = []
count = 0
clr = lambda: os.system('cls')
basewaittime = 0.5



#startpygame(SCREEN_WIDTH,SCREEN_HEIGHT)


#for i in range(0,int(ygrid)):
for i in range(0,int(xgrid) * int(ygrid)):
    gridlayout.append("#")





while True:

    count = 0
    county = 1
    properlayout = "   "
    


    for o in range(0,int(xgrid)):
        properlayout+=str(o+1) + " "
    properlayout+= "\n"

    properlayout+=str(county) + "  "
    for v in gridlayout:
        if count!=int(xgrid):
            if count>8:
                properlayout+=v + "  "
            else:
                properlayout+=v + " "
        else:
            county += 1
            count = 0
            if county > 9:
                properlayout+="\n" + str(county) + " " + v + " "
            else:
                properlayout+="\n" + str(county) + "  " + v + " "
        count+=1




    clr()
    
    print(properlayout)
    
    ll = input("put units(like this: x y) and type F to finish: ")


    if ll == "F":
        clr()
        break
    else:
        lx = int(ll.split(" ")[0])
        ly = int(ll.split(" ")[1])

    if gridlayout[(ly-1)*int(xgrid) + (lx - 1)] != "+":
        gridlayout[(ly-1)*int(xgrid) + (lx - 1)] = "+"
    else:
        gridlayout[(ly-1)*int(xgrid) + (lx - 1)] = "#"

zaza = 0

for i in gridlayout:
    if gridlayout[zaza] == "#":
        gridlayout[zaza] = " "  
    zaza+=1
newgridlayout = gridlayout[:]



def checkneibours(kok):



    neiboursamount = 0

    koky = math.floor(kok/int(ygrid)) + 1
    kokx = kok % int(xgrid) + 1


    if kokx != int(xgrid):
        if newgridlayout[kok+1] == "+":
            neiboursamount+=1

        if koky != int(ygrid):
            if newgridlayout[kok + 1  + int(xgrid)] == "+":
                neiboursamount+=1
        
        if koky != 0:        
            if newgridlayout[kok + 1 - int(xgrid)] == "+":
                neiboursamount+=1


    if kokx != 0:
        if newgridlayout[kok-1] == "+":
            neiboursamount+=1

        if koky != int(ygrid):

            if newgridlayout[kok - 1 + int(xgrid)] == "+":
                neiboursamount+=1
        
        if koky != 0:
            if newgridlayout[kok - 1 - int(xgrid)] == "+":
                neiboursamount+=1

    if koky != int(ygrid):

        if newgridlayout[kok + int(xgrid)] == "+":
            neiboursamount+=1

    if koky != 0:

        if newgridlayout[kok - int(xgrid)] == "+":
            neiboursamount+=1

    





    return neiboursamount




while True:

    if keyboard.is_pressed("space"):
        if paused == True:
            paused = False
        else:
            paused = True
        time.sleep(0.4)

    if paused == False:
            
        kok = 0
        count = 0
        properlayout = ""

        newgridlayout = gridlayout[:]

        for v in gridlayout:
            if count!=int(xgrid):
                properlayout+=v + " "
            else:
                count = 0
                properlayout+="\n" + v + " "
            count+=1

        properlayout += "\n" + "\n" + "turns: " + str(turns)




        for ye in newgridlayout:

            neighbours = 0
            neighbours = checkneibours(kok)

            if ye == "+":
                


                if neighbours == 2 or neighbours == 3:
                    pass
                else:
                    gridlayout[kok] = " "
            else:
                if neighbours == 3:
                    gridlayout[kok] = "+"
            kok+=1



        turns += 1
        
        clr()
        
        print(properlayout)
        if speed != "CT":
            time.sleep(basewaittime / int(speed))
        else:
            input()
        









