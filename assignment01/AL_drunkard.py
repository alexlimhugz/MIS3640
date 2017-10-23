import random
import turtle
import math
drunkard = turtle.Turtle()

def drunkard_walk(x, y, n):
    x = 0  #Origin (0,0)
    y = 0  #Origin (0,0)
    directions = ['N', 'S', 'E', 'W']  #Four options/directions 
    for blocks in range(n): 
        a = random.choice(directions)  #Picking a direction at random
        if a == 'N': #North
            y += 1
            print('Walked to: ({},{})'.format(x,y))  
            drunkard.setheading(90) #Setting the orientation of the turtle to 90 degrees (North)
        elif a == 'S': #South
            y -= 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(270) #Setting the orientation of the turtle to 270 degrees (South)
        elif a == 'E': #East
            x += 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(0) #Setting the orientation of the turtle to 0 degrees (East)
        else: #West                                              
            x -= 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(180) #Setting the orientation of the turtle to 180 degrees (West)
        drunkard.forward(50) #Moving the turtle forward by 50 (length of the lines in turtle)
    
drunkard_walk(0,0,20)

distance = drunkard_walk(0, 0, 20)
n = 20
x_2 = int(input("Please enter last x coordinate:")) #last x coordinate needed in order to calculate distance
y_2 = int(input("Please enter last y coordinate:")) #last y coordinate needed in order to calculate distance
xx = (x_2 - 0)**2 #last x cordinate & starting x coordinate in partial equation of distance formula
yy = (y_2 - 0)**2 #last y cordinate & starting y coordinate in partial equation of distance formula
distance = math.sqrt(xx + yy) 

print("The drunkard started from (%d,%d)." % (0, 0))
print("After", n, "intersections, he's", distance, "blocks from where he started.")

turtle.mainloop()