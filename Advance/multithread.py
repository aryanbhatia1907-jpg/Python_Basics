import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(sec):
    print(f"Sleeping for {sec} seconds")
    time.sleep(sec)
    return sec

time1=time.perf_counter()           # iss se time nikaal sakte hai 

# Normal Code : yeh func ko sleep kar kar ke baari -2 chalayega phele ek ko phir dusre ko 
# func(4)
# func(2)
# func(1)

# Same code using threads : yeh func ko ek sath chalayega
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()

t1.join()       # yeh karne se time 4 sec aayega kyuki ab yeh complete hone ka time bata raha
t2.join()
t3.join()

time2=time.perf_counter()
print("\n",time2-time1)         # time issliye 0 hai kyunki thread ne sirf start kara hai func, baaki ka kaam download bgere woh background mein hoga 

print("\n --Advance Concurrent Modules-- \n")
def poolingDemo():
    with ThreadPoolExecutor() as executer:
        l=[3,5,1,7]
        results=executer.map(func,l)
        for result in results:
            print(result)
poolingDemo()
time3=time.perf_counter()
print("\n",time3-time2) 