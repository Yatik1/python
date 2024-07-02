# Tuple Types in Python

- Tuple is similar to the List in terms of indexing , nested objects and repetition but the main difference between tuple and list is that unlike list which is mutable , tuple is immutable.

<!-- 

>>> mytuple = ('black' , 'white','grey')
>>> mytuple
('black', 'white', 'grey')
>>> mytuple[0]
'black'
>>> mytuple[2]
'grey'
>>> mytuple[1:1]
>>>
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>>  tuple1 = (1,2,3)
>>>  tuple1 = ("1","2")
  File "<stdin>", line 1
    tuple1 = ("1","2")
>>>
>>>
>>> numTuple = (1,2,3)
(1, 2, 3)
>>>
>>> allTuple = numTuple + mytuple
(1, 2, 3, 'black', 'white', 'grey')
>>>
>>> if 1 in allTuple:
...
yes

mytuple = (1,2,3,"mango")
>>> alltuple = mytuple+numTuple
>>> alltuple
>>>
  File "<stdin>", line 1
    alltuple.count(1_
                    ^
SyntaxError: invalid decimal literal
>>>
>>> alltuple.count(1)
2
>>>
>>> alltuple.count(8)
0
>>>
>>> alltuple
(1, 2, 3, 'mango', 1, 6)
>>>
>>> ("one" , "two","three","four","five","six") = alltuple
  File "<stdin>", line 1
    ("one" , "two","three","four","five","six") = alltuple
     ^^^^^
SyntaxError: cannot assign to literal
>>> (one,two,three,four,five,six) = alltuple
>>> one
1
>>> six
6
>>> four
'mango'
>>>
>>> type(alltuple)
<class 'tuple'>

 -->