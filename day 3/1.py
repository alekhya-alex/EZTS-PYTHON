#write a python program to print smallest vowel with is repeating odd number of times in a given string
s=input()
s1=""
for i in s:
    if i  in"aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))
