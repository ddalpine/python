#coding=utf-8



i = input("请输入3个整数,用','分开:")
i = i.split(',',3)

if len(i) != 3:
	print("请重新输入")
else:
	i.sort()
	print(i[0])
	print(i[1])
	print(i[2])
