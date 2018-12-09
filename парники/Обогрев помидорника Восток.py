import requests
import time

file='C:\\wamp\\www\\thermo\\BM1707.dat'
LoranIP='192.168.3.101'

Tmax_parnik2=5
''' температура выкл 5 '''

Tmin_parnik2=4
''' температура вкл 4 '''

period=10 

closed=1
''' нагрев при запуске (выключен) '''
print("NAGREV_OFF-pomidornik-vostok")
def relay(i, s, ip=LoranIP):
	url='http://{0}/cmd.cgi?cmd=REL,{1},{2}'.format(ip, i, s)
	print(url)
	r=requests.get(url)
	print(r.status_code)
	print(r.text)

while True:
	f=open(file, 'r')
	s=f.readlines()[-1]
	s=s[s.find('>')+1:]
	li=s.strip().split(' ')
	
	parnik=float(li[3].split('=')[1].replace(',', '.'))
	'''print(parnik)'''
	'''print(closed)'''
	
	'''if closed==1:
		print("NAGREV_OFF-pomidornik-vostok")
	
	if closed==0:
		print("NAGREV_ON-pomidornik-vostok")'''
	
	if parnik>Tmax_parnik2 and not closed:
		relay(2, 0)
		closed=1
		print("______________")
		print(parnik)
		print("NAGREV_OFF-pomidornik-vostok")
		print(" ")
		print(time.asctime())
		print("______________")	
	if parnik<Tmin_parnik2 and closed:
		relay(2, 1)
		closed=0
		print("______________")
		print(parnik)
		print("NAGREV_ON-pomidornik-vostok")
		print(" ")
		print(time.asctime())
		print("______________")	

	time.sleep(period)
	
