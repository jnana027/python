# def openrussiandoll(doll):
#     if doll==1:
#         print("all doors are opened")
#     else:
#         openrussiandoll(doll-1)
# print(openrussiandoll(5))
# a,b=input("enter the two name:").split(" ")
# print(a,b)

# print("#"*50)
# factorial number
# n=float(input("enter the number:"))
# def factorial(n):
#     if n>=0:
#         if n in [0,1]:
#             return 1
#         else:
#             return n*factorial(n-1) 
#     else:
#         print("not enter negative value") 
# x=factorial(n) 
# print(x) 


# fibonacci number
n=int(input("enter the number:"))
def fibonnaci(n):
    if n>=0:
        if n in [0,1]:
            return n
        else:
            return fibonnaci(n-1)+fibonnaci(n-2)
    else:
        print("not enter negetive number")
x=fibonnaci(n)
print(x)
