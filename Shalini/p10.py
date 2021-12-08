#DISPLAY DISTICT ELEMENTS FROM GIVEN TWO ARRAYS
from array import *
a1=[]
a2=[]
s1=int(input("Enter the size of the Array 1 ::"))
print("Enter the Element of Array 1::")
for i in range(int(s1)):
   x=int(input(""))
   a1.append(x)
s2=int(input("Enter the size of the Array 2 ::"))
print("Enter the Element of Array 2 ::")
for j in range(int(s2)):
   y=int(input(""))
   a2.append(y)
res = list(set(a1+a2))
print(res)
