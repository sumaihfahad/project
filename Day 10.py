# Day10 :
# 1) Arithmetic operators >> mathematical operation >>
x,y,z = 10,2,3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x%z)
print(x**y)
print(z**y)
print(x//y)
print(x//z)
print(x+x/y*x**z+y)
print('\n')

# 2) Assignment Operators >>
x,y,z,i,j,k,a,b,c,d,e,f = 1,2,3,4,5,6,7,8,9,10,11,12
x+=2 # >> x=x+2
# print(x+=2) > -- not working
y-=1 # >> y=y-1
z*=2 # >> z=z*2
i/=4 #>> i=i/4
j%=3 #>> j=j%3
k//=2
a**=2
b&=1
c|=1
d^=2
e>>=2
f<<=1
print(x,y,z,i,j,k,a,b,c,d,e,f,'\n',sep='\n')

# 3) Comparison Operators >>
x,y,z = 1,3,1
if x==z:
	print('^^')
if y!=x:
	print('\'-\'')
print(x<z)
print(x>=z)
print(y>x)

