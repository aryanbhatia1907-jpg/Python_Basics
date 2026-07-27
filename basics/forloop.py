colors=["Red","Green","Blue","Yellow","Orange"]    # Here colors is a List
for color in colors:
    print(color)
    for i in color:
        print(i)

# Print Numbers Using For Loop 
for x in range(10):
    print(x)

for y in range(1,9,3):   # range(Start,End,Step)
    print("\"",y,"\"")   # Here Step use increment by number You defined in range

# Use of Else with for loop
for i in range(10):
    print(i)
    # if(i==7):          # agar yeh if chal pade to bahar ka else nhi chalega,  kyunki yahan loop khatam nahi sirf break ho rha or woh khatam hone chalta hai..
    #     break
else:
    print("\"Else is now executed and Loop ended.\"")