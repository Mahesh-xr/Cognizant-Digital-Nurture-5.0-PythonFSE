# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service)

# driver.get(
#     "https://www.lambdatest.com/selenium-playground/simple-form-demo"
# )

# # CSS Selector using ID
# element1 = driver.find_element(
#     By.CSS_SELECTOR,
#     "#user-message"
# )

# # CSS Selector using attribute
# element2 = driver.find_element(
#     By.CSS_SELECTOR,
#     "[name='user-message']"
# )

# # CSS Selector using parent-child
# element3 = driver.find_element(
#     By.CSS_SELECTOR,
#     "div > input"
# )

# print(element1)
# print(element2)
# print(element3)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get(
    "https://www.lambdatest.com/selenium-playground/checkbox-demo"
)

# Locate using exact text
label = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print(label.text)

# Locate all labels containing "Option"
labels = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

for item in labels:
    print(item.text)

driver.quit()