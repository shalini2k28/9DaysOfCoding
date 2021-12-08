#PROGRAM TO REVERSE A NUMBER
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    rem = num % 10                  
    reverse = reverse * 10 + rem    
    num //= 10                      
print("Reversed number: ", reverse)