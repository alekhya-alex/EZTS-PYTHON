n,k=map(int,input().split(" "))
x= n*k
if x%4==0:
  y=x//4
else:
  y=(x//4)+1
print(y)
      
