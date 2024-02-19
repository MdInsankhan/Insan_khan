print("'The Calculator is Made by MD. INSAN KHAN'")
print("press 'A' for Addition")
print("press 'B' for Substraction")
print("press 'C' for Multiplication")
print("press 'D' for Division")
print("press 'E' for Exit")
print("------------------------------------------------")
while True:
        lists=["a","b","c","d","e"]
        
        input_choice = input("Choice Above lists:").lower()
        
        if input_choice==lists[4]:
            print("Good bye.......")
            print("Thanks for using this Calculator.")
            break
        
        Number1 = float(input("Insert first number:"))
        Number2 = float(input("Insert second number:"))
        
        
        add = Number1+Number2
        sub = Number1-Number2
        mul = Number1*Number2
        div = Number1/Number2
        
        
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
            

            