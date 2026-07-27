f=open('myfile.txt','w')
f.write("Hello World You are great")
f.close()

# APPENDING A FILE 
f=open('myfile.txt','a')
f.write("\nThis is content added through Append")
f.close()

# WITH STATEMENT

with open('myfile.txt','a') as f:
    f.write("\nUse of With Statement")
    # iska mainly use isliye hai ki agar file ko band nhi kara ho toh bhi write kar deta hai , Normally esa nhi hota hai