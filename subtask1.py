n = int(input())
p = 0
while(p*p<=n):
    p=p+1
if(p*p>=n):
    p=p-1
q=p*p
print("Closest square number=",q)