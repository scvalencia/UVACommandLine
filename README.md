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

Once you are logged, you 

One-time setup:
<pre>
> tpl add path/to/template.cpp 

> set-editor vim
Editor set

> add uva john.doe my-secret-password
Account added

> use uva john.doe
Account set as current

> tpl show
lang     | file path
C++        path/to/template.cpp

> set-browser "path to browser"
Browser set
</pre>

Sample usage:
<pre>
> view 123
... opens browser to show problem 123 ...

> edit 123.cpp
.... spawn the template and launch vim ....
Edit done

> send 123
Inferred Problem #: 123
       Source file: 123.cpp
Logging in...
Sending code...
Sent OK

> stat
Getting status...
Sub Id    | Prob # |      Verdict     |  Lang  | Runtime |  Rank |      Sub Time
 11638387      123           accepted      C++     0.008     519   2013-04-20 13:35:04
 11629565      125           accepted      C++     0.016     900   2013-04-19 00:16:01
...
</pre>

Non-interactive usage:
<pre>
lucastan$ node uva-node status
Getting status...
Sub Id    | Prob # |      Verdict     |  Lang  | Runtime |  Rank |      Sub Time
 11638387      123           accepted      C++     0.008     519   2013-04-20 13:35:04
 11629565      125           accepted      C++     0.016     900   2013-04-19 00:16:01

lucastan$
</pre>







UVA-NODE is an interactive shell (REPL) in which you can type commands 
of the syntax: `<action> <arg1> <arg2> ...`

Each `arg` can be surrounded by quotes if there are spaces in it.
For example, `"/path/with spaces/"` or `'/path/with spaces/'`. You can use either
double or single quote, but must be matching.

Quotes cannot be used for the `add` action as your password might contain quotes.

For your convenience, 
the program will in many cases auto-detect the language based on the file name extension:

| Ext.        | Lang |
| ---         | ---  |
| .java       | Java |
| .cpp / .cc  | C++  |
| .c          | C    |
| .pascal / .pas / .p |  Pascal |

The following are possible actions:

tpl
---
Syntax: 
- tpl add {filePath} 
- tpl remove {lang}
- tpl show

All template settings are global across your accounts, but still specific to
the OS user (computer user).

tpl add {filePath}: 
- Adds or replaces an existing template path. The program will merely store the file path,
and will *not* copy the template file to another place. This behavior ensures the program 
always use the latest version of your template without having you to re-add.
- It is recommended that filePath is absolute, instead of relative, to avoid path issues,
  and make it independent of where you launch uva-node.
- Will detect language based on file extension.
- The file must be in the UTF-8 or ASCII encoding. If you have no clue what it is,
  don't worry about it. 
- In the template file, put the string `$caret_start$` *in a line of its own* at where you want to start typing the code.   
The entire line containing `$caret_start$` will be replaced with a blank line.

Sample template file:
<pre>
#include &lt;stdio.h&gt;

int main()
{
    $caret_start$
    return 0;
}
</pre>

tpl remove {lang}: 
- Removes the template path but will *not* delete the template file.
- {lang} is cpp / c / java / pascal / pas / p.

tpl show: 
- Shows all template settings.

set-editor
----------
Syntax: set-editor {path to editor}

Sets editor command. Usually `vim` or `vi`. Actually any editor will do.
Try experimenting on your own. Only `vi` / `vim` is tested with.

If the command is relative, it must exist in one of the paths specified by the $PATH environment variable.

If the path contains spaces, please surround with quotes like this `"/path/Program 123"`

<strong>Windows users:</strong>
- If you are using Git bash shell, you can use something like `"C:\program files\Git\share\vim\vim73\vim.exe"`.

- If you are using MinGW, you could use a path such as `C:\MinGW\msys\1.0\bin\vim.exe`

- If you do not want to use absolute paths, you can simply use `vim.exe` but please
  ensure it is in your PATH environment variable.

- It is also possible to use a GUI-based editor such as gvim

edit
----
Syntax: edit {srcFilePath}

If {srcFilePath} does *not* exist, and there is a template configured for
the language, the program will spawn the template and launch the editor.
If there is no template, a blank file will be created instead.

Otherwise, if {srcFilePath} exists, the program will launch the editor only.

add
----
Syntax: add {type} {username} {password}

Adds a new user account, or replace an existing one 
with the same type and username. The replacing behavior is useful for updating
password.

All accounts will be preserved even after you quit the program.

Currently uva is the only supported type.

remove
------
Syntax: remove {type} {username}

Removes a user account. You cannot remove an account that is set as current.

use
---
Syntax: use {type} {username} OR use

Sets a user account as current.
If both {type} and {username} are omitted, sets the current account to none.
The current account setting will be preserved even after you quit the program.

show
----
Syntax: show 

Shows all user accounts

send
----
Syntax: send {problem #} {fileName/Path} OR send {fileName/Path} OR send {problem #}

Sends a code file using the current account. 
{fileName/Path} is relative to the current directory, which
is where you ran the `node ...` command to start uva-node

The program will auto-detect the language using the file name extension.

If only {problem #} is specified, the program will detect the source file in the current directory
whose name contains the {problem #}. For example, if there is an existing file 00123.cpp and you specify
the problem # as 123, the program will assume you want to send 00123.cpp (leading zeroes are ignored).
If multiple files are found to contain the problem # in their names, the program will abort sending.
For example, if there are files 123-a.cpp and 123.cpp, the program will not be able to know which one
you want to send.
In this case, you'd have to specify both the {problem #} and {fileName} args.

If only {fileName/Path} is specified, the program will infer the problem # from the file name.
The problem # is assumed to be the first integer found in the file name, ignoring leading zeroes.

status / stat
-------------
Syntax: status/stat {count}

Prints out the latest {count} submissions for the current account.
{count} defaults to 10 if omitted.

set-browser
-----------
Syntax: set-browser {path} [{arg1} {arg2} ...]

Sets the command for opening the browser to view a question. Args are optional.

If the path or args contains spaces, please surround with quotes.

**Mac OS users**:

* You may want to use the "open" tool which will open in your default browser.
For example, `set-browser open`.

get-browser
-----------
Syntax: get-browser 

Prints out the browser command including args.

view
----
Syntax: view {prob #}

Opens the problem webpage in the browser.

quit / exit
-----------
Saves all settings including account info and exits the program.

## TODO
- Use a queue of submissions whenever UVA is down
- Get statistics of problem
- Allow to edit a source in the program
- Autodetect solution's file
- Be able to run it without using `python uva.py`, just `uva`
- Detect files in the current folder
- Allow to read a problem from the command line
- Allow to open a problem in the web-browser
- Background submission
- Progress bar
- Data encryption


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



