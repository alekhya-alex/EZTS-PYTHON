#write a python program to check prime number or not
n=int(input())
for i in range(2,(n//2)+1):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("prime")
