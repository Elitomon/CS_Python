# Cylinder.py
# Eli Monroe
# 26 oct 2021
#calculating weight cylinder can withstand per meters cubed
import math
math.pi
math.sqrt

#area / radius calc
force = float(input("what is the force? choose between 100,000-500,000 "))
area = (force / 27000000)
radius = round(float(math.sqrt(area / math.pi)), 4)
print ("the radius is", radius, "meters")
print ("the diameter is", radius * 2, "meters")

#volume calc
height = float(3.7)
volume = float(math.pi*radius**2*height)
print ("the volume is", round(volume, 4), "meters cubed")

#weight calc
weight = float(2400 * volume)
print ("the weight is", round(weight, 4), "kilograms")
