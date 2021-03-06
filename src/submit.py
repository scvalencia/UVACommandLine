from bs4 import BeautifulSoup
import os
import requests
import apiServices

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
    if not form:
        return False 
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

def get_code(path):
    code = ''
    in_file = open(path, 'r')
    for line in in_file: 
        code += line
    in_file.close()
    return code

def process_submission(form, code, language):
    url = HOME + form['action']
    params = get_params(form)
    name = form.textarea['name']
    params[name] = code
    params['language'] = language 
    get_soup(url, action = POST, params = params)

def make_submission(url, code, language):
    soup = get_soup(url)
    form = soup.find_all('form')[1]
    process_submission(form, code, language)

def sumbit_problem(usr, pswrd, lang, problem_url, file_name, path = os.getcwd()):
    total_path = os.path.join(path, file_name)
    if not os.path.isfile(total_path):
        print 'Not a file'
        return
    code = get_code(total_path)
    login = make_login(usr, pswrd)
    if login:
        make_submission(problem_url, code, lang)
    else:
        print 'Error while submitting'

def sumbit_problem_with_id(username, password, language, problem_id, file_name, path = os.getcwd()):
    base_url = 'http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=submit_problem&problemid='
    base_url += str(problem_id)
    base_url += '&category='
    sumbit_problem(username, password, language, base_url, file_name, path)

def sumbit_problem_with_number(username, password, lang, problem_number, filename, path = os.getcwd()):
    problem = apiServices.get_problem_by_number(problem_number)
    if problem == {}:
        print 'Wrong problem number'
        return
    else:
        problem_id = str(problem[u'pid'])
        sumbit_problem_with_id(username, password, lang, problem_id, filename)

def submit(username, password, lang, problem_number, filename, mode):
    if mode == 1:
        print '(C : 1, Java : 2, C++ : 3, Pascal : 4, C++ 11 : 5)'
        lang = raw_input("Language: ")
        problem_number = raw_input("Problem's number: ")
        filename = raw_input("File name: ")
        if lang and problem_number and filename:
            if lang not in [str(i) for i in range(1, 6)]:
                print 'Wrong language.'
                return
            if not problem_number.isdigit():
                print 'Wrong problem.'
                return
            if '.' not in filename:
                print 'You must specify the file extension.'
                return
            sumbit_problem_with_number(username, password, lang, problem_number, filename)

        else:
            print 'Wrong input.'
            return
    else:
        pass