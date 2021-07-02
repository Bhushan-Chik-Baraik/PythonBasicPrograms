# Fabonacci Series
# n = int(input("Enter the Range"))
# i=0
# fvalue=0
# svalue=1
# for i in range(n):
#     if(i<=1):
#         x=i
#     else:
#         x=fvalue+svalue
#         fvalue=svalue
#         svalue=x
#     print(x)
#     i+=1


# prime Nummber
import math
n = int(input( "Enter the Number To Check:"))

x=math.ceil(n/2)
# print(x)

for i in range(2,x):
    if(n%i==0):
        print("Not A Prime Number")
        break
else:
    print("Prime Number")

#
#
# upper = int(input("Enter the upper value:"))
# for number in range(upper+1):
#     # if number>1:
#         for i in range(2,number):
#             if (number%i)==0:
#                 break
#         else:
#             print(number,end=" ")

#
# for i in range(101):
#     if i%2==0 or i%5==0:
#         pass
#     else:
#         print(i, end=" ")


# x = int(input("How Many Candy you want??"))
# av = 4
# i = 1
# while i <= x:
#     if i > av:
#         print("Out Of Stock")
#         break
#     print("Candy")
#     i += 1
# print("Bye")

#  for i in range(20):
#     if i%3==0 or i%5==0:
#         continue
#     # if i%5==0:
#     #     continue
#     print(i, end=" ")
