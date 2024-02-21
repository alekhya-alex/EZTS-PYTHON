#write a python program to check prime number or not
n=int(input())
i=2
while i < (2,(n//2)+1):
    if n%i==0:
        print("Not a prime")
        break
    i+=1
else:
  print("prime")
 
