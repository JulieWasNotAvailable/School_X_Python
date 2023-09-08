def stopIfZero(a):
    if int(a) == 0:
        return True
    else:
        print('Continue')
        return False

while True:
    if stopIfZero(input('Number: ')):
        break