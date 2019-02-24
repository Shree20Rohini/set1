num=int(input())
li=list(map(int,input().split()))
li2=[]
for i in range(0,len(li)):
    if i==li[i]:
        li2.append(li[i])
if len(li2)>0:
    print("li2")
else:
    print("-1")

