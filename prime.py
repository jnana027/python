#write a python program which will accept a numeric value and decide wheather the given number is prime or not.

# 1.
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


# 2.
# while(True):
#     n=int(input("Enter the number:"))
#     if(n>=2):
#         break
#     else:
#         print("enter the valid number")
# p="prime"
# for i in range(2,n):
#     if(n%i==0):
#         p="not prime"
#         break
# if p=="prime":
#         print(f"{n} is a prime number")
# else:
#         print(f"{n} is not a prime number")


# 3.
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


# 4.
#find the prime number from n of numeric value to n numeric value
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

# 5.
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

# 6.
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

# 7.
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



# Generate n prime number
# n=int(input("Enter the number you want see the prime number:"))
# count=0
# n1=2
# while True:
#     p="prime"
#     for i in range(2,n1):
#         if n1%i==0:
#             p="not prime"
#             break
#     if p=="prime":
#         print(f"{n1} is prime number")
#         count=count+1
#     if count==n:
#         break
#     n1=n1+1

