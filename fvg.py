from urllib.request import urlopen, Request
import requests
import time
from bs4 import BeautifulSoup
headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
print('Login Fshare')
mail = input('Enter your mail: ')
psss = input('Enter your password: ')
print('Loading page...')
login_data = {
    'LoginForm[email]': mail,
    'LoginForm[password]': psss,
    'LoginForm[rememberMe]':'0'
}
with requests.Session() as s:
    url = 'https://www.fshare.vn/site/login'
    req = Request(url,headers = headers)
    webpage = urlopen(req).read()
    #r = s.get(url, headers = headers)
    soup = BeautifulSoup(webpage, 'html.parser')
    login_data['_csrf-app'] = soup.find('input', attrs={'name':'_csrf-app'})['value']
    print('Connecting account ...')
    r = s.post(url, data= login_data,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    k=soup.title
    if str(k.text) == 'File Manager - Fshare' :
        print('Login Success')
    else:
        print('Login Fail')
        print('Program exit')
        exit()
    while True :
        try:
            print("\n| Enter 'q' to exit " )
            url_get = input('| Paste link file to Download: ')
            if url_get == 'q' :
                print('exit')
                break
            r = s.get(url_get)
            soup = BeautifulSoup(r.content, 'html.parser')
            get_linkcode = soup.find('input', attrs={'id':'linkcode'})['value']
            get_data = {
                'linkcode': get_linkcode,
                'withFcode5': '0'
            }
            get_data['_csrf-app'] = soup.find('input', attrs={'name':'_csrf-app'})['value']
            m=s.post('https://www.fshare.vn/download/get', data= get_data,headers=headers)
            print('link download: ')
            print(m.json()['url'])
        except:
            print('Get link fail ! Try again...')
