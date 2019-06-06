#shree
n1,k=map(int,input().split())
a= [[abs(i-k),i]for i in [int(x) for x in input().split()]]
a.sort()
a=a[1:]
a=[i[1] for i in a[:3]]
print(*a)
