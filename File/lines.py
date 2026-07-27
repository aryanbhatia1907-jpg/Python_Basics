f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()

# WRITELINES

f=open('myfile.txt','w')
lines = ['line 1 \n' , 'line 2\n','line 3 \n']
f.writelines(lines)
f.close()

# Readlines or Writelines se hota hai ki kiisi bhi file ko line by line read or write kara jaa sakta hai