#encoding:utf-8
#
#
#


import urllib,urllib2



url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers={"User-Agent": "Mozilla...."}



formdata = {
	'start':'0',
	'limit':'10'
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=headers)
response = urllib2.urlopen(request)


print response.read().decode('utf-8')