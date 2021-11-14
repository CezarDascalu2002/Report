N = [3,4,0,2,1,8,-1]
n=len(N) - 1
print(n)
N.pop()
if(n==0):
    m=-1
    print("minimum = ",m)
    a=-1
    print("average = ",a)
    s=0
    print("sum = ",s)
else:
    N.sort()
    print(N)
    m = N[0]
    print("minimum = ",m)
    s = sum(N)
    print("sum = ",s)
    a = s/n
    print("average = ",a)