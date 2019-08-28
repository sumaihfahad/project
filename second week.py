# Day6 
x = int(5)
y = int(5.3)
z = int('2')
print(x , y , z , sep='\n')  # sep=('\n') using to print variables in different line

x , y , z , w = float(4) , float(3.1) , float('3') , float('3.2')
print(x,y,z,w,sep='\n')


x , y , z = str('sl') , str(3) , str(1.1)
print(x , y , z , sep='\n')


# Day7
print('Hello')

A = 'Sumaih'
print(A)

B = '''Supercapacitors are electronic devices which are used to store
extremely large amounts of electrical charge. They are also known as 
double-layer capacitors or ultracapacitors'''
print(B)

C = 'Hello World'
print(C[1])
print(C[2:5])


# Day8
A = '   Hello World'
print(A)
print(A.strip())
print(A.strip('ld'))
print(A.strip('() ld')) # ^^
print(A.strip('rl')) #-_- not work

print(B.strip('s')) # just remove s from end 
print(B.strip()) # ^^

A = 'Hello World'
print(len(A))

print(A.lower())


print(A.upper())


print(A.replace('H','S'))


print(A.split('e'))
print(A.split(' '))


# Exercises for myself : 
x,y,z=' Sumaih',' Fahad',' Alshareef'
MyName = x + y + z
print(MyName.strip())
print('My name is'+ MyName)
# ^^ Good job ^-^




