n=int(input())
temp=abs(n)
sum=0
while(temp!=0):
  temp=int(temp/10)
  sum=sum+1
print (sum)
