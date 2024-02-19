print("-----Calculator------")
while True:
    self = ["a","s","e"]
    calc=input("Chose +-/* and E for Exit :").lower()
    if calc==self[2]:
        print("bye bye")
        break
    num1=float(input("Enter first Number:"))
    num2=float(input("Enter second Number:"))
    add = num1+num2
    sub = num1-num2
    if calc==self[0]:
        print(add)
    elif calc==self[1]:
        print(sub)
    
    else:
        print("Invalid Input")

            