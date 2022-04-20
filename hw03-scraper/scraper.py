import time
import pickle
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Install Dependencies:
#   brew install chromedriver (macos terminal)
#   choco install chromedriver (windows powershell (as admin))
#   poetry add bs4 lxml selenium

class Scraper:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.url = None
        # We'll use these .dom_* variables to keep track of when we use find_fast_elements and save some parsing time
        self.dom_url = None
        self.dom_cache = None

    # Utility function for if we want save/load cookies between sessions
    def load_cookies(self, cookie_file):
        try:
            cookies = pickle.load(open(cookie_file, "rb"))
            for cookie in cookies:
                self.wd.add_cookie(cookie)
        except FileNotFoundError:
            pass

    # Utility function for if we want save/load cookies between sessions
    def save_cookies(self, cookie_file):
        pickle.dump(self.wd.get_cookies(), open(cookie_file, "wb"))

    # Load the page in Chrome
    def get_page(self, url):
        self.url = url
        self.wd.get(url)
    
    # Pause execution for seconds until we see the given DOM element
    def wait_for_element(self, xpath, seconds=2):
        WebDriverWait(self.wd, seconds).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    # Pause execution for seconds based on the system time
    def wait_for_seconds(self, seconds):
        time.sleep(seconds)

    # Uses Selenium to have the browser query the page using XPATH
    def find_live_elements(self, xpath):
        return self.wd.find_elements(By.XPATH, xpath)

    # Uses BeautifulSoup to parse the page and rapidly query it using XPATH
    def find_fast_elements(self, xpath, dom=None):
        if dom: return dom.xpath(xpath)
        if self.dom_url != self.url:
            soup = BeautifulSoup(self.wd.page_source, "html.parser")
            self.dom_url = self.url
            self.dom_cache = etree.HTML(str(soup))
        return self.dom_cache.xpath(xpath)
