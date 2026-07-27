import os

if(not os.path.exists("_Enter Path here_")):
    os.mkdir("_Enter Path here_")
    print("Directory Created!!")
# To create Folder


os.rename("old", "new")  # rename
import os

# Isse current folder ki saari files ki list milegi
files_list = os.listdir("_Enter path here_")
print(files_list)