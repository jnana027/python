# from math import *
# import math 
# import calendar
# print(calendar.month(2022,10))
# calendar.calendar(2022)
# print(math.factorial(4))



# *********************************************************************************************************************************************
# ****Datatypes****
# 1.fundamental datatypes(int,floot,bool,complex)
# a=10
# print(a,type(a))
# a=-123
# print(a,type(a))
# sno=345
# print(sno,type(sno))
# bal=-456
# print(bal,type(bal))
# a=10
# b=20
# print(a,type(a))
# print(b,type(b))
# c=a+b
# print(c,type(c))
# a=0b1010
# print(a,type(a))
# a=0B11111
# print(a,type(a))
# a=10
# print(bin(a))
# a=300
# print(bin(a))
# a=0o34
# print(a)
# a=28
# print(oct(a))
# a=0o34
# print(bin(a))
# a=0o10
# print(bin(a))
# a=0b1000
# print(oct(a))

# a=24
# print(bin(a))
# a=0b11000
# print(a)
# a=24
# print(oct(a))
# a=0b11000
# print(oct(a))
# a=0o30
# print(bin(a))


# Binary to Decimal number
# a=0b11000
# print(a)

# b=0b0101
# print(b)

# c=0B01111
# print(c)

# Decimal to Binary number
# a=5
# print(bin(a))

# b=63
# print(bin(b))

# b=44
# print(bin(b))

# Octal to Decimal number
# a=0o30
# print(a)

# b=0O734
# print(b)

# b=0O63456
# print(b)

# Decimal number to Octal
# a=24
# print(oct(a))

# a=356
# print(oct(a))

# a=4230
# print(oct(a))

# Hexa Decimal to Decimal
# a=0xAC
# print(a)

# a=0xac
# print(a)


# a=0x9bd
# print(a)

# a=0x84EF5
# print(a)

# Decimal to Hexa Decimal
# a=1584 
# print(hex(a))

# a=84 
# print(hex(a))

# a=95
# print(hex(a))

# **********************************************************************************************************************************************
# list data type :

# l1=[10,20,30,10,20,34.56,0.99]
# print(l1,type(l1),id(l1))              #[10, 20, 30, 10, 20, 34.56, 0.99] <class 'list'> 3088611884800
# print(len(l1))                         # 7

# l2=[10,20,30,40,345,1000]
# print(l2,type(l2),id(l2))              #[10, 20, 30, 40, 345, 1000] <class 'list'> 2144197885696
# print(len(l2))                         # 6

# l3=[10,"Samir",34.56,True,2+3j]           
# print(l3,type(l3),id(l3))                 #[10, 'Samir', 34.56, True, (2+3j)] <class 'list'> 1564028976896
# print(len(l3))                            # 5
# print(l3[0])                              #10
# print(l3[-1])                             #(2+3j)
# l3[0]=100                                 #Update the list Elements
# print(l3)                                 #[100, 'Samir', 34.56, True, (2+3j)]
# print(l3,type(l3),id(l3))                 #[100, 'Samir', 34.56, True, (2+3j)] <class 'list'> 2492737142528
# print(l3[0:3])                            #[100, 'Samir', 34.56]
# print(l3[::-1])                           #[(2+3j), True, 34.56, 'Samir', 100]
# print(l3[::2])                            #[100, 34.56, (2+3j)]
# print(l3[1][::2])                         #Smr
# print(l3[1])                                #Samir
# print(l3[1][::-1])                          #rimaS

# l1=[100,"Rossum",34.56]
# print(l1,type(l1),id(l1),len(l1))          #[100, 'Rossum', 34.56] <class 'list'> 2935710367488 3

# l2=[]                                      #empty list
# print(l2,type(l2),len(l2),id(l2))          #[] <class 'list'> 0 2610616337472

# l3=list()
# print(l3,type(l3),len(l3),id(l3))            #[] <class 'list'> 0 2580088990720

# s="python"
# print(s,type(s),len(s))                   #python <class 'str'> 6
# l=list(s)
# print(l,type(l),len(l))                   #['p', 'y', 't', 'h', 'o', 'n'] <class 'list'> 6



# l1=[10,20,30,40,50,60,40,20,40,30,20,40]
# s=bytearray(l1)
# print(s,type(s))                                 #bytearray(b'\n\x14\x1e(2<(\x14(\x1e\x14(') <class 'bytearray'>
# l2=list(s)
# print(l2,type(l2))                                 #[10, 20, 30, 40, 50, 60, 40, 20, 40, 30, 20, 40] <class 'list'>


# *****append=This Function is used for Adding the value at the end of list object*****
# l1=[10,'Rossum']
# print(l1,type(l1),len(l1),id(l1))              #[10, 'Rossum'] <class 'list'> 2 1597268508416
# l1.append(34.56)
# l1.append("jnana")
# print(l1,type(l1),len(l1),id(l1))              #[10, 'Rossum', 34.56, 'jnana'] <class 'list'> 4 1597268508416


# l1=[]
# print(l1,type(l1),len(l1),id(l1))              #[] <class 'list'> 0 2898314411776
# l1.append(10)
# l1.append("bayani")
# l1.append("tamana")
# print(l1,type(l1),len(l1),id(l1))              #[10, 'bayani', 'tamana'] <class 'list'> 3 2898314411776


# l1=list()
# print(l1,type(l1),len(l1),id(l1))               #[] <class 'list'> 0 1874437778496
# l1.append(30)
# l1.append("append")
# print(l1,type(l1),len(l1),id(l1))               #[30, 'append'] <class 'list'> 2 1874437778496


# *****insert=This Function is used for adding the value at specified Index******
# l1=[10,40,"jnana"]
# print(l1,type(l1),len(l1),id(l1))             # [10, 40, 'jnana'] <class 'list'> 3 1763888021248
# l1.insert(2,"bayani")
# l1.insert(1,"mitu")
# print(l1,type(l1),len(l1),id(l1))              #[10, 'mitu', 40, 'bayani', 'jnana'] <class 'list'> 5 1763888021248
# l1.insert(30,"pradhan")
# l1.insert(100,"Bhuyan")
# print(l1,type(l1),len(l1),id(l1))            #[10, 'mitu', 40, 'bayani', 'jnana', 'pradhan', 'Bhuyan'] <class 'list'> 7 1763888021248


# *****remove=This Function is used for remvoing the First Occurence of the specified value from list object****
# l1=[10,20,30,20,10,30,20,10,"python",'jnana','bayani']
# print(l1,type(l1),len(l1),id(l1))               #[10, 20, 30, 20, 10, 30, 20, 10, 'python', 'jnana', 'bayani'] <class 'list'> 11 2425360170752
# l1.remove(10)
# print(l1,type(l1),len(l1),id(l1))               #[20, 30, 20, 10, 30, 20, 10, 'python', 'jnana', 'bayani'] <class 'list'> 10 2425360170752
# l1.remove(10)
# print(l1,type(l1),len(l1),id(l1))              #[20, 30, 20, 30, 20, 10, 'python', 'jnana', 'bayani'] <class 'list'> 9 2425360170752 
# l1.remove("python")
# print(l1,type(l1),len(l1),id(l1))                #[20, 30, 20, 30, 20, 10, 'jnana', 'bayani'] <class 'list'> 8 2425360170752 
# l1.remove("python")
# print(l1,type(l1),len(l1),id(l1))                   # ValueError: list.remove(x): x not in list



# ****pop(index)=This Function is used for removing the value from List object based on Index****
# l1=[10,"Rossum",45.67,True,3+4.5j]
# print(l1,type(l1))                              #[10, 'Rossum', 45.67, True, (3+4.5j)] <class 'list'>
# l1.append(10)
# print(l1,type(l1))                              #[10, 'Rossum', 45.67, True, (3+4.5j), 10] <class 'list'>
# print(l1.pop(-1))                               #10
# print(l1,type(l1))                              #[10, 'Rossum', 45.67, True, (3+4.5j)] <class 'list'>
# print(l1.pop(0))                                #10
# print(l1,type(l1))                              #['Rossum', 45.67, True, (3+4.5j)] <class 'list'>
# print(l1.pop(0))                                #Rossum
# print(l1,type(l1))                              #[45.67, True, (3+4.5j)] <class 'list'>
# print(l1.pop(-2))                               #True
# print(l1)                                       #[45.67, (3+4.5j)]
# print(l1.pop(0))                                #45.67
# print(l1)                                      #[(3+4.5j)]
# print(l1.pop(0))                               #(3+4.5j)
# print(l1,type(l1))                             #[] <class 'list'>
# print(l1.pop(0))                               #IndexError: pop from empty list
# print(list().pop(0))                          #IndexError: pop from empty list
# print([].pop(-1))                              #IndexError: pop from empty list
# print([10,20,30,40].pop(0))#10
# print([10,20,30,40].pop(10))#IndexError: pop index out of range


# ***pop()=This Function is used for remvoing last element***
# l1=[10,"Rossum",45.67,True,3+4.5j]
# print(l1,type(l1))                         #[10, 'Rossum', 45.67, True, (3+4.5j)] <class 'list'>
# print(l1.pop())                            #(3+4.5j)
# print(l1)                                  #[10, 'Rossum', 45.67, True]
# print(l1.pop())                            #True
# print(l1)                                  #[10, 'Rossum', 45.67]
# print(l1.pop())                            #45.67
# print(l1)                                  #[10, 'Rossum']
# print(l1.pop())                             #Rossum
# print(l1)                                #[10]
# print(l1.pop())                            #10
# print(l1,type(l1))                         #[] <class 'list'>
# print(l1.pop()) #IndexError: pop from empty list


# ***clear=This Function is used for removing all the elements from list object and after that list object is empty***
# l1=[10,"Rossum",45.67,True,3+4.5j]
# print(l1,type(l1))#[10, 'Rossum', 45.67, True, (3+4.5j)] <class 'list'>
# l1.clear()
# print(l1,len(l1))#[] 0
# print(l1.clear())#None

# l2=[10,20,30,40]
# print(l2,len(l2),type(l2))                   #[10, 20, 30, 40] 4 <class 'list'>
# l2.clear()
# print(l2,type(l2),len(l2))                   #[] <class 'list'> 0
# x=l2.clear()
# print(x)                                     #None

# ***del operator***
# >Syntax1: del  listobj[Start:Stop]   # Slice Based removal
# =>Syntax2: del  listobj[Index]  # Index Based removal
# =>Syntax3: del  listobj	     # Object Based Removal ( Values and object removed)
# =>Syntax4: del  listobj[Start:Stop:Step]
# l1=[10,20,30,40,10,10]
# print(l1,len(l1))#[10, 20, 30, 40, 10, 10] 6
# del l1[1:4]
# print(l1,len(l1))#[10, 10, 10] 3
# del l1[-1]
# print(l1,len(l1))#[10, 10] 2
# del l1[0]
# print(l1,len(l1))#[10] 1
# del l1
# print(l1)#NameError: name 'l1' is not defined

# l1=[10,20,30,40,10,10]
# del l1[12]
# print(l1) #IndexError: list assignment index out of range

#  index()
# --------------------------------------------------------
# =>Syntax:    listobj.index(value)
# =>This Function gives First Index  of Specified Value if the value present.
# =>If Value does not exist then we get ValueError

# l1=[10,20,30,40,10,10]
# print(l1,len(l1))             #[10, 20, 30, 40, 10, 10] 6
# print(l1.index(10))           #0
# print(l1)                     #[10, 20, 30, 40, 10, 10]
# print(l1.index(30))           #2
# # print(l1.index(100))         #ValueError: 100 is not in list
# # print([].index(1))          #ValueError: 100 is not in list
# print(list().index(10))       #ValueError: 100 is not in list
# print(["Raj","Ram","Rajesh"].index("Ram"))  #1
# ["Raj","Ram","Rajesh"].index("ram")         #ValueError: 'ram' is not in list


# count()
# ------------------------------------------------
# Syntax:   listobj.count(value)
# =>This Function is used for counting number of Occurences of Specified Value from list object.
# l1=[10,20,30,40,10,10,20,30,10,"python",10]
# print(l1.count(10))            #5
# print(l1.count(20))#2
# print(l1.count(30))#2
# print(l1.count(40))#1
# print(l1.count('python'))#1
# print(l1.count('jnana'))  #0
# print(list().count(10))   #0
# print([].count(10))       #0


# copy()---Implementation  Shallow Copy
# -----------------------------------------------------------
# =>This Function is used for copying the content of one list object into another list object.
# =>Syntax:   listobj2=listobj1.copy()
# shallow copy
# l1=[10,"Rossum"]
# print(l1,id(l1))#[10, 'Rossum'] 1321756606080
# l2=l1.copy()
# print(l2,id(l2))#[10, 'Rossum'] 1321758163904
# l1.append(20)
# l2.insert(1,"python")
# print(l1,id(l1))#[10, 'Rossum', 20] 1321756606080
# print(l2,id(l2))#[10, 'python', 'Rossum'] 1321758163904

# deep copy
# l1=[10,"Rossum"]
# print(l1,id(l1))#[10, 'Rossum'] 2040133664384
# l2=l1
# print(l2,id(l2))#[10, 'Rossum'] 2040133664384
# l1.append("python")
# print(l1,id(l1))#[10, 'Rossum', 'python'] 2040133664384
# print(l2,id(l2))#[10, 'Rossum', 'python'] 2040133664384
# l2.insert(1,"jnana")
# print(l1,id(l1))#[10, 'jnana', 'Rossum', 'python'] 2040133664384
# print(l2,id(l2))#[10, 'jnana', 'Rossum', 'python'] 2040133664384

#  Slice Based Copy:
# =>In Copy Mech, We copy either all the elements of list object or part of list object into another object.
# =>Slice Based Copy always considered as Shallow Copy.
# Examples:
# l1=[10,20,30,40,50,60]
# print(l1,id(l1))#[10, 20, 30, 40, 50, 60] 2503436353152
# l2=l1[0:4]
# print(l2,id(l2))#[10, 20, 30, 40] 2503438435264
# l3=l1[::2]
# print(l3,id(l3))#[10, 30, 50] 2503438345024
# l4=l1[::]
# print(l4,id(l4))#[10, 20, 30, 40, 50, 60] 2503436352704
# l5=l1[::-1]
# print(l5)#[60, 50, 40, 30, 20, 10]

# reverse()
# ----------------------------------------------
# Syntax:-   listobj.reverse()
# =>This Function is used for obtaining reverse of given list of elements ( Front to back and 
#     back to front)
# l1=[10,"Rossum",45.67,True]
# print(l1,id(l1))#[10, 'Rossum', 45.67, True] 2457936215680
# l1.reverse()
# print(l1,id(l1))#[True, 45.67, 'Rossum', 10] 2457936215680
# l2=[10,20,30,40,50,20]
# print(l2,id(l2))#[10, 20, 30, 40, 50, 20] 2518191259264
# l3=l2.reverse()
# print(l2,id(l2))#[20, 50, 40, 30, 20, 10] 2518191259264
# print(l3,id(l3))#None 140710664760520

# sort()
# -------------------------------------------
# Syntax1:-    listobj.sort()---->Gives List data in ASCENDING Order
# 			(OR)
# 		  listobj.sort(reverse=False)---->Gives List data in ASCENDING Order
# Syntax2:   list.sort(reverse=True)------Gives List data in DESCENDING ORDER
# l1=[10,23,-45,0,10,25,-5,2]
# print(l1,id(l1))#[10, 23, -45, 0, 10, 25, -5, 2] 2132741734016
# l1.sort()
# print(l1,id(l1))#[-45, -5, 0, 2, 10, 10, 23, 25] 2132741734016
# l1.reverse()
# print(l1,id(l1))#[25, 23, 10, 10, 2, 0, -5, -45] 2132741734016
# l1=[10,23,-45,0,10,25,-5,2]
# print(l1,id(l1))#[10, 23, -45, 0, 10, 25, -5, 2] 2035781549696
# l1.sort(reverse=True)
# print(l1,id(l1))#[25, 23, 10, 10, 2, 0, -5, -45] 2035781549696
# l1=["ritu","biden","trump","rossum","aditya"]
# print(l1,id(l1))#['ritu', 'biden', 'trump', 'rossum', 'aditya'] 1856423804544
# l1.sort()
# print(l1,id(l1))#['aditya', 'biden', 'ritu', 'rossum', 'trump'] 1856423804544
# l1=["ritu","biden","trump","rossum","aditya"]
# print(l1,id(l1))#['ritu', 'biden', 'trump', 'rossum', 'aditya'] 2049109540480
# l1.sort(reverse=True)
# print(l1,id(l1))#['trump', 'rossum', 'ritu', 'biden', 'aditya'] 2049109540480
# l1=[10,"Rossum",True,2+3j,34]
# print(l1,id(l1))#[10, 'Rossum', True, (2+3j), 34] 1782658449024
# l1.sort()
# print(l1)#TypeError: '<' not supported between instances of 'str' and 'int'

# extend()
# ----------------
# =>Syntax:    listobj1.extend(listobj2)
# =>This Function can extend the functionality of list obj1 with the elements if listobj2.
# 			(OR)
# =>This Function Merge Listobj2 values with listobj1
# =>This Function Can take One List object as an argument but not multiple.
# =>In Order to merger Multiple List objects values into Single list object, we use + Operator.
# Syntax:
# 	Listobj-n=listobj1+listobj2+....listobj-n-1
# l1=[10,20,30,40]
# l2=["Chitanya","Zohir","Rossum"]
# print(l1,id(l1))#[10, 20, 30, 40] 2561035157120
# print(l2,id(l2))#['Chitanya', 'Zohir', 'Rossum'] 2561037411328
# l1.extend(l2)
# print(l1,id(l1))#[10, 20, 30, 40, 'Chitanya', 'Zohir', 'Rossum'] 2561035157120
# print(l2,id(l2))#['Chitanya', 'Zohir', 'Rossum'] 2561037411328

# l1=[10,20,30,40]
# l2=["Chitanya","Zohir","Rossum"]
# print(l1,id(l1))#[10, 20, 30, 40] 2796241239680
# print(l2,id(l2))#['Chitanya', 'Zohir', 'Rossum'] 2796242707456
# l2.extend(l2)
# print(l1,id(l1))#[10, 20, 30, 40] 2796241239680
# print(l2,id(l2))#['Chitanya', 'Zohir', 'Rossum', 'Chitanya', 'Zohir', 'Rossum'] 2796242707456

# l1=[10,20,30,40]
# l2=["Chitanya","Zohir","Rossum"]
# l3=["C","Cpp","Python","R"]
# print(l1.extend(l2,l3))#TypeError: list.extend() takes exactly one argument (2 given)

# l1=[10,20,30,40]
# l2=["Chitanya","Zohir","Rossum"]
# l3=["C","Cpp","Python","R"]
# l1=l1+l2+l3
# print(l1,id(l1))#[10, 20, 30, 40, 'Chitanya', 'Zohir', 'Rossum', 'C', 'Cpp', 'Python', 'R'] 2560366980096
# print(l2,id(l2))#['Chitanya', 'Zohir', 'Rossum'] 2560366978048
# print(l3,id(l3))#['C', 'Cpp', 'Python', 'R'] 2560367068096

# Inner (OR) Nested list
# 		=======================================================
# =>The Process of Defining One List in another List is called Inner or Nested List

# =>Syntax:-lstobj1=[ Val1,Val2....[ Val11,Val12....Val1n ].....[Val21,Val22...Val2n]................Val-n ]
# =>Here  [Val11,Val12....Val1n] is called One Inner OR Nested List
# 	      [Val21,Val22...Val2n]  is called another Inner OR Nested List
#          [ Val1,Val2........[Val11,Val12....Val1n].....[Val21,Val22...Val2n]...................Val-n ] is called Outer List
# =>All the pre-defined Functions of List can be applied on Inner or Nested list.
# =>On Inner or Nested List we can perform Index and Slicing Operations.

# sf=[10,"RS",[17,18,16],[78,66,79],"OUCET"]
# print(sf,id(sf),type(sf))#[10, 'RS', [17, 18, 16], [78, 66, 79], 'OUCET'] 2226275288000 <class 'list'>
# print(sf[0])#10
# print(sf[1])#RS
# print(sf[2],type(sf[2]))#[17, 18, 16] <class 'list'>
# print(sf[3])#[78, 66, 79]
# print(sf[2][0])#17
# print(sf[2][-1])#16
# print(sf[2][0:2])#[17, 18]
# print(sf[2][::-1])#[16, 18, 17]
# print(sf[2][::2])#[17, 16]
# sf[2].append(20)
# print(sf,type(sf))#[10, 'RS', [17, 18, 16, 20], [78, 66, 79], 'OUCET'] <class 'list'>
# sf[2].insert(1,50)
# print(sf,type(sf))#[10, 'RS', [17, 50, 18, 16, 20], [78, 66, 79], 'OUCET'] <class 'list'>
# sf[3].clear()
# print(sf)#[10, 'RS', [17, 50, 18, 16, 20], [], 'OUCET']
# sf[3].append(4)
# print(sf)#[10, 'RS', [17, 50, 18, 16, 20], [4], 'OUCET']
# del sf[3]
# print(sf)#[10, 'RS', [17, 50, 18, 16, 20], 'OUCET']

# l1=[[10,20,30],[40,50,60],[70,80,90]]
# for s in l1:
#     print(s) 


# *************************************************************************************************************************************************
# ******Tuple*****
# t1=(10,20,30,40,50,60,10,20)
# print(t1,type(t1))#(10, 20, 30, 40, 50, 60, 10, 20) <class 'tuple'>
# t2=(10,"RS",34.56,"Python",2+3j,True)
# print(t2,type(t2))#(10, 'RS', 34.56, 'Python', (2+3j), True) <class 'tuple'>
# print(t1[0])#10
# print(t1[-1])#20
# print(t2[::-1])#(True, (2+3j), 'Python', 34.56, 'RS', 10)
# print(t1[1:4])#(20, 30, 40)
# print(t1[1:6:3])#(20, 50)

# t2=(10,"RS",34.56,"Python",2+3j,True)
# t2.append(100)
# print(t2)#AttributeError: 'tuple' object has no attribute 'append'
# t2[1]=111
# print(t2)#TypeError: 'tuple' object does not support item assignment

# t1=10,"KVR",34.56,"Hyd"
# print(t1,type(t1))#(10, 'KVR', 34.56, 'Hyd') <class 'tuple'>
# l1=[10,"RS",67.89,"Python"]
# print(l1,type(l1))#[10, 'RS', 67.89, 'Python'] <class 'list'>
# l2=tuple(l1)
# print(l2)#(10, 'RS', 67.89, 'Python')

# t1=(10,"Rossum")
# print(t1,type(t1))#(10, 'Rossum') <class 'tuple'>
# print(t1.index(10))#0
# print(t1.index("Rossum"))#1
# print(t1.index("hyd"))#ValueError: tuple.index(x): x not in tuple
# t1=(10,10,10,20,20,30,40,50,10)
# print(t1.count(10))#4
# print(t1.count(20))#2
# print(t1.count(30))#1
# print(t1.count(40))#1
# print(t1.count(50))#1

# t1=(10,20,30)
# t2=("satish","srinivas","moin")
# print(t1,type(t1))#(10, 20, 30) <class 'tuple'>
# print(t2,type(t2))#('satish', 'srinivas', 'moin') <class 'tuple'>
# # print(t1.extend(t2))#AttributeError: 'tuple' object has no attribute 'extend'
# t1=t1+t2
# print(t1,type(t1))#(10, 20, 30, 'satish', 'srinivas', 'moin') <class 'tuple'>

# t1=(12,34,56,-5,67,0,-23)
# print(t1,type(t1))#(12, 34, 56, -5, 67, 0, -23) <class 'tuple'>
# x=sorted(t1)
# print(x,type(x))#[-23, -5, 0, 12, 34, 56, 67] <class 'list'>
# print(x[0:4])#[-23, -5, 0, 12]
# print(x[0:4:2])#[-23, 0]


# ******************************************************************************************************************************************************
# *****set*********
# to store multiple value of same type or different type in a single object with unique values.
# the set object , the element is represented within {} and these element is sepatated by comma.
# the element of set never maintain insertion order because pvm can display any type of possibility of set object.
# the set object , cant perform indexing and slicing operation.
# the set is immutable bcoz set object does not support item assignment,mutable in case of add().
# there are two types set
# 1.empty set:the set object does contain any element and lenth is 0.
# set{}
# 2.nonempty set:the set object contain element and lengh is greater than 0.
# s={val,val2,val3}
# s={10,20,20,"python",3.23}
# print(s,type(s))
# a=set()
# a.add(10)
# a.add(40)
# print(a)
# a[1]=2
# print(a)
# a={10,20,30,50,"python",'rossum'}
# print(a,type(a))
# a.remove(10)
# print(a)
# a.remove(10)
# print(a)
# a={10,20,30,50,"python",'rossum'}
# a.discard(10)
# print(a)
# a.discard(10)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# a.clear()
# print(a)
# print(a.clear())
# a={10,20,30,50,"python",'rossum'}
# b={10,20,90}
# c={40,60}
# print(a.isdisjoint(c))
# print(a.issubset(b))
# print(a.issuperset(b))
# s=a.union(b)
# print(s)
# s=a.intersection(b)
# print(s)
# s=a.difference(b)
# print(s)
# s=a.symmetric_difference(b)
# print(s)
# a.update(b)
# print(a)

# **************************************************************************************************************************
# Display the Result of Python Program
# print(10)
# a=20
# print(a)
# print("I LOVE YOU MY LOVE TAMU")
# print('i love you bayani')
# a=20
# b=30
# c=a+b
# print("the value of a is",a ,"the value of b is ",b ,"and the sum is",c)
# print(a,'+',b,'=',c)
# print(a,'is the value of a',b,'is the value of b','=',c,'is the sum')
# a=20
# b=30
# c=a+b
# print('sum={}'.format(c))
# print('{} is the sum'.format(c))
# # sum of 10 and 20=30
# print('sum of {} and {}={}'.format(a,b,c))
# # sum of 10,20 and 30=60
# a=20
# b=30
# c=40
# d=a+b+c
# print('sum of {},{} and {}={}'.format(a,b,c,d))
# rno=10
# sname="Rossum"
# # My Roll No:10 and My Name is Rossum
# print('my roll no:{} and my name is {}'.format(rno,sname))
# # My Roll No:10 and My Name is 'Rossum'
# print("my roll no:{} and my name is '{}'".format(rno,sname))
# a=10
# b=20
# c=a+b
# # sum= 30
# print('sum =%d' %c)
# # 30 is the sum
# print('%d is the sum' %c)
# # sum of 10 and 20=30
# print('sum of %d and %d=%d' %(a,b,c))
# sum(10,20)=30
# print('sum(%d,%d)=%d' %(a,b,c))
# rno=10
# sname="Rossum"
# # My Roll No:10 and My Name is 'Rossum'
# print("my roll no:%d and my name is '%s'" %(rno,sname))
# a=10
# b=1.2
# c=a+b
# # sum of 10 and 1.200000=11.200000
# print('sum of %d and %f=%f' %(a,b,c))
# # sum of 10 and 1.20=11.200
# print('sum of %d and %0.2f=%0.3f' %(a,b,c))
# lst=[10,"RS",34.56,True]
# print(lst)
# print('content of valiue is',lst)
# print('content of value is {}'.format(lst))
# print('content of value is %s' %(str(lst)))
# # for x in lst:
# #     print(x)
# # for x in lst:
# #     print(x,end=" ")
# # for x in lst:
# #     print(x,end=",")
# # for x in lst:
# #     print('The content of value is',x,end=",")
# # for x in lst:
# #     print('The content of value is {}'.format(x),end=",")
# # for x in lst:
# #     print('{}'.format(x),end=",")
# # for x in lst:
# #     print('%s' %(str(x)),end=",")
# # for x in lst:
# #     print('%s' %(str(x)),end=",")
# a=10
# b=20
# c=a+b
# print(f"The value of a is {a} and the value of b is {b}, the sum is {c}")

# print("mul={}".format(float(input("Enter First Value:"))*float(input("Enter First Value:"))))
# a=10
# b=50
# c=(a+b)
# print(c,type(c))
# a=input("add some val")
# b=input("add some val")
# print(a,type(a))
# print(b,type(b))
# print(a+b)
# x=float(a)
# y=float(b)
# print(x,type(x))
# print(y,type(y))
# print(x+y)
# a=float(input("enter the val --"))
# b=float(input("enter the val --"))
# print(a)
# print("add={}".format(float(input("enter the val"))+float(input("enter the val"))))
# a=float(input("enter the val 1="))
# b=float(input("enter the val 2="))
# c=float(input("enter the val 3="))
# print(a*b*c)
# print("mul={}".format(float(input("enter the val 1="))*float(input("enter the val 2="))*float(input("enter the val 3="))))

# r=float(input("enter the val"))
# area=3.14*r*r
# print(area)

# lenth=float(input("enter the val " ))
# breath=float(input("enter the val"))
# area=lenth*breath
# print(area)
# side=float(input("enter the val"))
# area=side*side
# paremater=4*side
# print(area,paremater)

# a=float(input("enter the val"))
# b=float(input("enter the val"))
# x=a*a+2*a*b+b*b
# print(x)

# p=float(input("enter the val pricpal :"))
# t=float(input("enter the val of time :"))
# r=float(input("enter the val of rate of intrest :"))
# si=(p*t*r)/100
# print(si)

# print(10<<3)
# print(-10<<3)
# print(10>>3)
# print(-10>>3)
# print(12<<2)
# print(-12<<2)
# print(12>>2)
# print(-12>>2)
# print(15<<3)
# print(-15<<3)
# print(15>>3)
# print(-15>>3)
# print(~-12)
# print(10>>4)


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


#write a python program which will accept any digit and display its name
# dictobj={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# d=int(input("Enter the number between Zero to Nine:"))
# res=dictobj.get(d)
# if (res!=None):
#     print(f"{d} is {res}")
# else:
#     print(f"{d} is not a digit")


# dictobj={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# d=int(input("Enter the number between Zero to Nine:"))
# print("{} is {}".format(d,dictobj.get(d)) if dictobj.get(d)!=None else "{} is not a digit".format(d))


#write a python program which will accept a word and check wheather it is palindrome or not.
# word=input("Enter the word:")
# if word==word[::-1]:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# word=input("Enter the word:")
# p=list(word)
# res=list(reversed(word))
# if p==res:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# word=input("Enter the word:")
# print("Palindrome" if word==word[::-1] else "not a Palindrome")


# write a python program which will accept a word and decide wheather it is contains vowels or not.
# w=input("Enter the word:")
# if 'a' in w or 'e' in w or 'i' in w or 'o' in w or 'u' in w:
#     print("contains vowel")
# else:
#     print(" not contains vowel")

# w=input("Enter the word:")
# d={'a','e','i','o','u'}
# for x in w:
#     if x in d:
#         print(f"{x} is vowel")
#     else:
#         print( f"{x} is not vowel")



#write a python program which will impliment the following menu driven application
#                      --------------------------
#                      Arithmetic operations
#                      --------------------------
#                      1.Addition
#                      2.Substraction
#                      3.Multiplication
#                      4.Division
#                      5.modulo division
#                      6.Exponentiation
#                      7.Exit
#                      --------------------------
#                       Enter your choice
# import sys
# print("-"*50)
# print("\t Arithmetic operation")
# print("-"*50)
# print("\t1.Addition")
# print("\t2.Substraction")
# print("\t3.Multiplication")
# print("\t4.Division")
# print("\t5.Modulo Addition")
# print("\t6.Exponentiation")
# print("\t7.Exit")
# opr=int(input("Enter the number betwen 1 to 7:"))
# print("-"*50)
# match(opr):
#     case 1:
#         a=float(input("Enter the first number:"))
#         b=float(input("Enter the second number:"))
#         print(f"sum of{a} and {b} ={a+b}")
#     case 2:
#         a=float(input("Enter the first number:"))
#         b=float(input("Enter the second number:"))
#         print(f"sub of{a} and {b} ={a-b}")
#     case 3:
#         a=float(input("Enter the first number:"))
#         b=float(input("Enter the second number:"))
#         print(f"mul of{a} and {b} ={a*b}")
#     case 4:
#         a=float(input("Enter the first number:"))
#         b=float(input("Enter the second number:"))
#         print(f"div of{a} and {b} ={a/b}")
#         print(f"Floatdiv of {a} and {b}={a//b}")
#     case 5:
#         a=float(input("Enter the first number:"))
#         b=float(input("Enter the second number:"))
#         print(f"mod of{a} and {b} ={a%b}")
#     case 6:
#         a=int(input("Enter the base:"))
#         b=int(input("Enter the power:"))
#         print(f"power of{a} and {b} ={a**b}")
#     case 7:
#         print("Your every arithmetic operation complited")
#         sys.exit()
# print("Your program exicution complited")


#write apython program which will impliment the following
#-----------------------
#Area of Rectangle
#-----------------------
#R:Rectangle
#s:Square
#c:circle
#T:Triangle
#E:Exit
#--------------------------
#Enter your choice
# -------------------------

# import sys
# print("-"*50)
# print("Area of Rectangle")
# print("-"*50)
# l=input("Enter your chice this letters 'R,S,C,T,E':").upper()
# print("-"*50)
# match(l):
#     case 'R':
#         l=float(input("Enter the length:"))
#         b=float(input("Enter the breath:"))
#         print(f"length {l} and breath {b} then Area of Rectangle is {l*b}")
#     case 'S':
#         s=float(input("Enter the side:"))
#         print(f"Area of Square is {s*s}")
#     case 'T':
#         b=float(input("Enter the base:"))
#         h=float(input("Enter the height:"))
#         print(f"Area of Triangle is {(b+h)/2}")
#     case 'C':
#         r=float(input("Enter the Radious:"))
#         print(f"Area of circle is {3.14*r}")
#     case 'E':
#         print("Your operation complited")
#         sys.exit()
# print("Your program exicution complited")


# wkd=input("Enter the weekday:")
# match (wkd[0:3].upper()):
#     case 'MON':
#         print("It is Monday")
#     case 'THE':
#         print("It is Thusday")
#     case 'Wed':
#         print("It is Wednesday")
#     case 'THU':
#         print("It is Thursday")
#     case 'FRI':
#         print('It is friday')
#     case 'SAT':
#         print('It is Saturday')
#     case 'SUN':
#         print('It is Sunday')
#     case _:
#         print('It is not Weekday')
# print("Your Exicution complited")


# wkd=input("Enter the weekday:")
# match ( wkd[0:3].upper()):
#     case 'MON':
#         print("It is Working day")
#     case 'THE':
#         print("It is TWorking day")
#     case 'Wed':
#         print("It is Working day")
#     case 'THU':
#         print("It is Working day")
#     case 'FRI':
#         print('It is Working day')
#     case 'SAT':
#         print('It is Week day')
#     case 'SUN':
#         print('It is Holi day')
#     case _:
#         print('It is not Weekday')
# print("Your Exicution complited")


# wkd=input("Enter the weekday:")
# match ( wkd[0:3].upper()):
#     case 'MON'|'THE'|'Wed'|'THU'|'FRI':
#         print("It is Working day")
#     case 'SAT':
#         print('It is Week day')
#     case 'SUN':
#         print('It is Holi day')
#     case _:
#         print('It is not Weekday')
# print("Your Exicution complited")

# wkd=input("Enter the weekday:")
# if wkd[0:3].upper() in ['SUN','MON','THES','WEDNES','THURS','FRI','SATUR'] and wkd.isalpha():
#     match(wkd[0:3].upper()):
#           case 'MON'|'THE'|'Wed'|'THU'|'FRI':
#              print("It is Working day")
#           case 'SAT':
#             print('It is Week day')
#           case 'SUN':
#             print('It is Holi day')
#           case _:
#            print('It is not Weekday')
#     print("Your Exicution complited")


#write a python program which will generate 1 to n where n is positive integar value.
# import time
# n=int(input("Enter the number:"))
# if (n<=0):
#     print(f"{n} is invalid") 
# else:
#     i=1
#     while(n>=i): #while(i<=n):
#         print(f"{i}")
#         i=i+1
#         time.sleep(1)
# print("Program exicution complited")


#write a python program which will generate n to 1 where n is positive integar value
# import time
# n=int(input("Enter the number:"))
# if (n<=0):
#     print(f"{n} is invalid")
# else:
#     i=1
#     while(n>=i):
#         print(f"{n}")
#         n=n-1
#         time.sleep(1)
# print("Program exicution complited")


# write a python program for generating even numbers with in 'n' where 'n' must be the positive integer value 
# import time
# n=int(input("Enter the number:")) 
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     i=2
#     while(n>=i):
#         print(f"{i} is a even number")
#         i=i+2
#         time.sleep(1)
#     else:
#         print("It is else block statement")
# print("Program exicution complited")


# write a python program for generating odd numbers with in 'n' where 'n' must be the positive integer value
# import time
# n=int(input("Enter the number:")) 
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     i=1
#     while(n>=i):
#         print(f"{i} is a even number")
#         i=i+2
#         time.sleep(1)
#     else:
#         print("It is else block statement")
# print("Program exicution complited")


## write a python program which will generate multiplication table for a given positive integar value.
# import time
# n=int(input("Enter the number:")) 
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     i=1
#     while(n>=i):
#         print(f"{n} * {i} = {n*i}")
#         i=i+1
#         time.sleep(1)


# import time
# n=int(input("Enter the number:")) 
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     i=1
#     while(i<=10):
#         print(f"{n} * {i} = {n*i}")
#         i=i+1
#         time.sleep(1)


#write a python program which will accept a line of text and display them character by character
# line=input("Enter the sentences:")
# i=0
# while(len(line)>i):
#     # print("{} index value is {}".format(i,line[i]))
#     print(f"{i} index value is {line[i]}")
#     i=i+1


##write a python program which will accept a line of text and only print vowels
# line=input("Enter the sentences:")
# i=0
# while(len(line)>i):
#     if line[i] in ['a','e','i','o','u','A','E','I','O','U']:
#         print(f"{line[i]} is a vowel present in {line}")
#     i=i+1


#you are given an integar N .you need to print the series of all prime numbers till N.
# prime number is a natural number greater than 1 with no other divisor except 1 and itself
# n=int(input("Enter the number:"))



#write a python program which will display '1' to 'n' numbers when must be the positive integar value.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(1,n+1):
#         print(x) 



#write a python program which will display 'n' to '1' numbers when must be the positive integar value.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(n,0,-1):
#         print(x)


#write a python program which will generate all even numbers from 'n' to '1' where n is the positive integar value.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(n,0,-1):
#         if (x%2==0):
#             print(f"The even number is {x}")


#write a python program which will generate all even numbers from 'n' to '1' where n is the positive integar value.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(n,0,-1):
#         if (x%2!=0):
#             print(f"The odd number is {x}")


#write a python program which will generate multiplication table for a given integar value by using for loop that number 
# is the positive integar value .
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(10,0,-1):
#         # print("{} * {} = {}".format(n,x,n*x))
#         print(f"{n} * {x} = {n*x}")
        

# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     for x in range(0,11):
#         # print("{} * {} = {}".format(n,x,n*x))
#         print(f"{n} * {x} = {n*x}")
  

#write a python program which will list of value dynamically and display those value.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     li=[]
#     for x in range(n):
#         y=int(input("Enter the value:"))
#         li.append(y)
#         print(li)


#write a python program which will read key,value from keyboard and put them in dictionary.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     dct={}
#     for i in range(n):
#         x=int(input("Enter the key:"))
#         y=input("Enter the key:")
#         dct[x]=y  
#     else:
#         print(dct)


#write a python program which will read list of numerical values and sort them in both ascending descending order.
# n=int(input("Enter the number:"))
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#     li=[]
#     for x in range(n):
#         y=int(input("Enter the value:"))
#         li.append(y)
#     else:
        # print(li)
        # print(li[::-1])

        # li.sort()
        # li.reverse()
        # print(li)

        # li.sort(reverse=True)
        # print(li)


#write a python program print odd number using while loop.
# n=int(input("Enter the number:"))
# i=1
# if(n<=0):
#     print(f"{n} is invalid")
# else:
#    while i<=n:
#         if i%2!=0:
#          print(i)
#         i=i+1


#write a python program which will accept a numeric value and decide wheather the given number is prime or not.
# n=int(input("Enter the number:"))
# if(n<=1):
#     print(f"{n} is invalid input")
# else:
#     res="prime"
#     for i in range(2,n):
#         if(n%i==0):
#             res="not prime"
#             break
#     if(res=="prime"):
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not prime")


#find the prime number from n of numeric value to n numeric value
# low=int(input("enter the number:"))
# high=int(input("enter the number:"))
# for i in range(low,high+1):
#     if (i<=0):
#         print(f"{i} is invalid")
#     else:
#         res="prime"
#         for x in range(2,i):
#             if(i%x==0):
#                 res="not prime"
#                 break
#         if(res=="prime"):
#             print(i)


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


# n=int(input("Enter the number:"))
# n1=2
# while n1<=n:
#     p="prime"
#     for i in range(2,n1):
#         if (n1%i==0):
#             p="not prime"
#             break
#     if p=="prime":
#         print(f"{n1} is a prime number")
#     n1=n1+1
# else:
#     print("invalid number")



# write a python program which will accept list of values and find them sum and average.
# l=[10,20,30,40,50,60]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum) 
# avg=sum/len(l) 
# print(avg) 


# write a python program which will accept list of values dynamically and find them sum and average.
# n=int(input("enter the number:"))
# if(n<0):
#     print(f"{n} is invalid number")
# else:
#     l=[]
#     for i in range(n):
#         y=int(input(f"enter {i} number:"))
#         l.append(y)
#     else:
#         print(l)
#         s=0
#         for x in l:
#             s=s+x
#         print(s)
#         z=s/len(l)
#         print(z)
    

## write a python program which will accept list of numeric value and find max and min elements.
# n=int(input("enter the number:"))
# if(n<0):
#     print(f"{n} is invalid number")
# else:
#     l=[]
#     for i in range(n):
#         y=int(input(f"enter the {i} number:"))
#         l.append(y)
#     else:
#         print(l)
#         l.sort()
#         print(l)
#         min=l[0]
#         max=l[-1]
#         print(min)
#         print(max)


## write a python program which will accept list of numeric value and find sum,avg of positive numbers only.
# n=int(input("Enter the number:"))
# if(n<0):
#         print(f"{n} is invalid")
# else:
#     l=[]
#     for i in range(1,n+1):
#         y=int(input(f"enter the {i} number"))
#         l.append(y)
#     else:
#         print(l)
#         z=0
#         p=0
#         for x in l:
#                 if (x>0):
#                      z=z+x
#                      p=p+1
#         else:
#            print(f"sum ={z}")
#            avg=z/p
#            print(avg)


## write a python program which will accept list of numeric value and find sum,avg of negative numbers only.
# n=int(input("Enter the number:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     l=[]
#     for i in range(1,n+1):
#         y=int(input(f"Enter the {i} number:"))
#         l.append(y)
#     else:
#         z=0
#         p=0
#         for x in l:
#             if(x<0):
#                 z=z+x
#                 p=p+1
#         else:
#             print(z)
#             avg=z/p
#             print(avg)


## write a python program which will accept list of numeric value and display only even number.
# n=int(input("Enter the number:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     l=list()
#     for i in range(1,n+1):
#         y=int(input(f" enter the {i} number:"))
#         l.append(y)
#     else:
#         for w in l:
#             if(w%2!=0):
#                 continue
#             print(w,end=' ')
                

# n=int(input("Enter the number:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     l=list()
#     for i in range(1,n+1):
#         y=int(input(f" enter the {i} number:"))
#         if(y%2==0):
#             l.append(y)
#     print(l)


# num = input("Enter a a number").split()
# l = []
# l.append(num)
# print(l)



## write a python program which will accept list of numeric value and display only odd number.
# n=int(input("Enter the number:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     l=list()
#     for i in range(1,n+1):
#         y=int(input(f" enter the {i} number:"))
#         l.append(y)
#     else:
#         for w in l:
#             if(w%2==0):
#                 continue
#             print(w,end=' ')   


#write a python program which will accept list of words and display only pallendroms
# n=int(input("Enter the number:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     l=[]
#     for x in range(1,n+1):
#         y=input(f"Enter the {x} word:")
#         l.append(y)
#     else:
#         print(l)
#         for j in l:
#             if j!=j[::-1]:
#                 continue
#             print(j,end=' ')



#08.12.2022
#Write a python program which will impliment the following
#   1----->1
#          2
#          3
#   2----->1
#          2
#          3
#   3----->1
#          2
#          3
#   4----->1
#          2
#          3
#   5----->1
#          2
#          3
#   6----->1
#          2
#          3
# for i in range(1,7):
#         print(f"The value of **{i}**")
#         for j in range(1,4):
#                 print(f"The value of {j}")



#Write a python program which will generate '1' to 'n' multiplication tables where n is positive.
# n=int(input("Enter the value:"))
# if(n<0):
#     print(f"{n} is invalid")
# else:
#     for i in range(1,n+1):
#         print(f"{i} multiplication table are:")
#         for j in range(1,11):
#             print(f"{i} * {j} = {i*j}")


##Write a python program which will accept list of value from keyboard and generate a multiplication table
# n=int(input("Enter the number:"))
# if (n<0):
#     print(f"{n} is invalid")
# else:
#     l=[]
#     for i in range(1,n+1):
#         y=int(input("enter the {i} number:"))
#         l.append(y)
#     else:
#         print(l)
#         for x in l:
#             print(f"The multiplication table of {x}")
#             for z in range(1,11):
#                 print(f"{x} * {z} = {x*z}")



#Write a python program which will accept list of numerical value and display only prime number
# n=int(input("Enter the number:"))
# if (n<0):
#     print(f"{n} is invalid")
# else:
#     l=[]
#     for i in range(1,n+1):
#         y=int(input(f"enter the {i} number:"))
#         l.append(y)
#     else:
#         print(l)
#         for x in l:
#                 if(x<=1):
#                     print(f"the number is invalid {x}")
#                 else:
#                     res=True
#                     for y in range(2,x):
#                         if (x%y==0):
#                             res=False
#                             break
#                     if(res):
#                         print(f"the pn is {x}")

                

#Write a python program which will accept the age of the citigen and decide wheather eligible vote or not.
# while True:
#     n=int(input("Enter the number from 18 to 100:"))
#     if(n>=18) and (n<=100):
#         break
#     print("invalid again enter valid input:")
# print("This persion is eligible for voting")


#Write a python program which will accept student number,student name and marks in three subjects 'c','c++' and 'python'
# 1.calculate total marks
# 2.calculate percentage of marks
# 3.if grade is equal to fail provided student secured less than 40 in any of the three subjects.
# 4.if grade is equal to 'Distinction' provided total marks likes with in 300 and 250.
# 5.if grade is equal to 'first' provided total marks likes with in 200 and 249.
# 6.if grade is equal to 'second' provided total marks likes with in 150 and 199.
# 7.if grade is equal to 'third' provided total marks likes with in 120 and 149.
# 8.Display the total marks report.
# while True:
#     sno=int(input("Enter the student Roll number from 100 to 200:"))
#     if (200>=sno) and (sno>=100):
#         break
#     print("Invalid student number please enter valid student number")
# sname=input("Enter the student name:")
# while True:
#     cmark=int(input("Enter the mark C:"))
#     if (100>=cmark>=0):
#         break
#     print("Invalid marks of this subject --try again")
# while True:
#     cppmark=int(input("Enter thee mark c++:"))
#     if (100>=cppmark>=0):
#         break
#     print("Invalid marks of this subject --try again")
# while True:
#     pymark=int(input("Enter thee mark python:"))
#     if (100>=pymark>=0):
#         break
#     print("Invalid marks of this subject --try again")
# total=cmark+cppmark+pymark
# permark=(total/300)*100
# if(cmark<=40) or (cppmark<=40) or(pymark<=40):
#     grade="Fail"
# else:
#     if(total<=300) and(total>=250):
#         grade="Distinction"
#     elif (total<=249) and(total>=200):
#         grade="First"
#     elif (total<=199) and(total>=150):
#         grade="Second"
#     elif (total<=149) and(total>=120): 
#         grade="Third" 
# print("*"*50) 
# print(f"Student number is {sno}")
# print(f"Student name is {sname}")
# print(f"{sname} c marks is {cmark}")
# print(f"{sname} c++ marks is {cppmark}")
# print(f"{sname} python marks is {pymark}")
# print(f"Student grade is {grade}")
# print("*"*50)  



# s="mississipi"
# d={}
# for ch in s:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]=d[ch]+1
# print(d)




# **************************************************************************************************************************
#                                                    FUNCTION PROBLEM
# **************************************************************************************************************************
# 1.Define a function for performing addition of two number
# approach-1
#Input---->Function Call
#Processing-->Function Body
#Output-------->Function Call
# def add(a,b):
#         c=a+b
#         return c
# while True:
#     a=int(input("enter the first number:"))
#     b=int(input("enter the second number:"))
#     if (a>0) and (b>0):
#         c=add(a,b)
#         break  
#     else:
#         print("invalid value enter again")
# print(f"{a} + {b} = {c}")


# approach-2
#Input--->Function Body
#Process-->Function Body
#Result---->Function Body
# def add():
#     while True:
#         a=int(input("Enter the first name:"))
#         b=int(input("Enter the second name:"))
#         if (a>0) and (b>0):
#             c=a+b
#             break
#         else:
#             print("invalid value enter again")
#     print(f"{a} + {b} = {c}")
# add()


# approach-3
#Input------>Function call
#Process--->Function Body
#Output----->Function Body
# def add(a,b):      
#            c=a+b
#            print(f"{a} + {b} = {c}")
# while True:
#     a=int(input("Enter the first number:"))
#     b=int(input("Enter the second number:"))
#     if (a>0) and (b>0):
#        add(a,b)
#        break
#     print("invalid value enter again")


# approach-4
#Input------>Function Body
#Process--->Function Body
#Output----->Function Call
# def add():
#     while True:
#         a=int(input("Enter the first number:"))
#         b=int(input("Enter the second number:"))
#         if (a>0) and (b>0):
#             c=a+b
#             break
#         else:
#             print("invalid value enter again")
#     return a,b,c
# a,b,c=add()
# print(f"{a} + {b} = {c}")


#2.Write a python program which will calculate multiplication of two number
# def mul(a,b):
#     c=a+b
#     return c

# while True:
#    a=int(input("Enter the first number:"))
#    b=int(input("Enter the second number:"))
#    if(a>0) and (b>0):
#        c=mul(a,b)
#        break
#    else:
#         print("invalid value enter again")
# print(f"{a} * {b} = {c}")


# def mul():
#     while True:
#         a=int(input("enter the first number:"))
#         b=int(input("enter the second number:"))
#         if (a>0) and (b>0):
#             c=a*b
#             break
#         else:
#             print("invalid enter again")

#     print(f"{a} * {b} = {c}")
# mul()


# def mul(a,b):
#     c=a*b
#     print(f"{a} * {b} = {c}")

# while True:
#     a=int(input("Enter the  first number"))
#     b=int(input("Enter the  second number"))
#     if (a>0) and (b>0):
#         mul(a,b)
#         break
#     else:
#         print(f"invalid again enter value")


# def mul():
#     while True:
#         a=int(input("Enter the first number:"))
#         b=int(input("Enter the second number:"))
#         if (a>0) and (b>0):
#             c=a*b
#             break
#         else:
#             print("invalid try again value enter")
#     return a,b,c
# a,b,c=mul()
# print(f"{a} * {b} = {c}")
# res=mul()
# print(f"{res[0]} * {res[1]} = {res[2]}")


#3.write a python program which will calcute simple interest while reading principle amount , time and rate of interest and also calculate 
#total amount to pay by using function.

# def simpleint():
#     p=int(input("enter the principle amount:"))
#     t=int(input("enter the time:"))
#     r=int(input("enter the rate of interest:"))
#     sp=(p*t*r)/100
#     totam=p+sp
#     print(f" The principal amount is {p}")
#     print(f" The time is {t}")
#     print(f" The rate of interest is {r}")
#     return sp,totam
# simple_interest,total_amount=simpleint()
# print(f"the simple interest is {simple_interest}")
# print(f"the total amount to pay is {total_amount}")



#4.write a python program which will calculate area and perimeter of circle by using function
# def ciarea(r):
#     area=3.14*r**2
#     return area
# while True:
#     r=int(input("enter the area:"))
#     if r>0:
#         area=ciarea(r)
#         break
#     else:
#         print("Enter the valid area again")
# print(f"the radious is {r}")
# print(f"The area of circle is {area}")

# def ciarea(r):
#     perimeter=2*3.14*r
#     return perimeter
# while True:
#     r=int(input("enter the area:"))
#     if r>0:
#         perimeter=ciarea(r)
#         break
#     else:
#         print("Enter the valid area again")
# print(f"the radious is {r}")
# print(f"The perimeter of circle is {perimeter}")



# def ciarea(r):
#     area=3.14*r**2
#     perimeter=2*3.14*r
#     return area,perimeter
# while True:
#     r=int(input("enter the area:"))
#     if r>0:
#         area,perimeter=ciarea(r)
#         break
#     else:
#         print("Enter the valid area again")
# print(f"the radious is {r}")
# print(f"The area of circle is {area}")
# print(f"The perimeter of circle is {perimeter}")



#5.write a python program which will calculate area and perimeter of rectangle by using function
# def rect(l,w):
#     area=l*w
#     peri=2*(l+w)
#     return area,peri
# while True:
#     length=int(input("enter the length of rectangle:"))
#     width=int(input("enter the width of rectangle:"))
#     if (length>0) and (width>0):
#         area,perimeter=rect(length,width)
#         break 
#     else:
#         print(f"enter the valid value again")
# print(f"The length of rectangle is {length}")
# print(f"The width of rectangle is {width}")
# print(f"The area of rectangle is {area}")
# print(f"The perimeter of rectangle is {perimeter}")


#6.write a python program which will calculate factorial of given number
# def fact(n):
#     if n==0:
#         f=1
#     else:
#         f=1
#         for i in range(1,n+1):
#             f=f*i
#     return f
# while True:
#     n=int(input("Enter the number:"))
#     if (n>=0):
#         s=fact(n)
#         break
#     else:
#         print("invalid enter valid number again")
# print(f"The factorial of {n} is {s}")


# def fact(n):
#     if n==0:
#         f=1
#     else:
#         f=1
#         for i in range(n,0,-1):
#             f=f*i
#     return f
# while True:
#     n=int(input("Enter the number:"))
#     if (n>=0):
#         s=fact(n)
#         break
#     else:
#         print("invalid enter valid number again")
# print(f"The factorial of {n} is {s}")


#7.write a python program which will accept any positive numerical value and generate its multiplication table using function.
# def posmul():
#     while True:
#         n=int(input("Enter the number:"))
#         if n<=0:
#             print("invalid number again try")
#         else:
#             for i in range(1,11):
#                 print(f"{n} * {i} = {n*i}")
#             break
# posmul()

# def posmul(n):
#     for i in range(1,11):
#         c=(f"{n} * {i} = {n*i}")
#         print(c)
    
# while True:
#     n=int(input("Enter the number:"))
#     if (n>0):
#         res=posmul(n)
#         break
#     else:
#         print("invalid input try again")


#8.write a python program which will check wheather the given number is prime or not by using function
# def prime():
#     while True:
#         p=int(input("enter the number:"))
#         if p<=1:
#             print("invalid try again")
#         else:
#             q="prime"
#             for i in range(2,p):
#                 if (p%i==0):
#                     q="not prime"
#                     break
#             if q=="prime":
#                     print(f"{p} is a prime number")
#             else:
#                 print(f"{p} is not a prime number")
#             break

# prime()


#9.write a python program which will convert an arbitary number into Roman number by using function
# def roman(num):
#     while (num>=1000):
#         print("M",end='')
#         num=num-1000
#     if (num>=900):
#         print("CM",end='')
#         num=num-900
#     if num>=500:
#         print("D",end='')
#         num=num-500
#     if num>=400:
#         print("CD",end='')
#         num=num-400
#     while num>=100:
#         print("C",end='')
#         num=num-100
#     if num>=90:
#         print("XC",end='')
#         num=num-90
#     if num>=50:
#         print("L",end='')
#         num=num-50
#     if num>=40:
#         print("XL",end='')
#         num=num-40
#     while num>=10:
#         print("X",end='')
#         num=num-10
#     if num>=9:
#         print("IX",end='')
#         num=num-9
#     if num>=5:
#         print("V",end='')
#         num=num-5
#     if num>=4:
#         print("IV",end='')
#         num=num-4
#     while num>=1:
#         print("I",end='')
#         num=num-1

# while True:
#     num=int(input("Enter the number :"))
#     if num>0:
#         roman(num)
#         break
#     else:
#         print("invalid input enter valid number again")


#9.write a python program which will convert an Roman number into Arbitary number by using function
# def roman(char):
    # d={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
    # for i in d:
    #     print(i)

# m=input("Enter the Roman number:")
# roman(m)

# m=input("Enter the Roman number:")
# d={'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
# number=0
# for char in m:
#     number=number+d[char]
# print(number)    




#10.write a python program which will accept list of values and find their sum and average by using function
# approach-1
# def sumavg(listobj):
#     l=[]
#     for i in range(listobj):
#         y=int(input(f"Enter {i} number"))
#         l.append(y)
#     print(l)
#     sum=0
#     for k in l:
#         sum=sum+k
#         avg=sum/len(l)
    
#     print(sum)
#     print(avg)
# while True:
#    list=int(input("Enter How Many Number sum and avg u want to find:"))
#    if (list>0):
#     sumavg(list)
#     break
#    else:
#     print("invalid input try again")


# approach-2
# def readval():
#         l=[]
#         lst=int(input("Enter How Many Number sum and avg u want to find:"))
#         if (lst<=0):
#             return l
#         else:
#             for i in range(1,lst+1):
#                 y=int(input(f"Enter the {i} value:"))
#                 l.append(y)
#             return l
# # l=readval()
# # print(l)

# def sumavg():
#     l=readval()
#     print(l)
#     sum=0
#     for i in l:
#         sum=sum+i
#     else:
#         print(sum)
#         avg=sum/len(l)
#         print(avg)
# sumavg()


#11.write a python program which will accept list of names from the keyboard and sort them in both ascending and descending orders.
#approach=1
# def name():
#     l=[]
#     nm=int(input("Enter the number:"))
#     if (nm<=0):
#         return l
#     else:
#         for i in range(1,nm+1):
#             y=input("Enter the name:")
#             l.append(y)
#         return l
# # l=name()
# # print(l)
# def ascsort(l):
#     print(l)
#     l.sort()
#     print(l)
# # ascsort()
# def descsort(l):
#     print(l)
#     l.sort(reverse=True)
#     print(l)
# # descsort()
# l=name()
# print(l)
# if len(l)==0:
#     print("List is empty, can't sort Names")
# else:
#     while True:
#         opt=int(input("Do u want to sort names in\n Ascending Order (Press-1)\n Decending Order (Press-2) \n exit (press-3)\n Enter the option:"))
#         match(opt):
#             case 1:
#                 ascsort(l)
#             case 2:
#                 descsort(l)
#             case 3:
#                 print("Thx for using this Program")
#                 break
#             case __:
#                 print("Ur Selection of Operation is wrong--try again")




#approach=2
# def name():
#     l=[]
#     nm=int(input("Enter the number:"))
#     if (nm<=0):
#         return l
#     else:
#         for i in range(1,nm+1):
#             y=input("Enter the name:")
#             l.append(y)
#         return l
# # l=name()
# # print(l)
# def ascsort(l):
#     print(l)
#     l.sort()
#     print(l)
# # ascsort()
# def descsort(l):
#     print(l)
#     l.sort(reverse=True)
#     print(l)
# # descsort()
# l=name()
# if (len(l)==0):
#     print("List is empty, can't sort Names")
# while True:
#     n=int(input("Enter the number from 1 to 3:"))
#     if (n==1):
#         print(f"The original name is {l}")
#         p=ascsort(l)
#     elif n==2:
#         print(f"The original name is {l}")
#         p=descsort(l)
#     elif n==3:
#         print("Thx for using this Program")
#         break
#     else:
#         print("Enter invalid number please enter in between from 1 to 4")


#12.write a python program which will gererate Fibonocci Series
# def Fibonocci(n):
#     if n==1:
#         n1=0
#         print(n1)
#     elif n==2:
#         n1=0
#         n2=1
#         print(n1)
#         print(n2)
#     else:
#         n1=0
#         n2=1
#         print(n1)
#         print(n2)
#         for i in range(2,n):
#             n3=n1+n2
#             n1=n2
#             n2=n3
#             print(n3)
# while True:
#     n=int(input("Enter How Many Fibonocci Numbers u want:"))
#     if n>0:
#         Fibonocci(n)
#         break
#     else:
#         print("invalid enter valid input again")


#positional arguments example
#13.Program for Demonstrating Possitioan arguments
# def pos(roll,name,mark):
#     print(f"\t{roll}\t{name}\t{mark}")
# print("\tROLL\tName\tMarks")
# pos(1,'jnana',100)
# pos(2,'lipu',200)
# pos(3,'bayani',300)
# pos(4,'tamana',400)
# pos(5,'mitu',500)


# def pos(roll,name,mark):
#     print(f"\t{roll}\t{name}\t{mark}")
# print("\tROLL\tName\tMarks")
# pos(1,'jnana',100)
# pos(2,'lipu',200)
# pos(3,'bayani',300)
# pos(4,'tamana',400)
# pos(5,'mitu',500)
# pos(name='Rubi',roll=6,mark=600)



# def pos(roll,name,mark,crs='python'):
#     print(f"\t{roll}\t{name}\t{mark}\t{crs}")
# print("\tROLL\tName\tMarks\tcrs")
# pos(1,'jnana',100)
# pos(2,'lipu',200)
# pos(3,'bayani',300)
# pos(4,'tamana',400)
# pos(5,'mitu',500)
# pos(name='Rubi',roll=6,mark=600)


# def pos(roll,name,mark,crs='python',cnt='india'):
#     print(f"\t{roll}\t{name}\t{mark}\t{crs}\t{cnt}")
# print("\tROLL\tName\tMarks\tcrs\tcnt")
# pos(1,'jnana',100)
# pos(2,'lipu',200)
# pos(3,'bayani',300,crs='Medical')
# pos(4,'tamana',400,cnt='USA')
# pos(5,'mitu',500)
# pos(name='Rubi',roll=6,mark=600)
# pos(cnt='Japan',crs='Doctor',name='Baby',roll=7,mark=700)


# def pos(roll,name,mark,crs='python',cnt='india'):
#     print(f"\t{roll}\t{name}\t{mark}\t{crs}\t{cnt}")
# def pos1(roll,name,mark,crs='Java',cnt='USA'):
#     print(f"\t{roll}\t{name}\t{mark}\t{crs}\t{cnt}")
# def pos3(roll,name,mark,crs='Medical',cnt='Russia'):
#     print(f"\t{roll}\t{name}\t{mark}\t{crs}\t{cnt}")
# print("\tROLL\tName\tMarks\tcrs\tcnt")
# pos(1,'jnana',100)
# pos(2,'lipu',200)
# pos3(3,'bayani',300)
# pos3(4,'tamana',400,cnt='Japan')
# pos1(5,'mitu',500)
# pos(name='Rubi',roll=6,mark=600)
# pos1(cnt='Japan',crs='Doctor',name='Baby',roll=7,mark=700)


# A=[1,2,3]
# B=[4,5,6]
# print(A+B)

# def kwvarlen(**param):
#     print(param,type(param),len(param))
#     for k,v in param.items():
#         print(f"{k} : {v}")
# kwvarlen(name='jnana',roll=100,crs='B tech',cls='Gandhi')


# def kwvarlen(id,branch,**param):
#     print(param,type(param),len(param))
#     print(f"Student id is {id} and Branch is {branch}")
#     for k,v in param.items():
#         print(f"{k} : {v}")
# kwvarlen(1,'CSE',name='jnana',roll=100,crs='B tech',cls='Gandhi')


# def kwvarlen(id,branch,*para,**param):
#     print(f"Student id is {id} and Branch is {branch}")
#     print(param,type(param),len(param))
#     for k,v in param.items():
#         print(f"{k} : {v}")
#     print(para,type(para),len(para))
#     sum=0
#     for mark in para:
#         sum=sum+mark
#     print(f"The student mark is {sum}")
# kwvarlen(1,'CSE',10,20,30,40,50,name='jnana',roll=100,crs='B tech',cls='Gandhi')


# def kwvarlen(id,branch,*para,country="India",**param):
#     print(f"Student id is {id} of Branch  {branch} and belongs to {country} country")
#     print(param,type(param),len(param))
#     for k,v in param.items():
#         print(f"{k} : {v}")
#     print(para,type(para),len(para))
#     sum=0
#     for mark in para:
#         sum=sum+mark
#     print(f"The student mark is {sum}")
# kwvarlen(1,'CSE',10,20,30,40,50,name='jnana',roll=100,crs='B tech',cls='Gandhi')
# kwvarlen(2,'EEE',10,20,30,40,50,60,70,name='Biswa',roll=101,crs='Bcom',cls='kdpauto collage',country='USA')






				






  

        










    






                    





    




        
        
        

 









