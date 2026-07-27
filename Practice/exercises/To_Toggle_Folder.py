import shutil

# Folder copy karne ke liye
shutil.copytree("src", "des") 

# File copy karne ke liye
shutil.copy("src.ext", "des.ext")

# File move karne ke liye
shutil.move("src.ext", "des.ext")

# Folder delete karne ke liye
shutil.rmtree("MyFolder")

# src - source, des - destination, ext - extention
# Ex- shutil.copytree("C:/Users/Aryan Bhatia/Desktop/Coding/Markdown", "C:/Users/Aryan Bhatia/Desktop/Coding/_Snipps/New")
# Use { / } instead of { \ }