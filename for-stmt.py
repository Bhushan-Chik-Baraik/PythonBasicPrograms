# x = [23,45,'Bhushan',77,34,'Rani',34]

# for i in [23, 45, 'Bhushan', 'Rani', 34]:
#     print(i)
# for i in range(11,21,2):
#     print(i, end=" ")


# for i in range(21,10,-2):
#     print(i, end=" ")

# for i in range(1, 10):
#     if i % 3 != 0:
#         print(i, end=" ")

#  Printing Pattern
# n=int(input("Ente rthe number of Rows"))
# for i in range(n):
#     for j in range(n):
#         print(" *",end="")
#     print("")
# n=int(input("Ente rthe number of Rows"))
# for i in range(n):
#     for j in range(i,n):
#         print(" *",end="")
#     print()
n=int(input("Ente rthe number of Rows"))
for i in range(n):
    for j in range(i,n):
        print(j+1,end=" ")
    print()
