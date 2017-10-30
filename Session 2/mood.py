# print("Hi there, this is a superuser gateway")
#
# # string.upper() , string.lower()
#
# while True:
#
#     username = input("Username: ")
#     if username.lower() == "c4e":
#         password = input("Password: ")
#         if password == "codethechange":
#             print("Welcome, c4e")
#         else:
#             print("Password is incorrect")
#     else:
#         print("You are not superuser")

from random import randrange
from random import randint

print("Hello, I'm Husky")

n = randint(1, 100)
if n < 30:
    print("I'm feeling sad")
elif n < 60:
    print("I'm feeling OK")
else:
    print("""───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀""")
