# (30 points) The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions and
# stumbles to the next intersection, then again randomly picks one of four directions, and so on. 
# You might think that on average the drunkard doesn’t move very far because the choices cancel each other out, but that is actually not the case.

# Write a function to calculate the distance after n intersections.

import random
import math

def drunkard_walk(n):
    x = 0
    y = 0

    for i in range(n):
        a = random.randint(0, 4)
        if a == 0:
            y+=1
        elif a == 1:
            x+=1
        elif a == 3:
            y-=1
        else:
            x-=1
    return math.sqrt (x**2 + y**2)

print(str(drunkard_walk(10)))
