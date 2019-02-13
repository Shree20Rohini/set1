v=int(input())
for i in range (2, int(v/2)):
  if v%i == 0:
    print("no")
    break
 else:
    print("yes")
