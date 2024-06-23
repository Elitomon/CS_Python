# Python basic math
# E Monroe
# 19 Oct 2021
import math
print (math.pi)

num1 = 9
num2 = 7

print ("sum is", num1 + num2)
print ("difference is", num1 - num2)
print ("product", num1 * num2)
print ("quotient", num1 / num2)
print ("int quotient", num1 // num2)
print ("exponentiation", num1 ** num2)

print (" ") ####################################

a = float (num1)
b = float (num2)
print ("a is", a, "b is", b)

print (" ") ####################################

flt1 = 9.04
flt2 = 7.43
print ("sum is", flt1 + flt2)
print ("difference is", flt1 - flt2)
print ("product", flt1 * flt2)
print ("quotient", flt1 / flt2)
print ("int quotient", flt1 // flt2)
print ("exponentiation", flt1 ** flt2)

print (" ") ####################################

a = int(flt1)
b = int(flt2)
print ("a equals", a, "b equals", b)

print (' ') ####################################

myInt1 = 5
myInt2 = 5
myInt1 += 1
myInt2 -=1
print ("myInt one", myInt1, "myInt two", myInt2)

myInt1 *= 3
myInt2 /= 4
print ("myInt one", myInt1, "myInt two", myInt2)

print (' ') ####################################

a = 2 + 3 * 4 + 5
print ("a equals", a)
a = (2 + 3) * (4 + 5)
print ("a equals", a)

print (' ') ####################################

my_pi = 3.1415926535
dec_pi = my_pi / 10.0
print ("one tenth pi", dec_pi)
print ("rounded pi", round(dec_pi, 6))

print (' ') ####################################

MI_TO_KM = 1.60934
milesToday = 23.7
print ("Kilometers today were", milesToday * MI_TO_KM)
