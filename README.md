UVACommandLine
==============
`UVACommandLine` is an interactive command line utility to submit solutions to the UVA online judge, it also allows to check submissions and other statistics.

## Features

`UVACommandLine` offers the following features:

 * Command line submission
 * Remembers your account (username, id, password)
 * Check history of submissions
 * Fastest submission (non-interactive mode)
 * Implemented in [Python](https://www.python.org/) using a virtual env, so it's portable
 
## Requirements

- Python 2.7 +
- virualenv `pip install virtualenv`

## Installation

1.  Install [Python](https://www.python.org/) if you haven't.
2.  Download this [file](https://raw.githubusercontent.com/teamreactive/UVACommandLine/master/UVACommandLine/src/get-pip.py) and run in the downloads folder the following command: `python get-pip.py`
3. Download the client `git clone https://github.com/teamreactive/UVACommandLine`
4. Activate the virtualenviroment `source UVACommandLine/UVACommandLine/bin/activate`
4. Run the client: `cd UVACommandLine/UVACommandLine/src && python uva.py`
5. Submit your solutions, view your statistics

Soon: Installation via PIP: `pip install UVACommandLine`
 
## Usage

When you run `python uva.py` in the current virtuel enviroment, and you are not logged, you get a prompt to enter your account tuple (username, password)
    
![alt tag](https://raw.githubusercontent.com/teamreactive/UVACommandLine/master/UVACommandLine/docs/Main_page.png)

Once you are logged, you can type:




help
-------------
Syntax: `help`

Prints the menu 

whoami
-----------
Syntax: `whoami`

Prints the user information

msubs
-----------
Syntax: `msubs [itms]`

Prints the list of latest submissions by the user, the list should contains itms files. If itms is omitted, the systems asks for the items that you want to include.

![alt tag](https://raw.githubusercontent.com/teamreactive/UVACommandLine/master/UVACommandLine/docs/Table.png)

submit
----
Syntax: `submit`

Opens a dialog asking for the language, the problem, and the filename. It submit the solution iff UVA is available.

quit / exit
-----------
`quit`
Saves all settings including account info and exits the program.

If you have use the system at least once, you an use it in non-interactive mode:

* Help: `python uva.py -h`
* Five last submissions: `python uva.py -sb`
* A number of submissions: `python uva.py -sb {number}`

## TODO
- Use a queue of submissions whenever UVA is down
- Get statistics of problem
- Allow to edit a source in the program (Calling an editor, [vim](http://stackoverflow.com/questions/6309587/call-up-an-editor-vim-from-a-python-script), emacs, sublime, atom, ...)
- Autodetect solution's file
- Be able to run it without using `python uva.py`, just `uva`
- Detect files in the current folder
- Allow to read a problem from the command line
- Allow to open a problem in the web-browser
- Background submission
- Progress bar
- Data encryption
- Improve non-interactive mode
- Improve performance
- Muli-user enviroment (shared resources)
- Switch user account
- Sets a user account as current
- List all users
- Non-interactive mode submission
- Log in only once instead of logging in on every send
- Auto-retry submitting the solution (when UVA is down)
- Connects to UVAtoolkit

## Credits
- UVA website
- uHunt API
- Python
- Universidad de los Andes
- CCPL (Colombian Collegiate Programming League)

## Contributors

The initial prototype of `UVACommandLine` were pair programmed by [Sebastian Valencia](https://github.com/scvalencia) and [Juan Bages](https://github.com/jcbages). 

## License

None



