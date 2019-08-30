# Day 11 ..

# 4) Logical Operators >> used to combine conditional statements >> (and , or , not) >> output is True or False ..
x,y,z = 5,3,1
print(x<10 and y>6)
print(z>0 or x>3)
print(not(z>0 or x>3)) # >> not : returns False if result is true


# 5) Identity Operators >> used to compare the objects, not if they equal, but if they are actually the same object.
x = ['A','B']
y = ['A','B']
z = x
print(x is y)
print(x is z)
print(x is not y)
print(x != y) # >> note: (!=) mean not equal. and it is different from (is not)

a = 'A'
b = 'B'
print(a is b)
a = 1
b = 1
print(a is b) #>> note from myself: if the object is number the ( is ) mean equal


# 6) Membership Operators >> Used to see if the object is in the matrix >> (in , not in )
x = ['A','B','C',1,6]
print('A' in x)
print(1 in x)
print('C' not in x)
print(1 and 6 in x)
print(1 and 5 in x)
print('A' and 'D' in x)


# 7) Bitwise Operators >> used to compare Binary numbers ( & > and , | > or , ^ > xor , ~ > not , >> > zero fill left shift )
# bit = 0 or 1
# byte = 8 bit
# numbers = 4 byte
# bit*2^(bit location)
# 1 2 4 8 16 32 ......
''' Exp: 8 = 00010000 00000000 00000000 00000000
         3 = 11000000 00000000 00000000 00000000
         5 = 10100000 00000000 00000000 00000000
         10= 01010000 00000000 00000000 00000000
         if we use & between (8 and 3) the result is 0 ( no 1 in same bit between them) 
         ....................(10 and 8).......... is 8 ( 1 is in 4th bit for both)
         ....................(3 and 10).......... is 2 ( i is in second bit for both)
         if we use | between (3 and 5) .......... is 7 ( 1 in 3 is in (first bit = 1*2^0=1, and second bit = 1*2^1=2) and in 5 is in (first and 3th bit = 1*2^2=4) so result = 1+2+4=7) 
         if we ues ^ between (5 and 10).......... is 15 (it gives 1 when the bit is different) '''

'''  a   b   = 
 AND 0   0   = 0
     0   1   = 0
     1   0   = 0
     1   1   = 1
 OR  0   0   = 0
     0   1   = 1
     1   0   = 1
     1   1   = 1
 XOR 0   0   = 0
     0   1   = 1
     1   0   = 1
     1   1   = 0 

NOT a  = 
    0  = 1
    1  = 0
''' 
print(8 & 3)
print(8 & 10)
print(3 & 10)
print(3 | 5)
print(5 ^ 10)



# >> beautiful web. >>  https://www.programiz.com/python-programming/operators 