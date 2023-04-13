#First program to add two numbers - line 1
# a=10 # store 10 into variable a - line 2
# b=15 # store 10 into variable a - line 3
# c=a+b #add 10 and 15 and store into variable c - line 4
# print("sum=",c) #display the sum - line 5
# c1=2.5+2.5
# c2=3.0-0.5
# c3=c1+c2
# print("sum=",c3)
# print("welcome")
# print(10,25)
# x=4
# y=5
# print("sum=",(x+y))
# x=15.56
# int(x)
# num=15
# float(num)
# a=10
# b=bin(a)
# print(b)
# b=oct(a)
# print(b)
# b=hex(a)
# print(b)
a=10
b=20
if(a>b):
    print("a",a)
else:
    print("b",b)
elements=[10,20,30,40,50]
x=bytes(elements)
for i in x:
    print(i)
    
elements=[10,20,30,40,50]
x=bytearray(elements)
x[0]=88
x[1]=99
for i in x:
    print(i)
    
s={10,20,30,40,50}
print(s)