import requests
import time

file='C:\\BM1707.dat'
LoranIP='192.168.3.101'

Tmax_parnik=22 # температура включения вентиляторов 22
Tmin_parnik=20 # температура выключения вентиляторов 20
Tglyk=84
period=10 
closed=1       # вентиляторы при запуске (выключены)

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
#	print(li)
	parnik2=float(li[4].split('=')[1].replace(',', '.'))	# li[4] - четвертое значение из файла температуры (счет с нуля)
	print("POMIDORNIK_TEMP:", end =" ")
	print(parnik2)


	parnik=float(li[6].split('=')[1].replace(',', '.')) # li[6] - шестое значение из файла температуры (счет с нуля)
	print("OGURE4NIK_TEMP:", end =" ")
	print(parnik)

	# распечатка температур пом-ка и огур-ка



	# parnik2 - Помидорник (высокий)
	# parnik  - Огуречник (длинный)

	if closed==1:
		print("VENT_OFF")
		print("____________________________")
		
	if closed==0:
		print("VENT_ON")
		print("____________________________")
	
	if parnik2>Tmax_parnik and parnik2<Tglyk and closed:
		relay(1, 1)
		closed=0
		
	if parnik2<Tmin_parnik and not closed:
		relay(1, 0)
		closed=1
		
	time.sleep(period)
