import webbrowser
from random import randint
url=['http://google.co.kr','http://www.facebook.com','http://www.yahoo.com']
x=url[randint(0, 2)]
webbrowser.open(x, new=2)
