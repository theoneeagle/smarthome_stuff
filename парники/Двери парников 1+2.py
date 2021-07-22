import requests
import time

file='C:\\BM1707.dat'
LoranIP='192.168.3.101'

Tmax_parnik=24  # температура открытия
Tmin_parnik=22  # температура закрытия
Tmax_parnik2=24 # температура открытия
Tmin_parnik2=22 # температура закрытия
Tglyk=84
period=30       # частота считывания температуры и реагирования
period2=25      # время работы помпы
closed=1        # дверь при запуске (закрыта)
closed2=1       # дверь при запуске (закрыта)

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


relay(2, 1)  #  включил помпу закрытия огуречника 
time.sleep(period2)
relay(2, 0)  #  выключил помпу закрытия огуречника 

relay(9, 1)  #  включил помпу закрытия помидорника 
time.sleep(period2)
relay(9, 0)  #  выключил помпу закрытия помидорника 

relay(6, 0)	 #  погасил индикатор открытого помидорника 
relay(12, 0) #  погасил индикатор открытого огуречника 
	
while True:
	f=open(file, 'r')
	s=f.readlines()[-1]
	s=s[s.find('>')+1:]
	li=s.strip().split(' ')
		
	parnik=float(li[6].split('=')[1].replace(',', '.')) # запрос температуры огуречника 

	# print(time.asctime(), end =", ")
	# print("Current OGUR  temp:", end =" ")
	# print(parnik)

	if parnik>Tmax_parnik and parnik<Tglyk and closed:
		relay(1, 1)  #  включил помпу открытия огуречника 
		time.sleep(period2)
		relay(1, 0)  #  выключил помпу открытия огуречника 
		closed=0
		relay(12, 1) #  включил индикатор открытого огуречника

		print("____________________________")
		print("Temp:", end =" ")
		print(parnik, end =", ")
		print("OGURE4NIK_OPENED")
		print(" ")
		print(time.asctime())
		print("____________________________")
	
	if parnik<Tmin_parnik and not closed:
		relay(2, 1)    #  включил помпу закрытия огуречника 
		time.sleep(period2)
		relay(2, 0)    #  выключил помпу закрытия огуречника 
		closed=1
		relay(12, 0)   #  погасил индикатор открытого огуречника 

		print("____________________________")
		print("Temp:", end =" ")
		print(parnik, end =", ")
		print("OGURE4NIK_CLOSED")
		print(" ")
		print(time.asctime())
		print("____________________________")


	#  скрипт второго парника 
	
	f=open(file, 'r')
	s=f.readlines()[-1]
	s=s[s.find('>')+1:]
	li=s.strip().split(' ')
	
	parnik2=float(li[4].split('=')[1].replace(',', '.')) #  запрос температуры помидорника 

	# print(time.asctime(), end =", ")
	# print("Current POMID temp:", end =" ")
	# print(parnik2)


	if parnik2>Tmax_parnik2 and parnik2<Tglyk and closed2:

		relay(7, 1) #  включил помпу открытия помидорника 
		time.sleep(period2)
		relay(7, 0) # выключил помпу открытия помидорника 
		closed2=0
		relay(6, 1) #  включил индикатор открытого помидорника 
		
		print("____________________________")
		print("Temp:", end =" ")
		print(parnik2, end =" ")
		print("POMIDORNIK_OPENED")
		print(" ")
		print(time.asctime())
		print("____________________________")


	if parnik2<Tmin_parnik2 and not closed2:

		relay(9, 1)   # включил помпу закрытия помидорника
		time.sleep(period2)
		relay(9, 0)   #  выключил помпу закрытия помидорника 
		closed2=1
		relay(6, 0)   #  погасил индикатор открытого помидорника 

		print("____________________________")
		print("Temp:", end =" ")
		print(parnik2, end =" ")
		print("POMIDORNIK_CLOSED")
		print(" ")
		print(time.asctime())
		print("____________________________")
	 
	time.sleep(period)
