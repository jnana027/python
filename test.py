#(1) PYTHON INTRODUCTION
# Python is a General purpose high level programming language.
# python is introduced by Guido Van Rossum in the yaer 1989 while working at NTI in Netharland but python officically introduced in February 20th 1991.
# python and javascript both are dynamically typed programming language. 
# a=10
# print(type(a))
# a=10.6
# print(type(a))
# a='Jnana'
# print(type(a))

#(2) PYTHON FEATURES
# 1.Easy and simple to learn
# 2.forward and open source
# 3.high level programming language
# 4.platform independent
# 5.portability
# 6.***Dynamic Typed
# 7.***Both object oriented and procedure oriented
# 8.Interprited
# 9.Extensible
# 10.embedded
# 11.***Extensible library

# WRITE A PROGRAM TO GENERATE 6 DIGIT OTP
# from random import randint
# print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep="")

#(3) PYTHON LIMITATION
# 1.Mobile application
# 2.Enterprises application
#     ex:Banking application,Telecom application
# 3.Performance is low

#(4) PYTHON FLAVOURS
# 1.cpython(for C language application)
# 2.jpython/jython(for java language aplication)
# 3.Iron python(for c# .net)
# 4.ruby python(for Ruby platform)
# 5.anaconda python(work with large amount of data)
# 6.stackless(python for concurrence)
# 7.pypy(python for speed)


#(5) PYTHON IDENTIFIERS
# a  ->Variable
# _a  ->protected
# __a  ->private
# __a__  ->magic method

# import keyword
# s=keyword.kwlist
# print(s)

# convert binary to decimal
# a=0b1111
# print(a)

# convert  octal to decimal
# a=0o123
# print(a)

# convert binary to hexa decimal
# a=0x10
# print(a)
# b=0xface
# print(b)


# bin()  ->this method is used to convert, from decimal to binary numbers
# oct()  ->this method is used to convert, from decimal to octal numbers
# hex()  ->this method is used to convert, from decimal to hexa decimal numbers

# a=1.2e3  -->exponatioal form
# print(a)

# complex datatype
# a=10+20j
# print(type(a))
# print(a.real)
# print(a.imag)
# b=20+30j
# print(a+b)



# def myfun(a):
#     a=a+2
#     a=a*2
#     return a
# print(myfun(2))

# string data types
# triple quotes
# 1.to define multiple lines string literals/value
# 2.to use '' and "" as normal characters in our string 
# 3.define doc string

# a='abcdefghijklmnopqrstuvwxyz'
# print(a[3])
# slice operator
#syn: a[begin:end:step]
# print(a[3:9])
# print(a[3:])
# print(a[:9])
# print(a[3:9:2])
# print(a[3::2])
# print(a[:9:2])
# print(a[:])
# print(a[-1:])
# print(a[::-1])
# print(a[:9:-1])
# print(a[3::-1])
# print(a[0].upper()+a[1:])
# print(a[0].upper()+a[1:].upper())
# print(a[-1].upper())
# print(a[0:-2]+a[-1].upper())
# print(a[:len(a)-1]+a[-1].upper())
# print(a[0].upper()+a[1:len(a)-1]+a[-1].upper())

# a='jnana'
# print(a+a)
# print(a*3)
# print(3*a)

# type conversion/type casting
# int(),float(),bool(),complex(),str()
# print(int(10.5))
# print(int(True))
# print(int('10'))
# print(float(14))
# print(float(0b1111))
# print(float(0xfa))
# print(float(True))
# print(float('14'))
# print(complex(10))
# print(complex(0b111))
# print(complex(0xfa))
# print(complex(10,20))
# print(complex(0b11,0b10))
# print(complex(0xfe,0xea))
# print(bool(10))
# print(bool(0))
# print(bool(10.22))
# print(bool(10+20j))
# print(bool('True'))
# print(bool('no'))
# print(bool(''))
# print(str(10))
# print(str(10.5))
# print(str(10+20j))


# *34
# *All fundamental data types(int,float,complex,bool,str) are immutaable(can not be change)
# once we create an object,we can not perform any change in that object if we trying to perform any changes with those changes ,a new object will be created. 
# x=10
# print(id(x))
# x=x+1
# print(id(x))
# a=10
# b=a
# print(id(a))
# print(id(b))
# b=b+1
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# *35
# pvm(python virtual machine )is responsible for creating object.
# a=10
# b=10
# c=10
# print(id(a))
# print(id(b))
# print(id(c))
# print(a is b)
# a='jnana'
# b='jnana'
# print(id(a))
# print(id(b))
# print(a is b)

# *36
# l=[10,20,30]
# print(l)
# print(id(l))
# l[0]=40
# print(l)
# print(id(l))

# l1=[10,20,30]
# l2=l1
# print(l1)
# print(l2)
# l1[0]=99
# print(l1)
# print(l2)
# l2[1]=88
# print(l1)
# print(l2)

# *37
# collection related data types are list,tuple,set,dictionary
# list
# 1.order preserved
# 2.duplicate value are allowed
# 3.value is present inside []
# 4.Hetrogenous object are allowed
# 5.indexing and slicing concept are allowed
# 6.growable in nature
# 7.list is mutable
# l=[10,20,30]
# print(type(l))
# print(l)
# print(l[0])
# l.append(40)
# print(l)
# l.remove(30)
# print(l)

# *38
# tuple:tuple is exactly same as list except that it is immutable
# t=(10,20,30)
# print(type(t))
# print(t)
# print(t[1])
# print(t[0:2])

# difference between list and tuple
#    list                     |        tuple
# 1.mutable                   |     1.immutable 
# 2.[]                        |     2.()
# 3.more memory               |     3.less memory
# 4.performnce is less        |     4.performance is more

# *39
# set:
# 1.duplicate are not allowed.
# 2.order not required.
# 3.indexing and slicing are not allowed.
# 4.hetrogenious object are allowed.
# 5.growable and mutable
# s={10,20,30,20,40,30}
# print(type(s))
# print(s)
# s.add(80)
# print(s)
# s.remove(20)
# print(s)

# q={}
# print(type(q))
# q=set()
# print(type(q))

# difference between set and list:
#   list                       |   set
# 1.order is applicable        |   1.order is not applicable
# 2.duplicate are allowed      |   2.duplicate are not allowed
# 3.[]                         |   3.{}

# *40
# frozen set:it is immutable
# s={10,20,30}
# l=frozenset(s)
# print(type(l))
# print(l)

# *41
# dict:
# 1.key-value pairs
# 2.duplicate key not allowed but duplicate value is allowed
# 3.order not applicable
# 4.hetroginious object
# 5.mutable
# 6.slicing and indexing not allowed
# d={1:'jnana',2:'ranjan'}
# print(type(d))
# print(d)

# e={}
# e[100]='jnna'
# e[200]='pra'
# print(type(e))
# print(e)
# e[100]='mitu'
# print(e)

# *42
# range:
# 1.it is immutable
# 2.indexing,slicing,ordering is allowed
# s=range(10)
# print(type(s))
# print(s)
# for i in s:
#     print(i)

# b=range(20,30)
# for i in b:
#     print(i)

# c=range(20,40,5)
# for i in c:
#     print(i)

# d=range(20,0,-2)
# for i in d:
#     print(i)
    
# print(d[0])
# print(d[-1])

# *43
# bytes:
# 1.it  contain value only from 0 to 255
# 2.it is immutable
# s=[10,20,30]
# l=bytes(s)
# print(type(l))
# for i in l:
#     print(i)
# bytesarray:
# 2.it  contain value only from 0 to 255
# 1.it is mutable
# l=[10,20,30]
# s=bytearray(l)
# print(type(s))
# print(s[0])
# s[0]=40
# for i in s:
#     print(i)

# *45
# None data type:
# a=None
# print(type(a))
# print(id(a))

# *48(arithmatic operator)
# +(addition),-(substraction),*(multiplication),/(division operator),%(modulo operator),//(floor division operator),**(exponential operator or power operator)
# a=20
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a//b)
# print(a**2)
# a=40.0
# b=5
# print(a/b)
# print(a//b)
# print(10//3)
# print(10.0//3)
# print('jnana'+'tamana')
# *if add two variable ,the two variable must be same type
# print(50+50)
# print('jnana'+'10')
# print('jnana'+str(10))
# print('jnana'*3)
# print(3*'jnana')
# print('jnana'*'ranjan') //provide type error
# print('jnana'*'3') //provide type error
# print('jnana'*int('3'))

# *if we division by zero in any number ,provide zero divisionerror
# print(10/0)
# print(10.0/0)
# print(10//0)
# print(10.0//0)
# print(10%0)
# print('jnana'*True)
# print('jnana'*False)


# *51(relational operator(>,>=,<,<=))
# a=10
# b=20
# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)

# *ord() =>is used for find the unicode of character
# print(ord('a'))
# print(ord('A'))
# print(ord('b'))
# print(ord('B'))

# *chr() =>is used for find the chracter from the the number
# print(chr(97))
# print(chr(98))
# print(chr(65))
# print(chr(68))

# s1='bayani'
# s2='tamana'
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)

# s1='bayani'
# s2='bayani'
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)

# s1='tamana'
# s2='Tamana'
# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>=s2)

# print(True>False)
# print(True>=False)
# print(True<False)
# print(True<=False)

# *if we  are using comparision operator in different datatype provide Typeerror
# print(10<'jnana')

# a=10
# b=20
# if a>b:
#     print('a is greater than b')
# else:
#     print('a is not greater than b')

# *if all comparision is true then true if one is false then false
# print(10<20)
# print(10<20<30)
# print(10<20<30<40)
# print(10<20<30<40>50)

# *53(equality operator(==,!=))
# print(10==20)
# print(10!=20)
# print(1==True)
# print(10==10.0)
# print('jnana'=='jnana')

# *== operator is not usefull for different datatype.must usefull for same data type.
# print(10=='jnana')
# print(10=='10')

# *if all comparision is true then true if one is false then false
# print(10==20==30==40)
# print(10==10==10==10)

# difference between is and ==
# == operator meant for content comparision and is operator meant for reference comparision(address comparision)
# a=[10,20,30]
# b=[10,20,30]
# print(id(a))
# print(id(b))
# print(a is b)
# print(a==b)
# c=a
# print(a is c)

# *54(logical operator(and(*),or(+),not(!)))
# username=input('enter user name :')
# password=input('enter password :')
# if username=="jnana" and password=="tamana":
#     print("valid user")
# else:
#     print("invalid user")

# *0 means False
# *non-zero means True
# *empty string,empty list,empty tuple,empty set,empty dict -->false

# imp *if x and y are both non boolean type result x or y
# x and y --> result is x or y but not boolean type
# if x evaluates to false ,then result is x
# if x evaluates to true ,then result is y
# print(10 and  20)
# print(0 and  20)
# print('jnana' and  'tamana')
# print('' and 'tamana')


# imp *if x or y are both non boolean type result x or y
# x or y --> result is x or y but not boolean type
# if x evaluates to true ,then result is x
# if x evaluates to false ,then result is y
# print(10 or 20)
# print(0 or 20)
# print([] or 20)
# print('jnana' or 'tamana')
# print('' or 'tamana')

#imp * not for noboolean type then result is always boolean
# print(not 10)
# print(not [])
# print(not 'jnana')
# print(not '')
# print(not 0)

# *56 *bitwise operator
# bitwise and(&),bitwise OR(|),bitwise X-OR(^),bitwise compliment operator(~),bitwise leftshift(<<),bitwise rightshift(>>)
# bitwise operator is applicable for int and boolean datatype
# &  -->if both bits are 1 then result is 1 otherwise 0
# 1 & 1 =1
# 1 & 0 =0
# 0 & 1 =0
# 0 & 0 =0

# | -->if atleast one bit is 1 then result is 1 otherwise result is 0
# 1 | 1 =1
# 1 | 0 =1
# 0 | 1 =1
# 0 | 0 =0

# ^ -->if both bits are different then result is 1 otherwise result is 0
# 1 ^ 1 =0
# 1 ^ 0 =1
# 0 ^ 1 =1
# 0 ^ 0 =0

# print(4 & 5)
# print(4 | 5)
# print(4 ^ 5)

# in bitwise compliment operator '1' is converted to '0' and '0' is converted to '1'
# ~1=0
# ~0=1
# print(~4)
# print(~5)

# The most significanr bit(MSB) acts as sign bit
# 0  -->+ve number
# 1  -->-ve number
# +ve number will be represent  directly in the memory
# -ve number will be represent in 2's compliment form
# in 1's compliment-->1 converted to 0 and 0 converted to 1
# in 2's compliment =>1's compliment+1
# print(~4)
# print(~-4)

# *59(shift operator)
# <<(left shift) -->in that case two space fillup with 0 in left side
# >>(right shift) -->in that case two space fillup with on sighbit,in case positive to add o,if negative add 1 in right side
# print(10<<2)
# print(10>>2)

# *assignment operator
# x=10
# x+=20//x=x+20
# print(x)
# x=10
# += -->x=x+10
# -= -->x=x-10
# *= -->x=x*10
# /=  -->x=x/10
# %=  -->x=x%10
# //= -->x=x//10
# **=  -->x=x**10
# &=  -->x=x&10
# |=  -->x=x|10
# ^=  -->x=x^10
# >>=  -->x=x>>10
# <<=  -->x=x<<10
# x=10
# x&=5
# print(x)
# x=10
# x**=2
# print(x)
# x=10
# print(+x)
# print(+++x)
# print(++++++x)
# print(-x)
# print(--x)
# print(-----x)

# 61*imp*Terinary operator
# syn:first_value if condition else second_value
# if condition is True,first_value is consider else condition is false,second_value is consider
# a=10
# b=20
# c=30 if (a>b) else 40
# print(c)
# c=30 if (a<b) else 40
# print(c)

# write a program read two integer value from keyboard and print min value 
# a=int(input('enter the first number:'))
# b=int(input('enter the second number:'))
# c= a if a<b else b
# print(c)
# c=min(a,b)
# print(c)

# a=int(input('enter the first number:'))
# b=int(input('enter the second number:'))
# c=int(input('enter the third number:'))
# min= a if (a<b and a<c) else b if (b<a and b<c) else c
# print(min)
# a=int(input('enter the first number:'))
# b=int(input('enter the second number:'))
# c=int(input('enter the third number:'))
# max=a if (a>b and a>c) else b if (b>a and b>c) else c
# print(max)

# a=int(input('enter the first number:'))
# b=int(input('enter the second number:'))
# c=" Both number areEqual" if a==b else " First number is Smaller than second number" if (a<b) else "First number is greater than second number"
# print(c)

# *63*special operator
# 1.identity operator(is,is not)
# r1 is r2 ==>True iff both references pointing to the same object 
# r1 is not r2 ==>True iff r1 and r2 are not pointing  to the same object 
# a=10
# b=10
# print(a is b)
# print(a is not b)
# a='durga'
# b='durga'
# print(a is b)
# print(a is not b)
# a=[10,20,30]
# b=[10,20,30]
# print(a is b)
# print(a is not b)
# 2.membership operator(in, not in)
# a=[10,20,30,40,50]
# print(10 in a)
# print(600 in a)
# print(10 not in a)
# print(600 not in a)
# a="python is very easy to learn"
# print('s' in a)
# print('easy' in a)
# print('s' not in a)
# print('d' not in a)

# *64*operator precedence
# print(10+2*3)
# print((10+2)*3)

# () ==>parenthesis
# **  ==>exponential operator
# ~,-  ==>bitwise compliment operator and uninary minus operator
# *,/,%,//  ==>multiplication,division,modulo,floor division
# +,-  ==>addition,substraction
# <<,>>  ==>left shift,right shift
# &  ==>bitwise and
# ^  ==>bitwise x-or
# !  ==>bitwise or
# >,>=,<,<=,==,!=   ==>relational or comparision operator
# =,+=,-=,*= .... ==>assignment operator
# is,is not ==>identity operator
# in,not in ==>membership operator
# not  =>logical not
# and  ==>logical and
# or   ==>logical or
# a=30
# b=20
# c=10
# d=5
# print((a+b)*c/d)
# print((a+b)*(c/d))
# print(a+(b*c)/d)
# print(3/2*4+3+(10/5)**3-2)

# *65*python module
# module is a python which is colllection of variable,function,class etc.
# the advance of module is code reuseability 
# import dt
# dt.add(5,5)
# dt.mul(5,5)
# from math import *
# r=int(input("enter the value :"))
# # print("the area is:",pi*r**2)
# print("the area is:",pi*pow(r,2))
# import math
# print(dir(math))
# what is difference between dir() and help()
# dir() Returns the all functions that are available in particular Module
# help() Gives the information about the function in that particular Module
# import math
# print(dir(math))
# help(math.pow)
# print(math.sqrt(16))
# print(math.pi)
# print(math.e)
# print(math.floor(3.9))
# print(math.ceil(3.9))
# print(math.pow(3,2))
# import math as m
# print(m.sqrt(16))
# print(m.pi)
# print(m.e)
# print(m.floor(3.9))
# print(m.ceil(3.9))
# print(m.pow(3,2))
# from math import *
# print(sqrt(16))
# print(pi)
# print(e)
# from math import sqrt as s
# print(s(16))

# unit-3
# difference between raw_input() and input()
# the return type of raw_input is always string, while the return type of input need not be string only
# x=input("enter the number:")
# print(x,type(x))

# wrp take input from keyboard to perform addition
# x=int(input("enter the number:"))
# y=int(input("enter the number:"))
# print("the sum is:",x+y)
# print("the sum is:",int(input("enter the first number:"))+int(input("enter the second number:")))

# wrp to read employe data from the keyboard and print the data
# Eno=int(input('Enter the employe number:'))
# Ename=input("Enter the employe name:")
# Esal=float(input('enter the employe salary:'))
# Eadd=input("enter the employe address:")
# Emarried=eval(input("Employe is married or not married(True/False) :"))
# print("please conform your provided information ")
# print("Enter the employe number:",Eno)
# print("the employe name:",Ename)
# print("the employe salary:",Esal)
# print("the employe address:",Eadd)
# print("Employe married:",Emarried)

# *71*how to read multiple value from keyboard in a single line
# a,b=[int(x) for x in input("enter two number:").split(",") ]
# print("The sum of number is:",a+b)

# *wap to read 3 float value from the keyboard with comma separation and print the sum
# a,b,c=[float(x) for x in input("enter the three float value:").split(",")]
# print("The sum of number is:",a+b+c)

# *72*eval()  ==>The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed
# x=eval(input("Enter something:"))
# print(x,type(x))

# *73*command line arguments  ==>Python Command line arguments are input parameters passed to the script when executing them
# from sys import argv
# print(type(argv))
# print(argv[0])
# print(argv[1])
# print(type(argv[1]))

# wap to print command line argument information
# from sys import argv
# print("The number of command line arguments are:",len(argv))
# print("The list of command line arguments are:",argv)
# print("The command line arguments one by one:")
# for x in argv:
#        print(x)

# wap to print sum of given numbers provided as command line arguments:
# from sys import argv
# arg=argv[1:]
# sum=0
# for x in arg:
#     sum=sum+int(x)
# print("The sum is:",sum)

# *The main objective of command line arguments is we can customise behaviour of application based on our provided value,our appllication will work.
# *Python exposes a mechanism to capture and extract your Python command line arguments. These values can be used to modify the behavior of a
#  program. For example, if your program processes data read from a file, then you can pass the name of the file to your program, rather than
#   hard-coding the value in your source code*
# from sys import argv
# f1=open(argv[1])
# f2=open(argv[2])
# f3=open(argv[3],"w")
# for x in f1:
#     f3.write(x)
# for x in f2:
#     f3.write(x)

# *in command line argument space is the 1st argument,2nd argument,3rd argument etc. 
# ex:jnana tamana bayani
# if we use double quotes("") is taken one argument
# ex:"tamana bhuya"
# from sys import argv
# print(argv[1])

# from sys import argv
# print(argv[1]+argv[2])
# print(int(argv[1])+int(argv[2]))

# from sys import argv
# f1=open(argv[100])


# *75*output statement
# 1.print() without an argument:provide a next line(\n)
# print("jnana")
# print()
# print("tamana")
# 2.print(string)
# print('jnana')
# print("jnana\ntamana")
# print('jnana\ttamana')
# print('jnana'+'tamana')
# print(10*'tamana')
# 3.print() with various types of arguments
# a,b,c=10,20,30
# print("value are:",a,b,c)
# 4.sep attribute with print statement
# a,b,c,d=10,20,30,40
# print(a,b,c,d,sep=":")
# 5.end attribute with print statement
# print("jnana",end='')
# print("tamana",end='')
# print("jnana")

# print("jnana",end='::')
# print("tamana",end='$$')
# print("jnana")

# both sep attribute and end attribute
# print(10,20,30,sep='::',end="$$")
# print(40,50,60,sep='@@',end='==')
# print(70,80,90,sep='--')

# print(10,20,30,sep='::',end="$$")
# print(40,50,60,sep='@@',end='==')
# print(70,80,90)

# print("jnana"+"tamana")
# print('jnana','tamana')

# *6*print(object)
# l=[10,20,30,40]
# print(l)
# print(type(l))

# s=(10,20,30,40)
# print(s)
# print(type(s))

# *7 print() with replacement operator
# name='jnana'
# salary=300000
# gf='tamana'
# print('my name is {} and my salary is per month {} and my loveable gf is {}'.format(name,salary,gf))
# print('my name is {n} and my salary is per month {s} and my loveable gf is {g}'.format(n=name,s=salary,g=gf))

# *8*print() with formatted string
# %i ==>signed decimal value
# %d ==>signed decimal value
# %f ==>float Value
# %s ==>string value,any other objects like list,set etc....
# syn:print("formatted string" %(variable list))
# a=10
# print("a value is: %i" %a)
# a=10
# b=20
# c=30
# print('a=%d,b=%d,c=%d' %(a,b,c))

# name='jnana'
# mark=[100,200,300]
# print('my name is %s and my mark is %s' %(name,mark))

# price=50.23545
# print("my price is {}".format(price))
# print('my price is %f' %price)
# print('my price is %.2f' %price)
# print(f'the price is {price}')
# name='jnana'
# salary=300000
# gf='tamana(bayani)'
# print(f'My name is{name} ,my salary is{salary} and my beautiful wife is {gf}')

# ****To get the ASCII value****
# print(ord("A"))
# c = input ("enter the letter:")
# print ("the ascii value is", ord (c ))


# ********************************************************************************************************************************
                                                          # python flow control
# ********************************************************************************************************************************
# flow control has three parts
# 1.selection statement(if,if..else,if..elif..else,if..elif)
# 2.iterative statement/group of statement(for,while)
# 3.transfer statement(break,continue,pass)
# name=input("enter your name:")
# if name=="jnana":
#     print("This is correct guy")
# print("Tamana is a good girl")

# name=input("enter your name:")
# if name=="jnana":
#     print("This is correct guy")
# else:
#     print("My beautiful wife is Tamana ")
# print("Tamana is a good girl")

# name=input("Enter your Beautiful wife name:")
# if name=="Tamana":
#     print("This is my Future wife name")
# elif name=="Bayani":
#     print("This name is my Future wife surname")
# elif name=="rubi":
#     print("This is my first gf name")
# elif name=="Barsha":
#     print("This is my first cross gf")
# elif name=="gudi":
#     print("This is my village gf")
# elif name=="lizy":
#     print("This girl is my +2 cross")
# else:
#     print("This is not my Gf")

# *wap to find biggest of 2 given number.
# a=int(input("Enter the first number:"))
# b=int(input("Enter the Second number:"))
# if a>b:
#     print(f"a is greater than b and the number is {a}")
# else:
#     print(f"a is smaller than b and the number is {a}")


# a=int(input("Enter the first number:"))
# b=int(input("Enter the Second number:"))
# print(a if a>b else b)

# *wap to find biggest of 3 given number.
# a=int(input("Enter the first number:"))
# b=int(input("Enter the Second number:"))
# c=int(input("Enter the Second number:"))
# if a>b and a>c:
#     print(f"a is greater than other,the number is {a}")
# elif b>a and b>c:
#     print(f"b is greater than other,the number is  {b}")
# else:
#     print(f"c is greater than other,the number is {c}")


# a=int(input("Enter the first number:"))
# b=int(input("Enter the Second number:"))
# c=int(input("Enter the Second number:"))
# print(a if(a>b and a>c) else b if (b>a and b>c) else c)


# *wap to check wheater the given number is in between 1 and 100 or not
# a=int(input("Enter the number:")) 
# if (a>=1 and a<=100):
#     print(f"Number is present in betwwen 1 to 100, the number is {a}")
# else:
#     print(f"The number is not present in between 1 to 100, the number is {a}")


# a=int(input("Enter the number:")) 
# print(a if (a>=1 and a<=100) else a)


# *wap to take a single digit number from the keyboard and print its value in english word.
# a=input("Enter the number:")
# if a=="0":
#     print("Zero")
# elif a=="1":
#     print("one")
# elif a=="2":
#     print("Two")
# elif a=="3":
#     print("Three")
# elif a=="4":
#     print("Four")
# elif a=="5":
#     print("Five")
# elif a=="6":
#     print("Six")
# elif a=="7":
#     print("Seven")
# elif a=="8":
#     print("Eight")
# elif a=="9":
#     print("Nine")
# else:
#     print("Please enter the digit in between from 0 to 1")


# list=['zero','one','Two','Three','Four','Five','Six','Seven','Eight']
# a=int(input("Enter the number:"))
# print(list[a])

# a=int(input("Enter the number:"))
# print("one" if (a==1) else "Two" if (a==2) else "Three" if (a==3) else "Four" if (a==4) else "Five" if (a==5) else "six" if (a==6) else "Seven" if (a==7) else "Eight" if (a==8) else "Nine" if (a==9) else "Please enter the number between 0 to 9")

# *wap to take a  digit number from the keyboard to 1 to 99 and print its value in english word
# words_upto_19=['','one','Two','Three','Four','Five','Six','Seven','Eight','nine','Ten','Eleven','Twelve','Thirteen','Fourteen','fifteen','sixteen','seventeen','Eighteen','Ninteen']
# words_for_tens=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
# a=int(input("Enter the number:"))
# output=''
# if a==0:
#     print('Zero')
# elif a<=19:
#     output=words_upto_19[a]
# elif  (a>=20) and (a<=99):
#     output=words_for_tens[a//10]+''+words_upto_19[a%10]
# else:
#     output="Please enter in between 1 to 99"
# print(output)



# *wap to take a  digit number from the keyboard to 1 to 999 and print its value in english word
# words_upto_19=['','one','Two','Three','Four','Five','Six','Seven','Eight','nine','Ten','Eleven','Twelve','Thirteen','Fourteen','fifteen','sixteen','seventeen','Eighteen','Ninteen']
# words_for_tens=['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
# word_upto_99=['','','','one hundrend','two hundrend','three hundrend','four hundrend','five hundrend','six hundrend','seven hundrend','eight hundrend','nine hundrend']
# a=int(input("Enter the number:"))
# output=''
# if a==0:
#     print('Zero')
# elif a<=19:
#     output=words_upto_19[a]
# elif  (a>=20) and (a<=99):
#     output=words_for_tens[a//10]+''+words_upto_19[a%10]
# elif (a>=100) and (a<=1000):
#     if (a%100)<=19:
#         output=word_upto_99[a//100]+''+words_upto_19[a%100]
    # else (a%100>)>=20:
    #     output=word_upto_99[a//100]+''+words_for_tens[a%100]
# else:
#     output="Please enter in between 1 to 99"
# print(output)


# s='Tamana Bhuyan'
# for x in s:
#     print(x)

# s='Tamana Bhuyan'
# i=0
# for x in s:
#     print(f'The character present at {i} index {x}')
#     i=i+1

# s=input("Enter your name:")
# i=0
# for x in s:
#     print(f'The character present at {i} index {x}')
#     i=i+1

# s=input("Enter your future wife name is:")
# for x in range(5):
#     print(f'Tamana {x} times {s}')

# for x in range(1,11):
#     print(x)

# *to display odd number from 0 to 20.
# for x in range(21):
#     if x%2!=0:
#         print(x)

# for x in range(1,21,2):
#     print(x)

# *to display even number from 0 to 20.
# for x in range(21):
#     if x%2==0:
#         print(x)

# for x in range(0,21,2):
#     print(x)

# *To display number from 10 to 1 in decending order
# for x in range(10,0,-1):
#     print(x)


# To print the sum of numbers in the given list. 
# list=eval(input("Enter list of number:"))
# sum=0
# for x in list:
#     sum=sum+x
# print('The sum is:',sum)

# list=input("Enter  number:").split(',')
# sum=0
# for x in list:
#     sum=sum+int(x)
# print('The sum is:',sum)

# list=input("Enter  number:").split(',')
# sum=0
# for x in list:
#     y=int(x)
#     if y%2==0:
#       sum=sum+y
# print('The sum is:',sum)

# list=input("Enter  number:").split(',')
# sum=0
# for x in list:
#     y=int(x)
#     if y%2!=0:
#       sum=sum+y
# print('The sum is:',sum)

# list=eval(input("Enter list of number:"))
# print(sum(list))

#*imp* if we want  to exicute group of statement then we use for loop
# *imp* if we want  to exicute group of statement as long as some condition then we use while loop
# i=1
# while i<=10:
#     print("Hello,this is my while loop")
#     i=i+1

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# To print 1 to 20 which are divisiable by 3
# i=1
# while i<=20:
#     if i%3==0:
#         print(i)
#     i=i+1

# wap a program to display sum of first n numbers
# n=int(input("Enter the number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# name=''
# while name!='Tamana':
#     name=input("Enter your wife name:")
# print("This is my beautiful wife")

# i=1
# while True:
#     print("hello", i)
#     i=i+1


# i=1
# while True:
#     print("hello", i)
#     i=i+1
#     if i==10:
#         break

# nested loops:loops inside another loop
# for i in range(3):
#     for j in range(2):
#         print("Hello")

# for i in range(3):
#     for j in range(2):
#         print(f"i is {i} and j is {j}")


# *pattern prograam*
# n=int(input("Enter the number:"))
# for i in range(n):
#     print('*')

# n=int(input("Enter the number:"))
# for i in range(n):
#     print('*',end=' ')

# n=int(input("Enter the number:"))
# for i in range(n):
#     print('* '*n)

# n=int(input("Enter the number:"))
# for i in range(n):
#     print(i)
#     print((str(i+1)+' ')*n)


# n=int(input("Enter the number:"))
# for i in range(n):
#     print((str(i+1)+' ')*n)

# n=int(input("Enter the number:"))
# for i in range(n):
#     print((chr(65+i)+' ')*n)

# n=int(input("Enter the number:"))
# for i in range(n):
#     print((chr(97+i)+' ')*n)
   

# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print('x',end=' ')
#     print()

# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j),end=' ')
#     print()

# n=int(input("Enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i),end=' ')
#     print()

# n=int(input("Enter the number:"))
# for i in range(n):
#     print('x '*(n-i))

# n=int(input("Enter the number:"))
# for i in range(n):
#     print(' '*(n-i-1)+'x '*(i+1))

# n=int(input("Enter the number:"))
# for i in range(n):
#     print(' '*(i)+'x '*(n-i))


# n=int(input("Enter the number:"))
# for i in range(n):
#     print(' '*(n-i-1)+'x '*(i+1))
# for i in range(n-1):
#     print(' '*(i+1)+'x '*(n-i-1))


#print(10  or 5)
# print(~(-12))
# print(10<<3)
# **************************************************************************************************************************************
#                               PYTHON FLOW CONTROL-2
#***************************************************************************************************************************************
# for i in range(1,20):
#     if i==15:
#         print("please break the processing")
#         break
#     print(i)
# print("outside the loop") 
# 
# 
# l=[10,30,50,40,70,40,100,90,65]  
# for i in l:
#     if i>60:
#         print("processing item is complite {}".format(i))
#         break
#     print("This is your item {}".format(i)) 

# if you use break statement then you must use for loop or while loop.otherwise syntaxerror is coming(SyntaxError: 'break' outside loop).
# x=10
# if x>20:
#     print("complite the task")
#     break
# print("continue")

# wap to print both even and odd number using continue statement
# for i in range(30):
#     if i%2 !=0:
#         print("This is odd number :{}".format(i))
#         continue
#     print("The even number is:{}".format(i))

# l=[20,10,30,50,30,100,40,60,80,500,50,300,500,90]
# for i in l:
#     if i>=100:
#         print("You enter the {} value are greater than 100".format(i))
#         continue
#     print("The value is {} less than 100 ".format(i))

# check the number which is not divisible by 100
# l=[10,20,25,0,40,0,50,3,0,5]
# for i in l:
#     if i==0:
#         print("{} is not divisible by any number it gives the error".format(i))
#         continue
#     print("100/{}={}".format(i,100//i))

# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print("The value if  i={} and the value of j={} are equal".format(i,j))
#             break
#         print("{} {}".format(i,j))

# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print("The value if  i={} and the value of j={} are equal".format(i,j))
#             continue
#         print("{} {}".format(i,j))

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# print(a if a>b else b)

# a=int(input("enter the number:"))
# b=int(input("enter the number:")) 
# c=int(input("enter the number:"))
# print(a if (a>b>c) else b if (b>c) else c if (c>a) and (c>=b)  else "equal")
# print(a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if (c>a) and (c>b) else "all are equal")

# a=int(input("enter the number:"))
# b=int(input("enter the number:")) 
# print(a if a>b else b if b>a else "Equal")


# a=float(input("Enter the first number:"))
# b=float(input("Enter the second number:"))
# c=float(input("Enter the third number:"))
# if (a<0):
#     if (b>c):
#       print("{} is the bigger number".format(b))
#     elif(b<c):
#       print("{} is the bigger number".format(c))
#     else:
#         print("Both are equal")
# elif (b<0):
#     if (a>c):
#       print("{} is the bigger number".format(a))
#     elif(a<c):
#       print("{} is the bigger number".format(c))
#     else:
#         print("Both are equal")
# elif (c<0):
#     if (a>b):
#       print("{} is the bigger number".format(a))
#     elif(a<b):
#       print("{} is the bigger number".format(b))
#     else:
#         print("Both are equal")
# elif (b<=a>c):
#     print(f"{a} is bigger number")
# elif (a<b>=c):
#     print(f"{b} is bigger number")
# elif (a<=c>b):
#     print(f"{c} is bigger number")
# else:
#     print(f"{a},{b},{c} are equal")


#check given number is prime or not
# n=int(input("enter the number:"))
# p="prime"
# for i in range(2,n):
#     if (n%i==0):
#         p="not prime"
#         break
# if p=="prime":
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")


#write a python program to generate prime number which is less than or equal to the given number
# while(True):
#     n=int(input("Enter the number:"))
#     if n>=2:
#         break
#     else:
#         print("enter the valid input ")
# p="prime"
# for i in range(2,n):
#     if (n%i==0):
#         p="not prime"
#         break
# if p=="prime":
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not prime")


#generate prime number:
# while(True):
#     n=int(input("enter the number:"))
#     if n>=2:
#         break
#     else:
#         print("enter tne valid input")
# for i in range(2,n):
#     p="prime"
#     for j in range(2,i):
#         if (i%j==0):
#             p="not prime"
#             break
#     if(p=="prime"):
#         print(i)


# while(True):
#     n=int(input("Enter the number:"))
#     if(n>=2):
#         break
#     else:
#         print("enter the valid number")
# p="prime"
# for i in range(2,n//2+1):
#     if(n%i==0):
#         p="not prime"
#         break
# if p=="prime":
#         print(f"{n} is a prime number")
# else:
#         print(f"{n} is not a prime number")


n=int(input("Enter the number:"))
n1=2
while n1<=n:
    p="prime"
    for i in range(2,n1):
        if (n1%i==0):
            p="not prime"
            break
    if p=="prime":
        print(f"{n1} is a prime number")
    n1=n1+1
else:
    print("invalid number")






    
