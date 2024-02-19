# a = []
# while True:
#     v = input('Enter:')
#     if v == 'e':
#         break
#     # else:
#     #     print('Invalid Input')
#     a.append(v)
#     print(a)

class Car():
    def __init__(self,brand,model):
        self.x = brand
        self.y = model
        print(self.x)
    def color(self):
        print('red')
class Bus():
    def __init__(self,brand,model):
        self.x= brand
        self.y= model
        print(self.y)
    def color(self):
        print('black')
car= Car('Toyota','Premio')
bus = Bus('Hino','Balaka')
for i in (car,bus):
    i.color()

