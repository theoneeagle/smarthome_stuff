import requests
import time

file='C:\\wamp\\www\\thermo\\BM1707.dat'
LoranIP='192.168.3.101'

Tmax_parnik2=22
''' температура включения вентиляторов 22 '''
Tmin_parnik2=20
''' температура выключения вентиляторов 20 '''
Tglyk=84

period=10 

closed=1
''' вентиляторы при запуске (выключены) '''

print(time.asctime())

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
	print("POMIDORNIK")
	print(parnik)
	print("OGURE4NIK")
	print(float(li[7].split('=')[1].replace(',', '.')))
	
	'''распечатка температур пом-ка и огур-ка'''
	
	if closed==1:
		print("VENTIL_OFF")
		print("______________")
		
	if closed==0:
		print("VENTIL_ON")
		print("______________")
	
	if parnik>Tmax_parnik2 and parnik<Tglyk and closed:
		relay(1, 1)
		closed=0
		
	if parnik<Tmin_parnik2 and not closed:
		relay(1, 0)
		closed=1
		
	time.sleep(period)
	
