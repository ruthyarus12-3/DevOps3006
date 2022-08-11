import faker
import requests
from faker import Faker
from selenium import webdriver

print("------- 1 -------")
assert len((requests.get("https://api.github.com/users/avielb/repos")).json()) > 4

print("------- 2 -------")
faker = Faker()
for i in range(3):
    name = faker.first_name()
    assert 0 < ((requests.get(f"https://api.agify.io/?name={name}")).json())['age'] < 120

print("------- 3 -------")
response = (requests.get("http://universities.hipolabs.com/search?country=Israel")).json()
assert len(requests.get("http://universities.hipolabs.com/search?country=Israel").json()) > 5

print("------- 4 -------")
my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com/")

title = my_driver.find_element("xpath",
                               "//div[@class='prose']//h2[contains(text(), 'Y Combinator created a new model')]").text
assert title == "Y Combinator"

print("------- 5 -------")

my_driver.get("https://hub.docker.com")

title = my_driver.find_element("xpath",
                               "//div[contains(text(),'Welcome to Docker')]").text
assert title == "Docker Hub Container Image Library | App Containerization"
