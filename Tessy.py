import requests
import json
from myconfig import *

response = requests.get("https://google.com")
print(response.status_code)

