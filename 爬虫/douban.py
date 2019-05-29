#encoding:utf-8
import urllib
import urllib2

# demo1

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={"User-Agent": "Mozilla...."}

# 变动的是这两个参数，从start开始往后显示limit个
formdata = {
    'start':'0',
    'limit':'10'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)
response = urllib2.urlopen(request)

print response.read().decode('utf-8')


# demo2

# url = "https://movie.douban.com/j/chart/top_list?"
# headers={"User-Agent": "Mozilla...."}

# # 处理所有参数
# formdata = {
#     'type':'11',
#     'interval_id':'100:90',
#     'action':'',
#     'start':'0',
#     'limit':'10'
# }
# data = urllib.urlencode(formdata)

# request = urllib2.Request(url, data = data, headers = headers)
# response = urllib2.urlopen(request)

# j = response.read()
# with open("douban.txt","w") as f:
# 	f.write(j)
