#shree
import collections
n,k = map(int,input().split())
a,b,z = [],[],[]
for i in range(0,n):
  a.append(list(map(int,input().split())))
if n==1 and k==1:
  print('1')
else:
  for i in range(0,n-1):
    for j in range(0,k):
      for l in range(0,k):
        if a[i][j]==a[i+1][l]:
          b.append(a[i][j])
          break
  d = collections.Counter(b)
  for i in b:
    if i not in z:
      if d[i]==n-1:
        z.append(i)
  print(*sorted(z))
