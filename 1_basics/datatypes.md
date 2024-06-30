# Data Types / Object Types

- Number : 1234,3,145,3+4j,0b111,Decimal(),Fraction()
- String : "hello" , 'Bob's',b'a\s01c',u'sp\xc4m'
- List : [1,2,[3,"spam"],4.5] , list(range(10))
- Tuple : ( 1,'spam',4,'U') , namedTuple
- Dictionary : {"food" : "spam" , 'taste':'yumm'} , dict(hrs=10)

- Set : set('abbcd') -> {'a','b','c','d'}

- File : open("eggs.txt") , open(...file_location....)

- Boolean : True, False
- None : None
- Functions , modules , classes

- Advance : Decorators , Generators , Iterators , MetaProgramming


<!-- Hp@DESKTOP-IDIA3RH MINGW64 ~/Desktop/Programing/python (main)        
$ python
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64Type "help", "copyright", "credits" or "license" for more information>>> 2+2
>>> 4.5*7                                                            )] on win32
>>> 2**100                                                           .
>>> import math
3.141592653589793
>>> random.random()
>>> random.choice([1,2,3,4,5])
1
>>> random.choice([1,2,3,4,5])
>>> random.choice([1,2,3,4,5])
4
>>> random.choice([1,2,3,4,5])
3
>>> username = "yatik"
>>> len(username)
5
>>> username[0]
'y'
>>> username[4]
'k'
>>> username[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> username[-2]
'at'
>>> username[3:]
>>> def(username)
    def(username)
SyntaxError: invalid syntax
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '_', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isde', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'spliper', 'zfill']
>>>
[1, 2, [3, 'hel'], 4]
>>> myList = ['U']
>>> myList
['U']
>>> myList = [1,2,[3,"hel"],4 , 'U']
>>> len(myList)
5
>>> myList[2]
[3, 'hel']
>>> myList[-1]
'U'
>>> myList[2:]
[[3, 'hel'], 4, 'U']
>>> myList[:4]
[1, 2, [3, 'hel'], 4]
>>>
>>> myDict = {'one':"welcome" , "two":'yatik'}
{'one': 'welcome', 'two': 'yatik'}
Traceback (most recent call last):
AttributeError: 'dict' object has no attribute 'one'
>>> myDict[one]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'one' is not defined. Did you mean: 'None'?
>>> myDict['one']
'welcome'
>>> myDict['two']
'yatik'
>>>
>>> myTuple = (>>>
>>>
>>> myTuple = (1,2,3,"4")
>>> myTuple
(1, 2, 3, '4')
>>> myTuple[0]
1
>>> myTuple[3]
'4'
>>> myTuple[-1]
'4'
>>> myTuple[1:]
(2, 3, '4')
>>> myTuple[:3]
(1, 2, 3)
>>> myTuple[1:3]
(2, 3)
>>> len(myTuple)
4 -->