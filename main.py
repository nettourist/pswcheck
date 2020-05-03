# -*- coding: utf-8 -*-
# -*- vk.com/nettourist -*-
import requests

response = requests.get('https://raw.githubusercontent.com/nettourist/pswcheck/master/psw')
check = response.text.strip()
print (check)

if check == '123':
    print ('Ok.')
else:
    print ('Not ok.')
