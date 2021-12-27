import os
import sys
from os import rename

#import matplotlib
import requests

r = requests.get("https://coreyms.com")
print(r.status_code)
test = "Test"
name = input('your Name?')
print(f'Hello {name}')
