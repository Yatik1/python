str = "ababcdcdecdcdabab"

for char in str : 
    if(str.count(char) == 1):
        print("Unique char is : " , char)
        break
    