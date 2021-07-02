# import array
# from array import *
# vals = array.array('i',[20,34,-12,24,30,-66,53])
# # vals.reverse()
# # for i in range(len(vals)):
# #     print(vals[i],end=" ")
#
# for i in vals:
#     print(i,end=" ")

# from array import *
# val = array('u',['a','e','i','o','u'])
# for i in val:
#     print(i,end=" ")
# from array import *
# val = array('i',[2,4,7,5,9,12,8])
# newArr = array(val.typecode,(a*a for a in val))
# for i in newArr:
#     print(i,end=" ")

from array import *
arr = array('i',{})
a = int(input("Enter the Length Of the Array"))
for i in range(a):
    x= int(input("Enter the Next Value"))
    arr.append(x)
print(arr)

val = int(input("Enter the Value To Search"))
k=0
for e in arr:
    if e==val:
       print(k+1)
       break
    k+=1

# print(arr.index(val))
from numpy import *