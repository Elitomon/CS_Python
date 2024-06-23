# Conditionals2
# more fun stuff
# 2 Nov 2021

myFloat = 1.2 - 1.0

if myFloat == 0.2:
    print ('yes it is 0.2')
else:
    print ('no it is really', myFloat)
    
if myFloat >= 0.199 and myFloat <= 0.211:
    print ('yes it is close enough')
    
print (' ') # range values *****************************

score = 55

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print ('you have earned a', grade)
