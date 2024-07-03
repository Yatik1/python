username = "Yatik Srivastava"

def func():
    username = "yatik"
    print(username)

print(username) # Yatik Srivastava
func() # yatik

###############################################

x = 99 
def func2(y):
    z = x + y  # x is global variable thus can take value from the global ref.
    return z

result = func2(1)
print(result)  # 100

def func3():
    global x   # global keyword overwrites the value of global variable x. before this x=99 , after this x=12
    x = 12
    
func3()
print(x)
