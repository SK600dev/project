import sys

import requests

token = '6874803413:AAEZBIpD2PGpF32j5pSnEzeFHJXVGiUC5eU'

request = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(token, sys.argv[1], sys.argv[2])
requests.get(request)
