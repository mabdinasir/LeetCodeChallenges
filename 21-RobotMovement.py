# Question 21
# Level 3

'''
Question A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following: 
    UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ 
The numbers after the direction are steps. 
Please write a program to compute the distance from current position 
after a sequence of movement and original point. If the distance is a 
float, then just print the nearest integer. Example: If the following 
tuples are given as input to the program: 
UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

Hints: In case of input data being supplied to the question, 
it should be assumed to be a console input.
'''

# Solution:

import math
position = [0,0]

while True:
    s = input("Enter a direction and a number of steps:")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        position[0]+=steps
    elif direction=="DOWN":
        position[0]-=steps
    elif direction=="LEFT":
        position[1]-=steps
    elif direction=="RIGHT":
        position[1]+=steps
    else:
        pass

distance = int(round(math.sqrt(position[1]**2+position[0]**2)))
print(f"The robot has moved {distance} units.")
