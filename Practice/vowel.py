x=input("input:")
vowels="aeiouAEIOU"
count=0

for y in x:
    if y in vowels:
        count+=1
print(count)