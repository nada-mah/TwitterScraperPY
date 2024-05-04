import re
import schedule 
import time
from scraper import get_data

def is_valid_url(url):
    url_regex = re.compile(r'https://twitter.com/[a-zA-Z0-9./]+')
    return bool(url_regex.match(url))

account_list = []

for i in range(2):
    ACC = str(input("Enter 10 twitter accounts : "))
    if is_valid_url(ACC):
        account_list.append(ACC)
    else:
       print('Please enter valid url') 


Ticker = str(input('Enter stock symbol: '))
interval = int(input('Enter time interval in min: '))

get_data(account_list,Ticker,interval)
schedule.every(interval).minutes.do(lambda :get_data(account_list,Ticker,interval)) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 
