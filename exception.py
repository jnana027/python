# Example 1
# a=int(input("enter the first value:"))
# b=int(input("enter the second value:"))
# try:
#     d=a/b
#     print(d)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as ob:
#     print(ob)
# except Exception:
#     print("enter the correct value")
# else:
#     print("your answer is correct")
# finally:
#     print("Thanks you")


# Example 2
# try:
#     f=open('demo_file','w')
#     f.write('Test write this')
# except IOError:
#     print("Error: Could not find file or read data")
# else:
#     print("content written sucessfully")
#     f.close()


# Example 3
# try:
#     f=open('demo_file','r')
#     f.write('Test write this')
# except IOError:
#     print("Error: Could not find file or read data")
# else:
#     print("content written sucessfully")
#     f.close()


# Example 4
# def askint():
#     try:
#         val=int(input("please enter the integar value:"))
#     except:
#         print("loook like you did not enter an integar")
#     finally:
#         print("finally,I exucuted")
#     print(val)
# askint()


# Example 5
# def askint():
#     try:
#         val=int(input("please enter the integar value:"))
#     except:
#         print("loook like you did not enter an integar")
#         try:
#             val=int(input("Try again please enter the integar value:"))
#         except:
#             print("handle ittt")
#     finally:
#         print("finally,I exucuted")
#     print(val)
# askint()


# that only did one check . How can we continiouslly checking? We can use while loop

# Example 6
# def askint():
#     while True:
#       try:
#         val=int(input("please enter the integar value:"))
#       except:
#         print("loook like you did not enter an integar")
#         break
#       else:
#         print("that is an integar number")
#       finally:
#         print("finally,I exucuted")
#         print(val)
# askint()


# Example 7
# Rising an exception
# def raise_exe(a):
#     if a<5:
#         raise Exception(a)
#     return a 
# try:
#     res1=raise_exe(8)
#     print(res1)
#     res=raise_exe(2)
#     print(res) 
# except Exception as e:
#     print("Error is: ",e) 


# Example 8
# User defined Exception
# class NewError(Exception):
#     def __init__(self,val):
#         self.val=val
#     def __str__(self):
#         return (repr(self.val))
# try:
#     raise (NewError(5))
# except NewError as e:
#     print("A new exception occured :" , e.val)


# Example 9
# Assertion
# syn:assert condition,error_message
# a=10
# assert a<=10,'Invalid Syntax'
# print(a)


# try:
#     x=1
#     y=1
#     assert x!=y,"Both variable in not same"
#     print(x,y)
# except AssertionError as msg:
#     print(msg)


# list1=['a',0,2]
# for e1 in list1:
#     try:
#         print("The element is ",e1)
#         res=int(e1)/int(e1)
#         break
#     except Exception as e:
#         print(e, 'occured')
#         print("Next  check for another element in a list")
# print(res)


# try:
#     a=int(input("enter positive integar:"))
#     if a<=0:
#         raise ValueError("that is not a positive integar")
# except ValueError as e:
#     print(e)


# try:
#      a=int(input("enter a number:"))
#      assert a%2==0,"This is not even number"
# except AssertionError as msg:
#     print(msg)
# else:
#     print("you enter even number")


# def raise_exception(ex):
#     raise ex
# y=lambda x:2*x if x<10 else raise_exception(Exception('value is greater than 10'))
# # print(y(4))
# print(y(9))

# import math
# def find_sqrt(a):
#     if not isinstance(a(int,float)):
#         raise TypeError("a must be numeric")
#     elif a<0:
#         raise TypeError("a should not be negative")
#     else:
#         print(math.sqrt(a))
# print(find_sqrt(8))


# class NegativeNumberException(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)
# while True:
#     try:
#         a=int(input("enter first number :"))
#         b=int(input("enter second number :"))
#         if a<0 or b<0:
#             raise NegativeNumberException()
#         c=a/b
#         print(c)
#     except ValueError:
#         print("please input integar only")
#     except ZeroDivisionError:
#         print("please input non zero denomination")
#     except NegativeNumberException as e:
#         print(e)
