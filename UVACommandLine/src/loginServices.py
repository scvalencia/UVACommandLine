from bs4 import BeautifulSoup
import requests

GET = '0'
POST = '1'

HOME = 'http://uva.onlinejudge.org/'

ANSI_C = '1'
JAVA = '2'
C_PLUS = '3'
PASCAL = '4'
C_PLUS_11 = '5'

session = requests.session()

def get_params(form):
    params = {}
    inputs = form.find_all('input')
    for i in inputs:
        name = i.get('name')
        value = i.get('value')
        if name: 
            params[name] = value if value else '' 

    return params

def get_soup(url, action = GET, params = {}):
    request = None

    if action == GET: 
        request = session.get(url)
                                               
    elif action == POST: 
        request = session.post(url, params) 
                                                         
    html = request.text
    soup = BeautifulSoup(html)
    return soup 

def make_login(username, password, url = HOME):
    soup = get_soup(url) 
    form = soup.find(id = "mod_loginform") 
    url = form['action'] 
    params = get_params(form) 
    params['username'] = username 
    params['passwd'] = password 
    soup = get_soup(url, action = POST, params = params) 
                                                   
    if soup.find(id = "mod_loginform"): 
        return False 
    else: 
        return True

def check_login(username, password, url = HOME):
    return make_login(username, password, url)