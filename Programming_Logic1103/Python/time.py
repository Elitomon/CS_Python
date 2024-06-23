# time.py
# get the current time in hrs, mins, & secs
import time

def getTime():
    now = time.time()
    # print('now is', now)
    tStruct = time.localtime(now)
    # print ('time structure is', tStruct)
    clockTime = (str(tStruct.tm_hour) + ':' + str(tStruct.tm_min) + ':' +  str(tStruct.tm_sec))
    # print ('clock time is', clockTime)
    return clockTime

print('the current time is', getTime())
time.sleep(1.6)
print ('the second time is', getTime())
time.sleep(2.3)
print ('the third time is', getTime())
