height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

height_m = height / 100
BMI = weight / height_m ** 2

print("Your BMI is: ", BMI)

if BMI < 16:
    print("You're severely underweight")
elif BMI < 18.5:
    print("You're underweight")
elif BMI < 25:
    print("You're normal")
elif BMI < 30:
    print("You're overweight")
else:
    print("You're obese")
