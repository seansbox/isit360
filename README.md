# ISIT 360 Database Application Development

## How to install the tools for this course...

### Windows

Run these three commands in PowerShell (Run as Administrator):

    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
>
    choco install git vscode python
>
    python -m pip install pipenv poetry

### MacOS

Run these three commands in macOS Terminal:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>
    brew install git vscode python
>
    python -m pip install pipenv poetry

## You should now have these tools installed...

- [Chocolatey](https://chocolatey.org/) (Windows command-line app installer/manager)
- [Homebrew](https://brew.sh/) (macOS command-line app installer/manager)
- [Git](https://git-scm.com/) (source code versioning/manager)
- [Visual Studio Code](https://code.visualstudio.com/) (excellent text/dev editor)
- [Python](https://www.python.org/) (programming language runtime)
- [PipEnv](https://pipenv.pypa.io/) (python package/project manager)
- [Poetry](https://python-poetry.org/) (python package/project manager)

## Here is a work-in-process module outline...

- M01 Welcome and Python Crash Course *(ch1,4)*
- M02 Files, Formats, and Serialization *(ch5,6)*
- M03 Structuring Data and Querying It *(ch7,8)*
- M04 Mapping Objects and Speaking Excel *(ch9,10)*
- M05 Data Without Structure, with Structure *(ch11,12)*
- M06 Building the Blocks of an MVC App *(dj1,2)*
- M07 Making Templates and Displaying Data *(dj3,6)*
- M08 Data Change Forms and Permissions *(dj4,7)*
- M09 Deploying a Database Application *(hero)*
- M10 Advanced Data Features & Strategies
