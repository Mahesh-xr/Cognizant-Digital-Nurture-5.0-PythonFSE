import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, message):

    driver.get(
        "https://www.lambdatest.com/selenium-playground/simple-form-demo"
    )

    message_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "user-message")
        )
    )

    message_input.clear()
    message_input.send_keys(message)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "showInput")
        )
    )

    submit_button.click()

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "message").text == message
    )

    display = driver.find_element(By.ID, "message")

    assert display.text == message

# def test_simple_form_submission(driver):

#     driver.get(
#         "https://www.lambdatest.com/selenium-playground/simple-form-demo"
#     )

#     # Wait for the input field
#     message_input = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located(
#             (By.ID, "user-message")
#         )
#     )

#     message_input.clear()
#     message_input.send_keys("Hello Selenium")

#     # Wait for the button and click it
#     submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(
#             (By.ID, "showInput")
#         )
#     )

#     submit_button.click()

#     # Wait until the output text is updated
#     WebDriverWait(driver, 10).until(
#         lambda d: d.find_element(By.ID, "message").text == "Hello Selenium"
#     )

#     # Get the output element
#     display = driver.find_element(By.ID, "message")

#     assert display.text == "Hello Selenium"


# # def test_checkbox_demo(driver):

#     driver.get(
#         "https://www.lambdatest.com/selenium-playground/checkbox-demo"
#     )

#     checkbox = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//input[@type='checkbox']")
#         )
#     )

#     checkbox.click()

#     assert checkbox.is_selected()

#     checkbox.click()

#     assert not checkbox.is_selected()