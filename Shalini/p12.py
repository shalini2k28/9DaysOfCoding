#TO SEARCH FOR AN ELEMENT IN THE ARRAY
def search(arr,ele):
    for i in range(len(arr)):
        if arr[i]==ele:
            return print("FOUND")
    return print("NOT FOUND")
arr=[]
s=int(input("Enter the size of the array ::"))
print("Enter the Element of array::")
for i in range(int(s)):
   x=int(input(""))
   arr.append(x)
ele=int(input("Enter element to search: "))
search(arr,ele)