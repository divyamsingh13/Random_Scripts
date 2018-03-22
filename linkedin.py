import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com?allowUnsupportedBrowser=true'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit?allowUnsupportedBrowser=true'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html,'lxml')
csrf = soup.find(id="loginCsrfParam-login")['value']

login_information = {
    'session_key':'shivavns101@gmail.com',
    'session_password':'Asqwerty123',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)

x = client.get('https://www.linkedin.com/in/divyamsingh13/')
s=BeautifulSoup(x.text,'lxml')