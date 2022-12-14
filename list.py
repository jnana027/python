# List & ListComprehension

#1. write a python program to sum all the items in a list
# l=[1,2,3,4,5,6,7,8, 9,10]
# sum=0
# for i in l:
#     # sum=sum+i
#     sum+=i
# print('The sum is:', sum)



#2. write a python program to multiply all the items in a list
# l=[2,3,4,5,6]
# mul=1
# for i in l:
#     mul*=i
# print('The multiplication is:', mul)


#2. write a python program to get the largest number from a list
# l=[32,54,75,97,120]
# def largest(l):
#     largest=l[0]
#     for i in l:
#         if i>largest:
#             largest=i
#     return largest
# print('The largest number  is:', largest(l))


#2.1 write a python program to get the largest number from a list
# l=[32,54,75,97,120]
# l.sort()
# print('The largest number  is:', l[-1])


#2.2 write a python program to get the largest number from a list
# l=[32,54,75,97,120]
# print('The largest number  is:', max(l))


#3 write a python program to get the smallest number from a list
# l=[32,54,75,97,120]
# def smallest(l):
#     smallest=l[0]
#     for i in l:
#         if i < smallest:
#             smallest=i
#     return smallest
# print('The smallest number  is:', smallest(l))

#3.1 write a python program to get the smallest number from a list
# l=[32,54,75,97,120]
# l.sort()
# print('The smallest number  is:', l[0])

#3.2 write a python program to get the smallest number from a list
# l=[32,54,75,97,120]
# print('The smallest number  is:', min(l))


#4. write a python program to count the number of strings  where the string length is 2 
#  or more and the first and last character are same from a given list of string. 
# l=['adda','121','123321','1122','wwww']
# def stringcheck(l):
#     count=0
#     for i in l:
#         if len(i) >= 2 and i[0]==i[-1]:
#             count+=1
#     return count
# print('Number of matched strings are :' , stringcheck(l))

#5.1 write a python program to get a list ,sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples.

# def last(n):
#     return n[-1]
# def sort_last_list(tuples):
#     return sorted(tuples,key=last)
# print(sort_last_list([(1,2),(3,4),(5,6),(4,2)]))

#5.2 write a python program to get a list ,sorted in increasing order by the last element 
# in each tuple from a given list of non-empty tuples.
# def sort_tuple(tup):
#     tup.sort(key=lambda x:x[-1])
#     return tup
# tup=[(1,2),(3,4),(3,1),(8,5)]
# print(sort_tuple(tup))

#6 write a python program to remove duplicates from a list.
# l=[1,3,2,1,2,3,5,3,6,3,4]
# result=[]
# for i in l:
#     if i not in result:
#         result.append(i)
# print(result)

#7.1 write a python program to check a list is empty or not.
# l=[]
# def lengthcheck(l):
#     if len(l)==0:
#         return "This is empty List"
#     else:
#         return "This is not empty List"
# print(lengthcheck(l))

#7.1 write a python program to check a list is empty or not.
# l=[]
# def lengthcheck(l):
#     if len(l)==0:
#         return 0
#     else:
#         return 1
# print(lengthcheck(l))

#8 write a python program to clone or copy a list.
# l=[5,6,7,8,9]
# clone_of_list=l.copy()
# print('The clone is :',clone_of_list)


#9 write a python program to find the list of words that are longer than n from a given list of words
# l=[12334,23456,4345443,303897,937866646664,82309798975]
# def lencheck(l):
#     result=[]
#     n=5
#     for i in l:
#         if len(str(i))>n:
#             result.append(i)
#     return result
# print(lencheck(l))


#10 write a python program to generate a 3*4*6 3D array whose each element is *.
# a=[[['*' for col in range(6)] for col in range(4)] for col in range(3)]
# print(a)

#11 write a python function that take two list and returns  True if they have at least one common member.
# l1=['a','b','c','f']
# l2=['f','g','h','k']
# def elemcheck(l1,l2):
#     result = False
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 result=True
#     return result
# print(elemcheck([1,2,3,4],[4,5,6,7]))

#12 write a python program to print a specified list after removing the 0th,4th and 5th elements.
# l=[1,2,3,4,5,6,7,7,8]
# output=[x for (i,x) in enumerate(l) if i not in (0,4,5)]
# print(output)

#13 write a python program to shuffle and print a specified list.
# from random import shuffle
# l=['a','b','c','d','e']
# shuffle(l)
# print(l)

#13 write a python program to generate all permutations of a list in python.
# import itertools
# print(list(itertools.permutations([9,8,7])))

#14.1 List
#  1.List are used to store multiple items in a single variable.
# 2.list are created using square brackets.
# 3.list can store multiple data types .

# type() and len() method
# type() is used to get data type.
# len() is used to get length of list.
# l=[1,2,3]
# print(type(l))
# print(len(l))

# 14.2 List properties
# 1.list are ordered ,it means that if you add new items to a list ,the new items will be placed at the end of the list.
# one exception to this is insert() which insert at specific index.
# 2.list is mutable,it means that we can change,add and remove items in a list after it has been created.
# 3.list allow duplicates. 

# 14.3.list() method
# list() used to convert other data types to list
# s="jnana"
# print(list(s))
# tuple=(1,2,3)
# print(list(tuple))

# 15.Accessing list elements
# list can be accessed by positive and negative indexing
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]
# syn:l=[start:end:stop]
# print(l[0])
# print(l[0:])
# print(l[:3])
# print(l[0:4])
# print(l[0::2])
# print(l[-1])
# # /*upto 2nd last element*/
# print(l[:-1]) 
# print(l[-1::-1])
# print(l[-4::-1])
# print(l[::-1])

# 16.change list elements
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]

# 16.1 change item value at specific index 
# l[1]=5
# print(l)
# l[0]=6
# print(l)

# 16.2 insert multiple value
# l[0:3]=[7,8,9,4,5,6]
# print(l)



# 17 add element to a list
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]

# 17.1 append() add an item to the end of the list
# l.append('ranjan')
# print(l)

# 17.2 insert() insert an item at the specific index
# l.insert(0,5)
# print(l)

# 17.3 extend() 
# any iterables can be added to list using extend() method.
# iterables:list,tuple,set,dictionary etc
# l.extend(["tamana","bayani"])
# print(l)


# 18.Remove elements from list
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]

# 18.1 remove() it removes a specific element
# l.remove(3)
# print(l)

# 18.2 pop()
# it removes item at specific index.
# if no index specified pop() removes last element.
# l.pop(3)
# print(l)
# l.pop()
# print(l)

# 18.3 del keyword
# it removes the element at specific index
# del l[3]
# print(l)

# 18.4 clear()
# it is used to clear/empty the list
# l.clear()
# print(l)



# 19 loop through list
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]

# for loop
# for i in l:
#     print(i)


# for i in range(len(l)):
#     print(i)


# while loop
# i=0
# while i < len(l):
#     print(l[i])
#     i+=1

# 20. List comprehension
# syn:[expression for item in iterable if condition== True]
# l=[1,2,3,"jnana",{"name":"pradhan"},(2,7,8)]

# y=[x for x in l if x not in [2,3]]
# print(y)

# y=[x for x in range(5)]
# print(y)

# y=[x for x in range(5) if x<2]
# print(y)

# p=['red','blue']
# y=[x.upper() for x in p]
# print(y)

# y=[x if x!='jnana' else'no name' for x in l]
# print(y)

# new=[]
# for x in l:
#     if x!='jnana':
#         new.append(x)
#     else:
#         new.append('no name')
# print(new)

# p=[1,2,3,4,5,6]
# add=[]
# for x in p:
#     if x%2==0:
#         add.append(x)
#     else:
#         add.append('odd')
# print(add)

# y=[x if x%2==0 else 'odd' for x in p]
# print(y)


# 21.List method
# 1.sort()
# p=[1,2,3,8,4,5,6]
# p.sort()
# print(p)
# p.sort(reverse=True)
# print(p)

# 2.copy()
# x=p.copy()
# print(x)

# 3.joining 
# q=[0,9]
# x=p+q
# print(x)

# p=[1,2,3,8,4,5,6]
# q=[0,9]
# for x in p:
#     q.append(x)
# print(q)


# q.extend(p)
# print(q)

# 4.reverse()
# p.reverse()
# print(p)

# 5.count()
# print(p.count(2))
































