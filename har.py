# 1..Given an integer,n , perform the following conditional actions:
# If  n is odd, print Weird
# If  n is even and in the inclusive range of  2 to 5, print Not Weird
# If  n is even and in the inclusive range of 6 to 20, print Weird
# If  n is even and greater than 20, print Not Weird
n=int(input("Enter the number:").strip())
# print(n)
if n<0:
    print('NEGATIVE number')      
else:
    # print('POSITIVE number')
    if (n%2!=0) :
        print("Weird")
    if (n%2==0) and (2<=n<=5) or (n>20):
        print("Not Weird")
    if (n%2==0) and (6<=n<=20):
        print("Weird")
    if (n%2==0) and (n>20):
        print("Not Weird")
    