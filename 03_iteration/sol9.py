items = ["apple", "banana", "orange", "apple", "mango"]

uniqueItem = set()

for item in items :
    if item in uniqueItem:
        print("Already in the bucket : " , item)
        break
    uniqueItem.add(item)
    
    