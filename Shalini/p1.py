#PROGRAM TO REMOVE VOWELS FROM STRING
string = input("Enter any string: ")
newstr = string
print("\nRemoving vowels from the given string")
vowels = ('a', 'e', 'i', 'o', 'u')
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"")
print("New string after successfully removed all the vowels:")
print(newstr)