# rsz_1438840048-2cf71ed69d-findangle.png  is a right triangle,  at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side .
# The second line contains the length of side .

# Constraints


# Lengths  and  are natural numbers.
# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10
# Sample Output

# 45°

# Solution:
# Given the right triangle, we can use the tangent function to find the angle.
# tan(angle) = opposite/adjacent
# angle = arctan(opposite/adjacent)
# angle = arctan(AB/BC)
# angle = arctan(10/10)
# angle = arctan(1)

import math

def angleMBC(AB, BC):
    angle = math.degrees(math.atan(AB/BC))
    print(str(round(angle)) + chr(176))

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    angleMBC(AB, BC)
