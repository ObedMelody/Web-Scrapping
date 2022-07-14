# import sys
# from termcolor import colored, cprint
#
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')
#
# print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
# print_red_on_cyan('Hello, World!')
# print_red_on_cyan('Hello, Universe!')
#
#
#
# attrib +h c:\documents
from bs4 import BeautifulSoup

with open('Index.html') as web:
    file = web.read()

    soup = BeautifulSoup(file, 'lxml')
   # print(soup.prettify())
    for x in soup:
        print(x)

    letters = soup.find_all('h2')
    for letter in letters:
        print(letter.text)