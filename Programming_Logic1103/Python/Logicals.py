# logicals
# Eli monroe
# 2 Nov 2021
# logical operators

username = 'Eli'
password = 'cscc'

# and operators ****************************************

if username == 'Eli' and password == 'cscc':
    print ('Successful sign in')
else:
    print ('Not recognized')

print (' ') # or operator ******************************

leftDoor = 'closed'
rightDoor = 'open'

if leftDoor == 'open' or rightDoor == 'open':
    print ('sound door buzzer')
else:
    print ('Buzzer off')

print (' ') # precenece 
# parenthesis help the and not get mixed with or *******

if (3 < 4 or 7 > 6) and 8 == 4:
    print ('expression is true')
else:
    print ('expression is false')

print (' ') # Not operator *****************************
# made to keep conditions out of the fasle side ********
# if true or if not true, not if false *****************

exp = input('do you have experience with Blackboard? ')

if exp != 'yes':
    print ('here is a link to Blackboard training')
    
