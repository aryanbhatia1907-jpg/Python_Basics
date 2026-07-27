class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):       # there is no need of self in staticmethod
        return a+b      # No need of any object

a=math(5)
print(a.num)
a.addtonum(5)
print(a.num)

print(a.add(7,11))
print(math.add(7,11))    # Also call using 'Class name' by staticmethod

#   Normal -- obj.method()
#   @Static -- class.method()