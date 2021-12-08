#PROGRAM FOR ZIP,ZAP,ZOOM
def display(num):
    message="Zip, Zap, Zoom"

    if(num%3==0):
      print("Zip")
    elif(num%5==0):
      print("Zap")
    elif((num%3==0) and (num%5==0)):
      print("Zoom")
    else:
      print("Invalid Number")
    return message

number=int(input("enter an integer: "))
message=display(number)
print(message)