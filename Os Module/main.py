import os

if(not os.path.exists("data from Os")):
    os.mkdir("data from Os")

for i in range(0,100):
    os.mkdir(f"data from Os/Day{i+1}")

# iski madad se hum  bahut sare folders ek sath bana sakte hai 