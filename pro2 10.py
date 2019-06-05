#shree
n=int(input())
i=0
llist=[]
while(i<n):
    lis=list(map(int,input().split(" ")))
    llist.extend(lis)
    i=i+1
 
llist.sort() 
i=0
while(i<len(llist)):
    print(llist[i],end=" ")
    i+=1
 
