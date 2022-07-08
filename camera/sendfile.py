import requests
import time
from datetime import datetime
import fnmatch
import os

period = 3600

def send_image(y, m, d, h):
    dir='C:/DVR/Picture/{0}{1}{2}/{3}/'.format(y, m, d, h)
    pattern = 'snap{0}{1}{2}_{3}1*.jpg'.format(y, m, d, h)
    for name in os.listdir(dir):
        if fnmatch.fnmatch(name, pattern):
            print('Sending image:', end=' ')
            print(name)
            fullpath = dir+name
            files = {'photo':open(fullpath,'rb')}
            resp = requests.post('https://api.telegram.org/botTOKEN/sendPhoto?chat_id=-CHAT_ID', files=files)
            print('Waiting 3600 sec.')
            time.sleep(period)

while True:
    now = datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")

    send_image(year, month, day, hour)
    print('Waiting for 5 sec.')
    time.sleep(5)
