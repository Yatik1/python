
# Decorators -> 


def debug(func):
    def wrapper():
        print("decorator")
        return func()
    return wrapper

@debug
def hello():
    print("hello")


hello()