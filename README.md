# ISIT 360 Database Application Development

## Setup & Dependencies

### Windows

Run these three commands in PowerShell (Run as Administrator):

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
>
    choco install git vscode python
>
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -

These tools should now be installed, which we'll be using throughout the course:

- [Chocolatey](https://chocolatey.org/) [command-line based app install manager]
- [Git](https://git-scm.com/) [source code manager]
- [Code](https://code.visualstudio.com/) *(Visual Studio)* [fancy text editor]
- [Python](https://www.python.org/) [programming language runtime]
- [Poetry](https://python-poetry.org/) [python package/project manager]

### Mac

Run these three commands in Terminal:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>
    brew install git vscode python
>
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

These tools should now be installed, which we'll be using throughout the course:

- [Homebrew](https://brew.sh/) [command-line based app install manager]
- [Git](https://git-scm.com/) [source code manager]
- [Code](https://code.visualstudio.com/) *(Visual Studio)* [fancy text editor]
- [Python](https://www.python.org/) [programming language runtime]
- [Poetry](https://python-poetry.org/) [python package/project manager]
