from numpy import var
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import InvalidArgumentException
import argparse

parser = argparse.ArgumentParser(description="Scrap information for given LinkedIn URL")
parser.add_argument('url',type=str,nargs=1,help="The public profile URL to scrap details from")
args = parser.parse_args()

#Driver and URL setup
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
url = args.url[0]

try:
    driver.get(url)
    assert "https://www.linkedin.com/" in driver.current_url
    
except InvalidArgumentException:
    print("Not a valid URL")
except AssertionError:
    print("Not a LinkedIn URL")
