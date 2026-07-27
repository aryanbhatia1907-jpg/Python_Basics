import time
# def usingWhile():
#     i=0
#     while i<50000:
#         i=i+1
#         print(i)
 
# def usingFor():
#     for i in range(50000):
#         print(i)

# init = time.time()                # time.time() module 1970 se realtime tak time nikalta hai
# usingFor()
# t1=time.time() - init             # yahan pe ho rha h ki upar init pe time fir loop ko chalaya or loop chalne ke baad phir se time.time() nikala or uss se upar jo init pe time usse minus or phir t1 variable pe daal or yeh pata chal gya ki loop chalne pe kitna time laga
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1,"~For")


print(4)
time.sleep(3)                                 # Yeh karne se program seconds mein delay lega (jaise yahan 3 sec), phir uske baad agli line chalayega 
print("This is printed after 3 seconds")


t= time.localtime()                             # iss se program, computer ka local time lega 
formated_time = time.strftime("%Y-%m-%d %H:%M:%S",t)        # time ko str ke roop mein format karega or local_time ki value leke daalega
print(formated_time)