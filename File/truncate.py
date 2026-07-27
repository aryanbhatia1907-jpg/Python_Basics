with open('myfile.txt','w') as f:
    f.write("\nUse of truncate ")
    f.truncate(7)

with open('myfile.txt','r') as f:
    print(f.read())

# truncate karne se yeh hoga ki file kitne bytes ki rahe sirf 
# yahan pe file mein jyada bytes hai par truncate karke woh utna hi file save kar rhi phir usse hi read kar rhi