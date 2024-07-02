import time
print("I am here")
username = "Yatik"
print(username)

# $ python
# Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for 
# more information.
# >>> f=open("iteration.py")
# >>>
# >>> f.readline()
# 'import time\n'
# >>> f.readline()
# 'print("I am here")\n'
# >>> f.readline()
# 'username = "Yatik"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''

# >>> f = open("iteration.py")
# <_io.TextIOWrapper name='iteration.py' mode='r' encoding='cp1252'>
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'print("I am here")\n'
# >>> f.__next__()
# 'username = "Yatik"\n'
# >>> f.__next__()
# 'print(username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# >>> for line in open("iteration.py"):
# ...     print(line)
# import time

# print("I am here")

# username = "Yatik"

# print(username)
# >>>
# >>> for line in open("iteration.py"):
# ...     print(line , end="")
# ...
# import time
# print("I am here")
# username = "Yatik"
# print(username)


# myList = [1,2,3,4,5]
# [1, 2, 3, 4, 5]
# >>> I = iter(myList)
# <list_iterator object at 0x00000224D0DE90C0>
# >>> I.__next__()
# 1
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I
# <list_iterator object at 0x00000224D0DE90C0>
# >>> I.__next__()
# 4
# >>> I
# <list_iterator object at 0x00000224D0DE90C0>
# >>> I.__next__()
# 5
# >>> I
# <list_iterator object at 0x00000224D0DE90C0>
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration



