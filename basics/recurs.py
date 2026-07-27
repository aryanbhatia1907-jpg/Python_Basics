# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))


# here is the step by step process of using Recursion/ Call funtion again within function..
# 5 * factorial(4)
# 5 * 4 *factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# ~120 

# Countdown
def count(n):
    # Base case: when to stop
    if n==0:
        print(0)
        return 0

    # Recursive case: call itself
    print(n)
    count(n-1)
count(3)



# Fibonacci
def fib(f):
    fib(f)=0,fib(f)=1,fib(f)
    fib(f)=fib(f)+fib(f)
    fib(f)=fib(f)
    fib(f)=fib(f)
print(fib(7)) 