#shree
s=int(input())
l1=list(map(int,input().split()))
r=1
l=[]
for i in l1:
  r=r*i
for i in l1:
  l.append(r//i)
print(*l)
