from numpy import *

# arr=array([1,2,3,4.0,5,6],int)
# print(arr.dtype)

# arr= linspace(0,15)

# arr = arange(0,15,2)

# arr = logspace(1,40,5)
# print('%.2f' %arr[3])

# arr=zeros(5)

# arr=ones(5)

# arr1 = array(([1,12,24,3,5,6,7,8]))
# arr2 = array(([19,5,6,7,8,9,10,11]))
# arr3 = arr1+arr2
# print(arr3)

# arr = array(([1,2,3,4,5,6,7,8]))
# print(log(arr))

# arr1 = array(([1,2,3,4,5,6,7,8,9]))
# arr2 = array(([6,7,8,9,5,4]))
# print(sqrt(arr))
# print(sum(arr))
# print(min(arr))
# print(max(arr))
# print(sort(arr))
# arr1 = array(([1,2,3,4,5,6,7,8,9]))
# arr2 = array(([6,7,8,9,5,4]))
# print(concatenate([arr1,arr2]))
arr1 = array(([1,2,3,4,5,6,7,8,9]))
# arr2 = arr1
# arr2 = arr1.view()
arr2 = arr1.copy()
arr1[1]=7

print(arr1)
print(arr2)
print(id(arr2))
print(id(arr1))