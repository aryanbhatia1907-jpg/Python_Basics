import os

if(not os.path.exists("data from Os")):
    os.mkdir("data from Os")

for i in range(0,100):
    os.rename(f"data from Os/Day{i+1}",f"data from Os/Tutorial{i+1}") 

# Folders ko directly rename karne ke liye 