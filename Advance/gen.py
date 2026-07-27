def my_generator():
    for i in range(100000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# generator jo hai woh value store nhi karta woh usse on the fly generate karta hai jitna chahiye jiss se space problem nahi hoti or fast execute hota program

# for j in gen:
#     print(j)