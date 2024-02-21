ly=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or ly%400==0:
    print("leap year")
else:
    print("non leap year")
