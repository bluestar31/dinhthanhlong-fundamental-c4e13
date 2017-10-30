a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
Delta = b ** 2 - (4 * a * c)
a_2 = a * 2
if a == 0:
    print("Day la phuong trinh bac nhat! Nghiem cua phuong trinh la x = ", -c/b)
elif Delta < 0:
    print("Phuong trinh vo nghiem!")
elif Delta == 0:
    x = -b / a_2
    print("Phuong trinh co nghiem kep x = ", x)
else:
    Delta_root = Delta ** 0.5
    x1 = (-b + Delta_root) / a_2
    x2 = (-b - Delta_root) / a_2
    print("Phuong trinh co 2 nghiem phan biet: x1 = {0}, x2 = {1}".format(x1, x2))
    print("x1 = ", x1)
    print("x2 = ", x2)

print("Phuong trinh da giai xong!")
