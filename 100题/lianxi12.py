#coding=utf-8
k=range(101,200)
k=list(k)
# k.remove(150)
# print (k)

for h in range(101,200):
	b=2
	while b <h:#已经排除被自身除和除以1
		#能找到有因数就不是素数
		# print("%d/%d=%d"%(h,b,h%b))
		if h%b == 0:
			k.remove(h)
			break
		# if h%b == 0:
		# 	print(h)
		# 	# print(h%b)
		# 	break		
		b+=1
print(k)
print(len(k))