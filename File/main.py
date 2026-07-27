f=open('myfile.txt','r')
# f=open('myfile.txt','rb')    #   rb karne se woh file Binary mein khulti hai
text=f.read()                  #    poori file padh leta hai
print(text)
f.close()