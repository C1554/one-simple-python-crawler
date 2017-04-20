import cookielib
import urllib2

url="http://www.baidu.com"

print "first method"
#direct response
response1=urllib2.urlopen(url)
#get status code ,200 mean successfunlly
print response1.getcode()
#read content
print len(response1.read())

print "second method"
#create request object
request=urllib2.Request(url)
#add data  request.add_data('a','1')
#add http's header
request.add_header("user-agent","Mozilla/5.0")
#sent request to get result
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

#add  special situation's processor:HTTPCookieProcessor/ProxyHandler/HTTPSHandler/HTTPRedirectHandler
print "third method"
#create cookie container
cj=cookielib.CookieJar()
#create one opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#install opener for urllib2
urllib2.install_opener(opener)
#urllib2 visit web with cookie
response3=urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()












