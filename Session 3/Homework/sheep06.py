sheep_size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Long and these are my sheep sizes:")
print(sheep_size)
print()

max_size = sheep_size[0]

for i in range(len(sheep_size)):
    if max_size < sheep_size[i]:
        max_size = sheep_size[i]
print("Now my biggest sheep has size", max_size, "let's shear it")

for i in range(len(sheep_size)):
    if sheep_size[i] == max_size:
        index_max = i
        break
sheep_size[index_max] = 8
print("After shearing, here is my flock")
print(sheep_size)
print()

month_number = int(input("How many months later do you want to see my flock? "))
print()

for j in range(month_number):
    if j == month_number - 1:
        print("MONTH ", j+1, " :")
        for i in range(len(sheep_size)):
            sheep_size[i] += 50
        print("One month has passed, now here is my flock")
        print(sheep_size)
    else:
        print("MONTH ", j+1, " :")
        for i in range(len(sheep_size)):
            sheep_size[i] += 50
        print("One month has passed, now here is my flock")
        print(sheep_size)

        max_size = sheep_size[0]

        for i in range(len(sheep_size)):
            if max_size < sheep_size[i]:
                max_size = sheep_size[i]
        print("Now my biggest sheep has size", max_size, "let's shear it")

        for i in range(len(sheep_size)):
            if sheep_size[i] == max_size:
                index_max = i
                break
        sheep_size[index_max] = 8
        print("After shearing, here is my flock")
        print(sheep_size)
        print()

    print()

sum_size = 0
for i in range(len(sheep_size)):
    sum_size += sheep_size[i]

sum_money = sum_size * 2
print("My flock has size in total: ",sum_size)
print("I would get",sum_size, "* 2$ =", sum_money)
