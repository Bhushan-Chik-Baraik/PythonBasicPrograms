
n=int(input("Enter the Range : "))
i=0
fvalue = 0
svalue = 1
while i< n:
    if(i<=1):
        Next = i
    else:
        Next=fvalue+svalue
        fvalue=svalue
        svalue=Next
    print(Next)
    i+=1

# i=1
# while i<=5:
#
#     print("Bhushan")
#     i=i+1
#     # i+=1

# i = 5
# j=1
# while i>=1:
#     print("Bhushan",end=" ")
#     # j=1
#     while j<= 4:
#         print("Rocks",end=" ")
#         j = j + 1
#
#     i=i-1
#     print()