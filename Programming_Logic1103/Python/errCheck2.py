# error check using try and catch
testFlt = input('please enter your float ')
try:
    myFlt = float(testFlt)
    print ('yes float')
except:
    print('no float')
