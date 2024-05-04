import re
import schedule 
import time
from scraper import get_data

def is_valid_url(url):
    url_regex = re.compile(r'https://twitter.com/[a-zA-Z0-9./]+')
    return bool(url_regex.match(url))

# TEST ACCOUNTS 
account_list = ['https://twitter.com/RoyLMattox','https://twitter.com/Barchart',
                'https://twitter.com/CordovaTrades','https://twitter.com/AdamMancini4',
                'https://twitter.com/TriggerTrades','https://twitter.com/yuriymatso',
                'https://twitter.com/allstarcharts','https://twitter.com/ChartingProdigy',
                'https://twitter.com/warrior_0719','https://twitter.com/Mr_Derivatives'
                ]
# # uncomment to add twitter accounts
# for i in range(10):
#     ACC = str(input("Enter 10 twitter accounts one at a time : "))
#     if is_valid_url(ACC):
#         account_list.append(ACC)
#     else:
#        print('Please enter valid url') 


Ticker = str(input('Enter stock symbol: '))
interval = int(input('Enter time interval in min: '))

get_data(account_list,Ticker,interval)
schedule.every(interval).minutes.do(lambda :get_data(account_list,Ticker,interval)) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 
