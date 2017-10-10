def randomWalk(steps):
    x = 0  # Make sure you initialize the position to 0,0 each time the function is called
    y = 0
    directions = ['N', 'E', 'S', 'W']  # To keep track of directions, you could use strings instead of 0, 1, 2, 3.
    for i in range(steps):
        a = random.choice(directions)  # You can use random.choice to choose a dir
        if a == 'N':
            y += 1
            print('Current position: ({},{})'.format(x,y))  # You can print the position using format
        elif a == 'S':
            y -= 1
            print('Current position: ({},{})'.format(x,y))
        elif a == 'E':
            x += 1
            print('Current position: ({},{})'.format(x,y))
        else:
            x -= 1
            print('Current position: ({},{})'.format(x,y))

randomWalk(3)