from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.ycombinator.com/")

#getting title from the .title method
title_from_method = driver.title
print(title_from_method)

#getting title from element xpath
title_element_from_html = driver.find_element(By.XPATH, "/html/head/title")
page_title = title_element_from_html.get_attribute("innerText")
print(page_title)
