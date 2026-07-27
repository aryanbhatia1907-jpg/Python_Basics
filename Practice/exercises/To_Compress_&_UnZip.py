import shutil

# 1. Jis folder ko compress karna hai uska rasta (Path)
folder_to_compress = "_Enter path here_"

# 2. Jo nayi ZIP file banegi uska naam aur jagah
output_zip_name = "_Enter path here_"

# 3. Compress karne ki command (Isse My_Backup.zip ban jayegi)
shutil.make_archive(base_name=output_zip_name, format="zip", root_dir=folder_to_compress)

print("Folder Compressed!")

# To UnZip
shutil.unpack_archive("_Enter path here_.zip", "_Enter path here_")
print("Folder Unzipped!")






