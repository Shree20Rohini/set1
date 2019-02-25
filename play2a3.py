#shree
b=int(input())
sq=0
while b>0:
	m=b%10
	sq=sq+m*m
	b=b//10
print(sq)
