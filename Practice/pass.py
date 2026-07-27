import random
chars= "abcd1234@!~`#$%^&*"
length=int(input("Enter length:"))
password=""

for a in range(length):
    password+=random.choice(chars)
print(password)


attempts = 0
password = ""
while password != "123456":
    password = input("Password enter karo: ")
    attempts += 1
    if attempts > 3:
        print("Lockout ho gaya!")
        break
        