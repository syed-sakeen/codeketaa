s,k=map(int,input().split())
for num in range(s+1,k):
	order=len(str(num))
	temp=num
	sum=0
	while (temp>0):
		rem=temp%10
		sum=sum+rem**order
		temp//=10
	if(num==sum):
		print(num)
