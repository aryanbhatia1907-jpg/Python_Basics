# Finally block hamesa execute hoga chahe fn kyu naa ho
# Normal print function ke return karne pe execute nahi hoga , Normally kahin-2 execute nahi hota like fn , else etc..
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")

x = func1()
print(x)
