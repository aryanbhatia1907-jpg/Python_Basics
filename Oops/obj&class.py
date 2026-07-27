class person:
    name="Reigns"
    Age=9
    Occupation="Developer"
    networth= 10
# Self means woh object jisme yeh method call ho rha hai , matlab jese niche , agar do object banaye hai toh fn ko self se pata chale ki kisme daalna like phele a"  kara toh usme then b"
    def info(self):
        print(f"{self.name} is a {self.Occupation}")

a = person()        # Object
b = person()
c = person()
a.name="Roman"                    # Class ka use karke yahan pe directly name change kiya jaa sakta hai
a.Occupation="WWE champ"
b.name="Raman"                   
b.Occupation="Coder"
# print(a.name,"is a",a.Occupation)
a.info()
b.info()
c.info()    # Yahan pe c" ko koi  values nahi di hai to usme default value jayegi    