print('====Welcome to Python Function====')
def calculator():
    print('===============================')
    print("---Calculator using Function---")
    print('===============================')
    print('A for Adding')
    print('B for Substraction')
    print('C for Multiplication')
    print('D for Division')
        # print('E for Exit')
    while True:
        lists = ['a','b','c','d']
            
        Input_Choice = input('Enter your Choice:').lower()
            
            # if Input_Choice==lists[4]:
            #     print('bye')
            #     break
        num1 = float(input('Enter first:'))
        num2 = float(input("Enter Second:"))
        
        if Input_Choice==lists[0]:
            print(f'{num1} + {num2} = {num1+num2}')
        elif Input_Choice==lists[1]:
            print(f'{num1} - {num2} = {num1-num2}')
        elif Input_Choice==lists[2]:
            print(f'{num1} / {num2} = {num1/num2}')
        elif Input_Choice==lists[3]:
            print(f'{num1} * {num2} = {num1*num2}')
        
        else:
            print('Invalid Input!')
        mind_change = input('Do you want to continue?').lower()
        if mind_change !="y":
            print('Good bye....')
            break
            
calculator()
def Number():
    print('==========1-100 print==============')
    
    while True:
        change = input('Do you want to show 1-100?').lower()
        if change !="y":
            print('Good bye....')
            break
        for i in range(0,101):
            print(i)
        
Number()
def evenNumber():
    while True:
        change1 = input('Do you want to show Even Number among 1-100?').lower()
        if change1 !="y":
            print('Good bye....')
            break      
        for j in range(0,101,2):
            print(j)
        
evenNumber()
def OddNumber():
    while True:
        change2 = input('Do you want to show odd Number among 1-100?').lower()
        if change2 !="y":
            print('Good bye....')
            break    
        for k in range(1,100,2):
            print(k)
        
OddNumber()
def Namta():
    while True:
        change2 = input('Do you want to do Namta?').lower()
        if change2 !="y":
            print('Good bye....')
            break
        Namta_Input = int(input('Enter your Number for whatever Namta you want'))
        for i in range(0,10):
            print(f'{i} + {Namta_Input} = {i*Namta_Input}')
Namta()       
def showPiramid():
    while True:
        change2 = input('Do you want to show Piramid?').lower()
        if change2 !="y":
            print('Good bye....')
            break
        for i in range(0,5):
            # print(i)
            for j in range(0,i+1):
                print('*',end='')
            print('\r')
        for k in range(5,0,-1):
            for l in range(0,k-1):
                print('*',end='')
            print('\r')

showPiramid()
def add(x,y):
        print(x+y)
add(10,30)



    
    
    


