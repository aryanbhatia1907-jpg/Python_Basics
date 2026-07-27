# Iss se hoga yeh ki agar code mein error aa rha hai kissi line pe toh usse handle kese kare
# Jahan pe lagg rha error hai wahan pe "try" aa rha karke uska "except" banao or except mein jo bhi likhoge woh aayega or Error nahi aayega.. 
x=input("ENter the number:")
print(f"Multiplication of {x} is:")

try:
    for i in range(1,11):
        print(f"{int(x)} X {i} = {int(x)*i}")
except:
    print("Invalid Input and Errors Comeing!!")
print("Some other and important lines os Code")
print("End of Program")

# Isko karne se integer ka error nahi aayega
# try:
#     num=int(input("Enter Num:"))
#     print(num)
# except ValueError:
#     print("Number you entered is not an integer")


# Practice 2: Predict the Output 
# def test_logic():
#     try:
#         return "Returning from Try"
#     finally:
#         print("Printing from Finally")
# print(test_logic())

#Tip: One critical detail is that finally is so strict about running that it will execute even if you use a return statement inside the try block. It "overwrites" the exit process to ensure it finishes its task before the function actually returns