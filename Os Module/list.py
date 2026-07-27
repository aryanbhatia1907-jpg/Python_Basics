import os
folders = os.listdir("data from Os")

print(folders)

for folder in  folders:
    print(os.listdir(f"data from Os/{folder}"))

# isme folders ko print kara jaa sakta hai or last line ko karke agar kissi folder ke andar bhi folder hai toh usse bhi kara jaa sakta hai