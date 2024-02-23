#write a python program to print sum of the given matrix
r,c=int(input("Rows:")),int(input("Coloums:"))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
summ=0
for i in l:
    summ+=sum(i)
print(summ)
