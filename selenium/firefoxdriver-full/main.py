from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver 
# from seleniumwire import webdriver 


class Selenium_turtle:
    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")                   # Runs Firefox in headless mode.
        firefox_options.add_argument('--disable-dev-shm-usage')      # overcome limited resource problems
        firefox_options.add_argument("--start-maximized")            # open Browser in maximized mode
        firefox_options.add_argument("--no-sandbox")                 # Bypass OS security model
        firefox_options.add_argument('--disable-plugins')            # disable plugins
        firefox_options.add_argument('--disable-infobars')           # disable infobars
        firefox_options.add_argument('--disable-extensions')         # disable extensions
        
        firefox_options.set_capability('acceptInsecureCerts', True)  # accept insecure certs
        firefox_options.set_capability('httpKeepAlive', True)        # keep alive http connection

        webdriver_service = Service("/usr/local/bin/geckodriver")
        self.driver = webdriver.Firefox(service=webdriver_service, options=firefox_options) 

        print("Selenium_turtle is ready to go!")
        
    def get(self, url):
        self.driver.get(url)
        print(self.driver.title)

if __name__ == '__main__':
    turtle = Selenium_turtle()
    turtle.get("https://www.google.com")