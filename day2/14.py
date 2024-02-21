#write a python program to print the count in both even and odd positions
s=input()
ec,oc=0,0
for i in range(len(s)):
    if i%2==0:
        if s[i] in "aeiouAEIOU":
            ec+=1
        else:
            if s[i] in "aeiouAEIOU":
                oc+=1
print(ec,oc)
            
