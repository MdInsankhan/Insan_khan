# a = [10,20,'Insan','Country = Bangladesh']
# b = ['age']
# a.append(b)
# for i in a:
#     if isinstance(i,str):
#         print(i)
# while i== True:
#     b.extend(a)
#     print(b)
a = [100, 200, 300, "","Apple"]
b = [400,500]
c = ['Banana','Jack fruit']
c.sort()
b = c
d = ['Bangladesh']
d.insert(0,'I love')
# for i in a:
#     if type(i) is int:
#         b.append(i)
#         b.sort()
print(b)
for j in a:
     if type(j) is str:
        b.append(j)
        b.sort()
d.extend(b)        
print(d)