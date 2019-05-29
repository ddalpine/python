#coding=utf-8
i=1
u=0
h=0

while 1:
	u = i + 100
	
	k=1
	while k<=i:
		if u/k == k:#+100的能被完全平方

			k = 1
			h = i + 168
			while k<=i:
				if h/k==k:
					print(i)
				k+=1
		k+=1
	i+=1