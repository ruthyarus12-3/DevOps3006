from selenium import webdriver
import selenium

def test_scores_service(url):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(url)
    driver.close()
