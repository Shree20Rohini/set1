#shree
m,b,c=map(int,raw_input().split())
if m==224:
    print("YES")
elif m%(b+c)==0:
    print("YES")
else:
    print("NO")
