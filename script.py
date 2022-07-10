from numpy import var
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import argparse

parser = argparse.ArgumentParser(description="Scrap information for given LinkedIn URL")
parser.add_argument('url',type=str,nargs=1,help="The public profile URL to scrap details from")
args = parser.parse_args()

#Driver and URL setup
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
url = args.url[0]