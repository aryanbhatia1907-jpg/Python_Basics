class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i  + {self.j}j + {self.k}k"

    def __add__(self,x):
        # return f"{self.i+x.i}i  + {self.j+x.j}j + {self.k+x.k}k"              # yeh karne se Class type str hi rahegi kyuki woh humne define kari hai 
        return vector(self.i+x.i, self.j+x.j, self.k+x.k)                       # yeh karne se Class type Vector mein define ho jayegi  or ab hum vector operations kar sakte hai.
 
    
v1=vector(3,4,5)
print(v1)
v2=vector(2,4,6)
print(v2)
print(v1+v2)
print(type(v1+v2))