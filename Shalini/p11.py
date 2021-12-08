#PROGRAM TO INSERT AN ELEMENT INTO EXISTING ARRAY
a=[]
s=int(input("Enter the size of the array ::"))
print("Enter the Element of array::")
for i in range(int(s)):
   x=int(input(""))
   a.append(x)
index=int(input("enter the index value for insertion: "))
value=int(input("enter the value to be inserted: "))
def insert_(index,value):
    return (a.insert(index,value))
insert_(index,value)
print(a)