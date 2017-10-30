# n = int(input("Enter a number: "))
#
# for i in range(n):
#     print(i, end=" ")

# print(*range(n))

n = int(input("Enter a number: "))

# for i in range(0, n, 2):
#     print(i)

for i in range(n):
    if i % 2 == 0:
        print(i)
