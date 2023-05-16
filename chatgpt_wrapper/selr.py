import pyautogui    
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pyperclip import copy, paste
import os
from pprint import pprint
import re
import traceback
from datetime import datetime, timedelta
from select import select
from time import *
from urllib.parse import urlparse

import pause
from pymsgbox import *
from pyperclip import *
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.remote import remote_connection
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from utils import foreground


# from seleniumrequests.request import RequestsSessionMixin


class SessionRemote(webdriver.Remote):
    name = 'chrome'
    def start_session(self, desired_capabilities, browser_profile=None):
        w3c = True

    def check_element_exists_by_css(self,css):
        try:
            webdriver.find_element(By.CSS_SELECTOR, css)
        except NoSuchElementException:
            return False
        return True
    def get2(self,url):
        if self.current_url != url:
            self.get(url)
            
    def fetch_tabs(self,debug=0):
        self.tabs = {}
        self.tabs_url = {}
        for i in self.window_handles[::-1]:
            self.switch_to.window(i)
            # print tab index
            if debug:
                print(self.current_url)
            if not self.current_url:continue
            c = any(self.current_url.startswith(protocol) for protocol in ['file://', 'chrome://', 'about:', 'localhost','chrome-extension://','devtools://'])
            if c:
                continue
            domain = urlparse(self.current_url).netloc
            self.tabs_url[self.current_url] = i
            try:
                domain_name = domain.split('.')[-2]
            except Exception as e:
                print(domain)
                raise e
            
            if domain_name not in self.tabs:
                self.tabs[domain_name] = i
            elif domain_name+'3' not in self.tabs:
                self.tabs[domain_name + '3'] = i
        return self.tabs, self.tabs_url
    tabs = {}
    tabs_url = {}
    
    def move_and_click(self, selector):
        print(selector)
        element = self.find_element(By.CSS_SELECTOR, selector)
        x,y = element.location['x'], element.location['y']
        print(f"$('{selector}').")
        print(x,y);exit()
        pyautogui.moveTo(x, y, .4, pyautogui.easeOutQuad)   
        element.click()
        sleep(.5)

    def switch_to_tab_by_url(self, tab):
        if not self.tabs_url.get(tab):
            self.tabs, self.tabs_url = self.fetch_tabs()
        self.switch_to.window(self.tabs_url[tab])
    def switch_to_tab(self, tab):
        if not self.tabs:
            self.tabs, self.tabs_url = self.fetch_tabs()
        self.switch_to.window(self.tabs[tab])
b = None
folder_path = os.path.dirname(os.path.realpath(__file__))

a = folder_path+ '/sr'
a = (open(a). read())
exec(a)
def bcu(): return b.current_url


def bes(a):
    a = re.sub(r'(?<!\\)\$', 'document.querySelector', a)
    a = a.replace(r'\$', '$')
    return b.execute_script(a)


bfc = lambda x:b.find_element(By.CSS_SELECTOR,x)
# bfcs = lambda x:b.find_elements(_by_css_selector
# bfx = lambda x:b.find_element(by_xpath
# bfxs = lambda x:b.find_elements(_by_xpath
driver = b
browser = b
