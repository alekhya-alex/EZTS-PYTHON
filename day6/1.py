#write a python program shoping mall having 5% discount for men and 7% disount for women and individual discount on each item topurchase is 3*number of item customer purchase calculate the total billd={}\\]'
d={}
n=int(input("enter no of item:"))
for i in range(n):
    k=input("enter item:")
    v=int(input("enter item price:"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("enter the gender:")
if g=="male":
     bill=sum(l)-sum(l)*7/100
     print(bill)
else:
     bill=sum(l)-sum(l)*5/100
     print(bill)
j=0
print("items - prices : discount-prices")
for i in d:
    print(f"{i}-{d[i]}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"total bill :{bill}")
