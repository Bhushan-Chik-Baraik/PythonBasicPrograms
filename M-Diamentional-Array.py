from numpy import *
# arr1 = array([
#     [1,2,3,9],[4,5,6,4]
# ])
# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# print(arr1.flatten())

# arr2 = arr1.reshape(2,2,3)
m1=matrix('1,2,3;6,4,5; 1,6,7')
m2=matrix('1,2,3;6,8,5; 2,6,7')
# print(m)
# print(diagonal(m))
# m3= m2+m1
m3= m1*m2
print(m3)