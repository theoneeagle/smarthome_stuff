import requests
import time

file='C:\\wamp\\www\\thermo\\BM1707.dat'
LoranIP='192.168.3.101'

Tmax_parnik=24
''' температура открытия '''

Tmin_parnik=22
''' температура закрытия '''

Tmax_parnik2=24
''' температура открытия '''

Tmin_parnik2=22
''' температура закрытия '''

Tglyk=84

period=10 
''' частота считывания температуры и реагирования '''

period2=30
''' время работы помпы '''

closed=1
''' дверь при запуске (закрыта) '''

closed2=1
''' дверь при запуске (закрыта) '''

def relay(i, s, ip=LoranIP):
	url='http://{0}/cmd.cgi?cmd=OUT,{1},{2}'.format(ip, i, s)
	print(url)
	r=requests.get(url)
	print(r.status_code)
	print(r.text)

def relay2(i, s, ip=LoranIP):
	url='http://{0}/cmd.cgi?cmd=REL,{1},{2}'.format(ip, i, s)
	print(url)
	r=requests.get(url)
	print(r.status_code)
	print(r.text)


relay(2, 1)    
''' включил помпу закрытия огуречника '''
time.sleep(period2)
relay(2, 0)     
''' выключил помпу закрытия огуречника '''
relay2(3, 1) 
''' включил помпу закрытия помидорника '''
time.sleep(period2)
relay2(3, 0)
''' выключил помпу закрытия помидорника '''
relay(6, 0)	   
''' погасил индикатор открытого помидорника '''
relay(12, 0)	
''' погасил индикатор открытого огуречника '''
	
while True:

	f=open(file, 'r')
	s=f.readlines()[-1]
	s=s[s.find('>')+1:]
	li=s.strip().split(' ')
		
	parnik=float(li[7].split('=')[1].replace(',', '.')) 
	''' запрос температуры огуречника '''
		
	if parnik>Tmax_parnik and parnik<Tglyk and closed:
		relay(1, 1)  
		''' включил помпу открытия огуречника '''
		time.sleep(period2)
		relay(1, 0)         
		''' выключил помпу открытия огуречника '''
		closed=0
		relay(12, 1)       
		''' включил индикатор открытого огуречника '''
		print("______________")
		print(parnik)
		print("OGURE4NIK_OPEN")
		print(" ")
		print(time.asctime())
		print("______________")
	
	if parnik<Tmin_parnik and not closed:
		relay(2, 1)       
		''' включил помпу закрытия огуречника '''
		time.sleep(period2)
		relay(2, 0)       
		''' выключил помпу закрытия огуречника '''
		closed=1
		relay(12, 0)   
		''' погасил индикатор открытого огуречника '''
		print("______________")
		print(parnik)
		print("OGURE4NIK_CLOSED")
		print(" ")
		print(time.asctime())
		print("______________")
		
	''' скрипт второго парника '''
	
	f=open(file, 'r')
	s=f.readlines()[-1]
	s=s[s.find('>')+1:]
	li=s.strip().split(' ')
	
	parnik2=float(li[3].split('=')[1].replace(',', '.'))
	''' запрос температуры огуречника '''
	
	if parnik2>Tmax_parnik2 and parnik2<Tglyk and closed2:
		relay2(2, 1)
		''' включил помпу открытия помидорника '''
		time.sleep(period2)
		relay2(2, 0)
		'''выключил помпу открытия помидорника '''
		closed2=0
		relay(6, 1)
		''' включил индикатор открытого помидорника '''
		
		print("______________")
		print(parnik2)
		print("POMIDORNIK_OPEN")
		print(" ")
		print(time.asctime())
		print("______________")
		
		
	if parnik2<Tmin_parnik2 and not closed2:
		relay2(3, 1)          
		''' включил помпу закрытия помидорника '''
		time.sleep(period2)
		relay2(3, 0)         
		''' выключил помпу закрытия помидорника '''
		closed2=1
		relay(6, 0)    
		''' погасил индикатор открытого помидорника '''
		print("______________")
		print(parnik2)
		print("POMIDORNIK_CLOSED")
		print(" ")
		print(time.asctime())
		print("______________")
	 
	time.sleep(period)
	
