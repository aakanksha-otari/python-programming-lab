())
l=[]
a=0
b=1
count=0
if n<=0:
  print("Series does not exist")
elif n==1:
  print("0")
elif n==2:
  print("1")
else:
  l.append(0)
  l.append(1)
while count<n-2:
  l.append(a+b)
  c=a+b
  a=b
  b=c
  count+=1
print(l)

