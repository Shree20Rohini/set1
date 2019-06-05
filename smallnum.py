#shree
from itertools import combinations
a,b=map(int,input().split())
h=len(str(a))
listval=list(combinations(str(a),h-b))
listval=sorted(listval)
print("".join(listval[0]))
