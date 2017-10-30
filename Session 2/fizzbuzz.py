n = int(input("Enter a number: "))

for i in range(n):
    if i % 2 == 0:
        if i % 3 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if i % 3 == 0:
            print("Buzz")
