#coding=utf-8



i = input()
preday = 0
trueday=0

year = i[:4]
md = i[4:]
month = md[:2]
day = md[2:]
# print (month)
# print (day)

year = int(year)
month = int(month)
day = int(day)

if month == 1:
	# print("1")
	trueday = day

elif month == 2:
	trueday = 31 + day

elif month == 3:
	# print("3")
	preday = 31+28+day

elif month == 4:
	preday = 31+28+31+day

elif month == 5:
	preday = 31+28+31+30+day

elif month == 6:
	preday = 31+28+31+30+31+day	

elif month == 7:
	preday = 31+28+31+30+31+30+day 

elif month == 8:
	preday = 31+28+31+30+31+30+31+day 

elif month == 9:
	preday = 31+28+31+30+31+30+31+30+day 	

elif month == 10:
	preday = 31+28+31+30+31+30+31+30+31+day 	

elif month == 11:
	preday = 31+28+31+30+31+30+31+30+31+30+day 

elif month == 12:
	preday = 31+28+31+30+31+30+31+30+31+30+31+day 	
else:
	print("请重新输入")



if month >2:
	if year % 4 ==0:
		trueday = preday+1
	else:
		trueday = preday

print(trueday)

