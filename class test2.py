# insert value in list from user
c= []
while True:
    
    d = input('Enter your Item:')

    c.append(d)
    print(c)
    if d=="e":
        print('good bye')
        break

# a= [2,56,67,60,22,12,2] find the no of 2
a= [2,56,67,60,22,12,2]
print(a.count(2))

# Insert keys and values to existing dictionary
b= {'Name':'Insan'}
b.update({'city':'Dhaka'})
print(b)
print(b.get('city'))

# find prime no into 1 to 100
x = []
for i in range(1,101):
    if i %2 == 0:
        x.append(i)
        
print(x)
        




    

