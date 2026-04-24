from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Caminho para o chromedriver
def abrir_google():
    chrome_driver_path = './chromedriver-mac-arm64/chromedriver'
    service = Service(executable_path=chrome_driver_path)
    browser = webdriver.Chrome(service=service)
    browser.get('https://www.google.com')
    time.sleep(5)
    browser.quit()

if __name__ == '__main__':
    abrir_google()