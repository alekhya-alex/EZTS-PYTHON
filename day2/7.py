#write a python progra to check whether the number is armstrong or not(153,307)
n=int(input())
temp=n
rev=0
while n> 0:
    num=n%10
    rev=rev+num**3
    n//=10
if rev == temp:
    print("armstrong")
else:
    print(" Not a armstrong")
       
    
