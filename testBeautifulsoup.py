from bs4 import BeautifulSoup
import requests
import subprocess

html_file = requests.get('https://github.com/chidiebereojingwa/Hello_Microverse.git').text
soup = BeautifulSoup(html_file, 'lxml')
for x in soup:
    print(x)

