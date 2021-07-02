# n=int(input("Enter the Range : "))
# i=0
# fvalue = 0
# svalue = 1
# while i< n:
#     if(i<=1):
#         Next = i
#     else:
#         Next=fvalue+svalue
#         fvalue=svalue
#         svalue=Next
#     print(Next)
#     i+=1
# prime Nummber
# import math
# n = int(input( "Enter the Number To Check:"))
#
# x=math.ceil(n/2)
# # print(x)
#
# for i in range(2,x):
#     if(n%i==0):
#         print("Not A Prime Number")
#         break
# else:
#     print("Prime Number")

# Factorial Number

# n=int(input("Enter the Range : "))
# n=6
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# n=int(input("Enter the Range : "))
n=6
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result = fact(n)
print(result)
