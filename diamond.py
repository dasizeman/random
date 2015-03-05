__author__ = 'Dave Sizer <dasizer@gmail.com>'

while 1==1:
    try:
        WIDTH = int(raw_input('Width?'))
    except ValueError:
        print 'Not a number!'
        continue

    CHAR = raw_input('Draw character?')

    for i in range(1,WIDTH-1):
        for j in range(1, WIDTH-i):
            print(''),
        for k in range(1,i):
            print (CHAR),
        print ''

    for i in reversed(range(1,WIDTH)):
        for j in range(1, WIDTH-i):
            print(''),
        for k in range(1,i):
            print (CHAR),
        print ''




