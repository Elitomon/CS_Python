# scope.py
# example variable scope

def subScope():
    varX = 99
    print('inside sub scope varX is', varX)

def scope():
    varX = 50
    print('inside scope varX is', varX)
    for varX in range (1,5,1):
        print('  inside loop varX is', varX)
    print('out of loop varX is', varX)
    subScope()
    print ('after subscope varX is', varX)


if __name__ == '__main__':
    varX = 100
    print('in main varX is', varX)
    scope()
    print ('back in main varX is', varX)




