# This program is used to calculated area and perimeter of circle.

#Import math lib
import math

#Enter radius
radius=eval(input('Enter radius:\n'))
area=(radius**2)*math.pi
perimeter=2*radius*math.pi

#Output circle area and perimeter
print('Area is {0:.2f} and Perimeter is {1:.2f}'.format(area,perimeter))