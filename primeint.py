a,b=map(int,raw_input().split())
for j in range(a+1,b):
	if(j>1):
		for i in range(2,j):
			if(j%i==0):
				break
		else:
			print j,
