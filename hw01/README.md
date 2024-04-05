# Welcome to Database Application Development!

## The course in a nutshell...

1. Learn some _development_ stuff
2. Learn some _database_ stuff
3. Learn some _application_ stuff

## In this module...

Just in case some folks are joining us with **_zero programming experience_**, we're going to kick things off with a crash course in **_Python_** programming. Start out by reading the **_first 4 chapters_** of the textbook. We will **_not_** be reading this much regularly! Module 01 will be a lot of review for some, and a _lot_ to digest for others. Just do your best, and keep in mind you won't need to retain all of this, just the _"good parts"_ which we'll be talking about in class. We'll go over the basics again and again throughout the course.

_I'm going to schedule our first live session right away, because I'm going to actually do this homework (HW01) in the session for (and I hope along side) the class._

Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion.

# Setting Up Our Development Stack

We'll be using several tools/applications throughout this course. This "development stack" includes the following tools:

- [Chocolatey](https://chocolatey.org/) _(command-line based application install manager)_<br>
  or [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/) _(same thing)_
- [Git](https://git-scm.com/) _(source code manager)_
- [Code](https://code.visualstudio.com/) (Visual Studio) _(fancy text editor)_
- [Python](https://www.python.org/) _(programming language and runtime)_
- [Pipenv](https://github.com/pypa/pipenv) _(python package/project manager)_

Each are linked above, and I encourage you to familiarize yourself with them. We'll be going through them one-by-one in the first session as well.

## Installing The Stack

### Using Chocolately

We'll use **Windows PowerShell** to install these needed tools. Make sure to right-click and run **PowerShell** _as Administrator_, and execute the following commands. At the end of the course, you can use **chocolatey** to remove all of these tools as well. First we'll install **chocolately**:

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Ugh, yeah that is all a single command. Then run these on at a time...

    choco install -y vscode python

>

    choco install -y git.install --force --params "'/GitAndUnixToolsOnPath /WindowsTerminal /NoAutoCrlf'"

>

    choco install -y sqlite mongodb

>

    choco upgrade all -y

### Using WinGet Instead of Chocolately

If you _don't_ have **choco** installed, and need/want to use WinGet, try these commands instead. We'll still use **Windows PowerShell** to install these needed tools. Make sure to right-click and run **PowerShell** _as Administrator_, and execute the following commands:

    winget install python.python.3.11 git.git sqlite.sqlite  --accept-source-agreements --accept-package-agreements

>

    winget install vscode mongodb --accept-source-agreements --accept-package-agreements

### Finally, Install Some Python Tools

You may have to close and re-open PowerShell (again, as Administrator) and then run these commands...

    python -m pip install --upgrade pip pipenv pipupgrade

>

    python -m pip install --upgrade sqlite_web streamlit

>

    pipupgrade --latest

What are these?!

- **PIP.** Python's builtin package (external dependencies) manager.
- **PIPUPGRADE.** PIP doesn't have a great way to upgrade all of the installed packages. The pipupgrade utility will help us get them all upgraded at ONCE!
- **PIPENV.** If is very common for different Python projects/folders to require different versions of the same dependencies. PIPENV makes this really easy to manage by managing local 'Pipfile's and unique "python environments."

Now you should be able to run the following commands and see what versions of python/pip you have installed:

    C:\Windows\System32>python --version
    Python 3.11.3
    
    C:\Windows\System32>pip --version
    pip 24.0 from C:\Python311\Lib\site-packages\pip (python 3.11)
    
    C:\Windows\System32>pipenv --version
    pipenv, version 2023.12.1

Close out your PowerShell window (running as Administrator). We shouldn't really need to run any shells as Administrator again until the end of the course when it's time to uninstall.

TODO: Might as well put the uninstall instructions here, for example:

    winget uninstall python --purge

# Our First Project

Just the hints...

    mkdir hw01

>

    cd hw01

>

    code .

>

    (edit hw01.py)

>

    pipenv install requests termcolor (you should use different packages)

>

    pipenv run python hw01.py

>

    bundler

# Completing the Homework

Create a **_hw01_** project/folder that demonstrates the following:

- Contains a Python script named **_hw01.py_**
- Imports an external, third-party module
- Defines a class and uses inheritance
- Leverages `pipenv` (and a Pipfile) to manage its dependencies
- Contains at least 20 lines of (non-filler) code
- Does not directly copy examples from the book or class

Save a screenshot of your app _(successfully running)_ to `screenshot.jpg` in your project folder. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.
