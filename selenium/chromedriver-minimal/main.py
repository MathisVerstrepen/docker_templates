from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver 


class Selenium_turtle:
    def __init__(self):
        caps = DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True      # accept insecure certs
        caps['HTTPKeepAlive'] = True            # keep alive http connection
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")                   # Runs Chrome in headless mode.
        chrome_options.add_argument('--disable-dev-shm-usage')      # overcome limited resource problems
        chrome_options.add_argument("--start-maximized")            # open Browser in maximized mode
        chrome_options.add_argument("--no-sandbox")                 # Bypass OS security model
        chrome_options.add_argument('--disable-gpu')                # disable GPU
        chrome_options.add_argument('--disable-plugins')            # disable plugins
        chrome_options.add_argument('--disable-infobars')           # disable infobars
        chrome_options.add_argument('--disable-extensions')         # disable extensions
        
        
        webdriver_service = Service("/usr/lib/chromium/chromedriver")                                                       # specify the path to chromedriver
        self.driver = webdriver.Chrome(service=webdriver_service, options=chrome_options, desired_capabilities=caps)        # start the webdriver

        print("Selenium_turtle is ready to go!")
        
    def get(self, url):
        self.driver.get(url)
        print(self.driver.title)

if __name__ == '__main__':
    turtle = Selenium_turtle()
    turtle.get("https://www.google.com")