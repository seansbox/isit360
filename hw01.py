import requests
from termcolor import colored

class Monkey:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return colored(self.name, 'red')

class CuriousMonkey(Monkey):
    def __str__(self):
        return colored(self.name, 'yellow')

# r = requests.get('https://api.ipify.org?format=json')
# print(colored(r.json(), 'red'))

m = Monkey('Carl')
print(m)

m2 = CuriousMonkey('George')
print(m2)

# poetry init  <== build a new project
# poetry add   <== add a new dependency/module
# poetry shell <== run your app/project (python hw01.py)
# poetry build <== later on, fancy stuff
