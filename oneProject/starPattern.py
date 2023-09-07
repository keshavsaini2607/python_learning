

def printStars(noOfCols):
    for i in range(noOfCols):
        j = noOfCols - i
        while(j >= 0):
            print(' ', end='')
            j -= 1
        print('* ', end='')
    print('')


printStars(5)