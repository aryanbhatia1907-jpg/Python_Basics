marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Bro, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):     # Start hum kahin se bhi kar sakte index ko 0 se yaa 1 etc se start equal kar ke
  print(mark)
  if(index == 3):
    print("Bro, awesome!")

    # Enumerate hume tupple bana ke deta hai or jab hum index ko bata kar mangte hai to woh unpack kar deta hai
for  mark in enumerate(marks):     
      print(mark)