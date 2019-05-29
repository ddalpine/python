#coding=utf-8
i =100
while i<1000:
	b = int(i//100)
	s = int(i/10%10)
	g = int(i%100%10)
	if b**3+s**3+g**3==i:
		print(i)
	i+=1