def sumAllParams(*args):
    
    for i in args:
        print(i*2)
        
    return sum(args)

print(sumAllParams(1,2,3,4))  

# $ python sol7.py
# 2
# 4
# 6
# 8
# 10
