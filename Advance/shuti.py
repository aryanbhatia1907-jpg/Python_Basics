import shutil

# Folder copy karne ke liye
shutil.copytree("100/Oops", "100/MyFolder") 

# File copy karne ke liye
shutil.copy("100/fn.py", "100/MyFolder/MyFile.py")

# File move karne ke liye
shutil.move("100/000.py", "100/MyFolder/f.py")

# Folder delete karne ke liye
shutil.rmtree("100/MyFolder")