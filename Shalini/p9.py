#THE SUM OF FIRST N ODD NUMBERS
num = int(input("Print sum of odd numbers till : "))
sum = 0
if num<=0:
    print("Please enter a valid integer")
for i in range(1, num + 1):
    if(not (i % 2) == 0):
        sum += i
print("\nSum of odd numbers from 1 to", num, "is :", sum)