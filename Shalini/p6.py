#DISPLAYING THE PATTERN
row = int(input('enter the number of lines: '))
c = row // 2
for i in range(1,row+1):
    if i <= (row // 2 + 1):       
        for j in range(1, row+1-i):
            print(' ', end='')
        for j in range(1,i+1):
            print(j, end='')
        for j in range(i-1,0,-1):
            print(j, end='')
    else:
        for j in range(1, i):
            print(' ', end='')
        for j in range(1, c):
            print(j, end='')
        for j in range(c, 0, -1):
            print(j, end='')
        c -= 1      
    print()