#import asyncio




def my_bot(text=None):
    TOKEN=bot1_token='6492031694:AAEHG9PFz2_CniijJFAWM2p2rw51How-S-Y'
    
    url =f'https://api.telegram.org/bot{TOKEN}/sendmessage?chat_id=-1001571458368&amp'
    data ={'text':text}
    r= requests.get(url,params=data)

while 1 :
 my_bot(text='salam')
 time.sleep(12)
