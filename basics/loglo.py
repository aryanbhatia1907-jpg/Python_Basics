x=4
print(x)

def hello():
    global x     # This is used to modify Global Variable 
    x=25
    y=5
    print("Hello  Everyone!")
    print(y)
    print(f"The local Variable is {y}")

print(f"The Global Variable is {x}")
hello()
print(f"The Global Variable is {x}")