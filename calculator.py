print("press 'A' for Addition")
print("press 'B' for Substraction")
print("press 'C' for Multiplication")
print("press 'D' for Division")
print("------------------------------------------------")
def calculator():
    while True:
        Number1 = float(input("Number1:"))
        Number2 = float(input("Number2:"))
        add = Number1+Number2
        sub = Number1-Number2
        mul = Number1*Number2
        div = Number1/Number2
        lists=["a","b","c","d"]

        input_choice = input("Press:")
        if input_choice==lists[0]:
            print(Number1,"+",Number2,"=",add)
        elif input_choice==lists[1]:
            print(Number1,"-",Number2,"=",sub)
        elif input_choice==lists[2]:
            print(Number1,"*",Number2,"=",mul)
        elif input_choice==lists[3]:
            print(Number1,"/",Number2,"=",div)
        else:
            print("invalid input")
        next_calculation = input("Do you want to perform another calculation? (y/n): ")
        if next_calculation.lower() != "y":
            break
calculator()
    
    

    