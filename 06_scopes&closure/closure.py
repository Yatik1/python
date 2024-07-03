def f1():
    x=88
    def f2():
        print(x)
    return f2

print(f1())  # <function f1.<locals>.f2 at 0x000001FE772C9800>

result = f1()
result() # 88

####################----------------################################

def number(n):
    def actual(x):
        return x**n
    return actual

print(number(2)) # <function number.<locals>.actual at 0x0000015F707A98A0>

f=number(2) # arg 2 is for number(n) parameter 
print(f(3)) # here arg:3 is for the actual(x) parameter

g=number(4)
print(g(3))  # 81 -> 3**4