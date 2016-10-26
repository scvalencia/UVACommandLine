from fabric import colors

VERSION = '1.2'
YEAR = '2014'
AUTHORS = 'Reactive Team'
params = {"version" : VERSION, "year" : YEAR, "authors" : AUTHORS}

HEADER = '''
\033[35m .----------------.  .----------------.  .----------------.\033[0m  
\033[35m| .--------------. || .--------------. || .--------------. |\033[0m   UVAcl %(version)s
\033[35m| | _____  _____ | || | ____   ____  | || |      __      | |\033[0m   Copyleft %(authors)s %(year)s
\033[35m| ||_   _||_   _|| || ||_  _| |_  _| | || |     /  \     | |\033[0m   This is free software.
\033[35m| |  | |    | |  | || |  \ \   / /   | || |    / /\ \    | |\033[0m   There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
\033[35m| |  | '    ' |  | || |   \ \ / /    | || |   / ____ \   | |\033[0m   PARTICULAR PURPOSE.
\033[35m| |   \ `--' /   | || |    \ ' /     | || | _/ /    \ \_ | |\033[0m
\033[35m| |    `.__.'    | || |     \_/      | || ||____|  |____|| |\033[0m   Type help, to see the manual.    
\033[35m| |              | || |              | || |              | |\033[0m   Type quit, to quit the session.  
\033[35m| '--------------' || '--------------' || '--------------' |\033[0m   
\033[35m '----------------'  '----------------'  '----------------' \033[0m
''' % params

WRONG_COMMAND = 'Did you mean'

FINAL_MESSAGE = 'Bye'

PERSISTENCE_FILENAME = 'user_info'

MANUAL = '''\n\033[1m    UVACommandLineClient\'s manual\033[0m:
  
    Type submit to submit a problem.
    Type msubs to see your submissions.
    Type stats to see your statistics.
    Type browse to browse a problem.
    Type whoami to see the current user.
    Type help to print this message.
  '''

SAVING_DATA = 'Saving data: '

WELCOME_MESSAGE = 'Hi, it seems that you are new to me. Let me know your information.'

FINE_DATA_INFO = 'Data saved successfully\a'

WRONG_USERNAME = 'Wrong username.\a'

WRONG_PASSWORD = 'Wrong password.\a'

FLAG_BASED_AUTH_ERROR = 'Sorry, you are not logged in, to begin, launch the \
app in interactive mode and log in.'