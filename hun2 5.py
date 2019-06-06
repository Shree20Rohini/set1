#shree
xx=int(input())
a=list(map(int,input().split(" ")))
l=len(a)
m=[]
for i in range(0,l):
    v=max(a[i:])
    if(v==a[i]):
        m.append(v)
for i in range(0,len(m)-1):
    print(m[i],end=" ")
print(m[len(m)-1],end="\n")
print(max(a),end="")
