def argsTest(a, b):
    if a > b:
        print 'First integer is greater'
        print 'Second integer is lower'

    else:
        print 'Second integer is greater'
        print 'First integer is lower'

print 'Function Argument Demo'
try:
    x = int(raw_input('Enter first integer:  '))
    y = int(raw_input('Enter second integer:  '))
    argsTest(x, y)
except:
    print 'Value is not an integer!'
