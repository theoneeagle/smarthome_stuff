import requests
import time

LoranIP='192.168.3.101'


period1=2


def relay(i, s, ip=LoranIP):
	url='http://{0}/cmd.cgi?cmd=REL,{1},{2}'.format(ip, i, s)
	print(url)
	r=requests.get(url)
	print(r.status_code)
	print(r.text)

	
	

	
relay(1, 0)
time.sleep(period1)
			
relay(2, 0)
time.sleep(period1)

relay(3, 0)
time.sleep(period1)
		
relay(4, 0)
time.sleep(period1)
		
		
		
	
	
