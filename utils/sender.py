import sys

import requests

token = '1731506104:AAFTSw03X1CIQf8zv4TJ-AHto7a0gAFRjrU'

request = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={sys.argv[1]}&text={sys.argv[2]}"
requests.get(request)
