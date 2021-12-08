#SOLID RECTANGLE AND HOLLOW RECTANGLE
print("This is solid Rectangle program")
rows1 = int(input("Enter number of rows: "))
columns1 = int(input("Enter number of columns: "))
for i in range(0,rows1):
    for j in range(0,columns1):
        print("*",end='')
    print() 
print("This is hollow rectangle program")
rows2 = int(input("Please Enter the number of rows  : "))
columns2 = int(input("Please Enter the number of columns  : "))
ch = '*'
print("Hollow Rectangle Star Pattern") 
for x in range(rows2):
    for y in range(columns2):
        if(x == 0 or x == rows2 - 1 or y == 0 or y == columns2 - 1):
            print('%c' %ch, end = '')
        else:
            print(' ', end = '')
    print()