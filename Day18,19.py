# Day 18 and 19 >> a challenge .
# first :
name = ['Mohamad','Ahmad','Feras','Maher']
name2 = name.copy()
name.insert(2,'Yasir')
name.pop(0)
if 'Ahmad' in name2:
	name2.reverse()
print(name)
print(name2)

# secand :
tuple1 = ('java','python','swift')
if 'python' in tuple1:
	print('yes, python is in tuple1')