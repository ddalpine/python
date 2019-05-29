#encoding:utf-8
import time,random
import hashlib
import urllib,urllib2


def getSalt():
	salt = int(time.time()*1000) + random.randint(0,10)

	return salt


def getMd5(v):
	md5 = hashlib.md5()
	md5.update(v.encode("utf-8"))
	sign = md5.hexdigest()
	return sign


def getSign(key,salt):
	sign = "fanyideskweb" + key + str(salt) + "sr_3(QOHT)L2dx#uuGR@r"
	sign = getMd5(sign)
	return sign


def youdao(key):
	url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
	salt = getSalt()
	data = {
		"i": key,
		"from": "AUTO",
		"to": "AUTO",
		"smartresult": "dict",
		"client": "fanyideskweb",
		"salt": str(salt),
		"sign": getSign(key, salt),
		"doctype": "json",
		"version": "2.1",
		"keyfrom": "fanyi.web",
		"action": "FY_BY_CLICKBUTTION",
		"typoResult": "false",
	}
	data = urllib.urlencode(data).encode('utf-8')


	headers = {
		"Accept": "application/json,text/javascript,*/*;q=0.01",
		# "Accept-Encoding": "gzip,deflate",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Connection": "keep-alive",
		# "Content-Length": len(data),
		"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
		"Cookie": "OUTFOX_SEARCH_USER_ID=1076696971@10.168.8.63;JSESSIONID=aaaZ6s5m9DVmYf8g3QoDw;OUTFOX_SEARCH_USER_ID_NCOO=473292646.5080033;___rl__test__cookies=1543228484656",
		"Host": "fanyi.youdao.com",
		"Origin":"http://fanyi.youdao.com",
		"Referer":"http://fanyi.youdao.com/",
		"User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.100Safari/537.36OPR/56.0.3051.104X-Requested-With:XMLHttpRequest"
	}

	req = urllib2.Request(url=url, data=data,headers=headers)
	rsp = urllib2.urlopen(req)
	html = rsp.read().decode('utf8')
	print html


if __name__ == '__main__':
	youdao('free')
