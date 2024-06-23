# Conditionals
# Eli Monroe
# 2 Nov 2021
# some basic if then structures

ticket_price = 10.00
age = 60

# single alternative *********************************** 

if age > 55:
    print ('senior discount applies')
    ticket_price = ticket_price - (ticket_price * .15)

if age <= 12:
     print ('Children\'s discount applies')
     ticket_price = ticket_price - (ticket_price * .5)

print ('ticket price is', ticket_price)

print (' ') # dual alternative *************************

direction = 'right'

# == for testing otherwise it will store value *********

if direction == 'right':
     print ('you are driving east')
else:
    print ('You are driving west')

print (' ') # booleans *********************************

flag = False

if flag:
    print ('the flag is true')
else:
    print ('no the flag is false')

print (' ') # three way conditionals *******************

myInt = 19

if myInt > 0:
    print ('it is positive')
elif myInt < 0:
    print ('it is negative')
else:
    print ('it is zero')
