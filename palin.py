x=int(raw_input())
temp=x
r=0
while(x>0):
    d=x%10
    r=r*10+d
    x=x//10
    	
if(temp==r):
	print("yes")
else:
	print("no")
