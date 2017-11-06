# This is exercise 2.1 - 2.4
sheep_size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Long and these are my sheep sizes:")
print(sheep_size)
print()
max_size = sheep_size[0]

for i in range(len(sheep_size)):
    if max_size < sheep_size[i]:
        max_size = sheep_size[i]
print("Now my biggest sheep has size ", max_size, " let's shear it")
print()

for i in range(len(sheep_size)):
    if sheep_size[i] == max_size:
        index_max = i
        break
sheep_size[index_max] = 8
print("After shearing, here is my flock")
print(sheep_size)
print()

for i in range(len(sheep_size)):
    sheep_size[i] += 50
print("One month has passed, now here is my flock")
print(sheep_size)
