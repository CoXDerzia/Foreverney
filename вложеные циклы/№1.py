for x in range (1,9):
    for y in range (1,9):
        if (x+y)%2 == 0:
            print('W', end=' ')
        else:
            print('B', end=' ')
    print()