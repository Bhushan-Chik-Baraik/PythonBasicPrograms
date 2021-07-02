

def Great():
    print("Hallow ")
    print("Good Morning ")


# Great()

# def add(x,y):
#     c=x+y
#     return c
# r1 = add(8,5)
# print(r1)
#
# def addSub(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# r1,r2 = addSub(8,5)
# print(r1,r2)
# def Upd(a):
#     print(id(a))
#     a[1] = 8
#     print(id(a))
#     print("x : ",a)
#
# a = [10,2,32,45]
# print(id(a))
# Upd(a)
# print("a : ",a)

# def Per(name,age= 18):
#     print(name)
#     print(age)

# Position Paramiter
# Per(age=23,name='Bhushan')

# Variable Length Argument
# def add(x,*y):
#     c=x
#     for i in y:
#         c=c+i
#     print(c)
# add(5,8,3,2)

# Variable **Keyword Arrgument
# def Person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,": ",j)
# Person('Bhushan',age=21,city='Mumbai',Mob=9523175103)


# Local & Global Variable
a=10
print(id(a))
def Some():
    a = 16
    x=globals()['a']
    print(id(x))

    print("Inside Fun",a)

    globals()['a']=24
Some()
print("OutSide",a)
