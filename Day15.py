# Day15 :
fruits = ['apple','orang','banana','Kiwi','orang','Kiwi']

# length of list >> use (len())
print(len(fruits))

# to add items :
# 1- at the end of the list >> use (.append()) ..
fruits.append('cherry')
print(fruits)

# 2- at specific index >> use (insert( ,'   ')) ..
fruits.insert(1,'strawberry')
print(fruits)

# to remove item :
# 1- remove the specific item (the fist one )>> use (remove())
fruits.remove('orang')
print(fruits)

# 2- remove the specific index or the last itme if index is not specified >> use (pop(  , '  ')) or (pop()) ..
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

# to copy a list with a new name :
# 1- use (copy()) ..
myfruits = fruits.copy()
# 2- use list() ..
myfruits1 = list(fruits)
# note : if ues myfruits2 = fruits >> any change gets to the list fruits it will gets to myfruits2
myfruits2 = fruits

# to remove all itmes >> use (clear()) ..
fruits.clear()
print(fruits)
print(myfruits)
print(myfruits1)
print(myfruits2)

# to create a liste >> use list(())
newlist = list(('hi','hello','boo'))
print(newlist)

# رق م   ان د ك س 
print(newlist.index('hello'))

# ع د
print(myfruits1.count('Kiwi'))

# عكس  
myfruits1.reverse()
print(myfruits1)

#
newlist.sort()
print(newlist)



