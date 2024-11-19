from selenium.webdriver.common.by import By


class Homepage:
    PAGE_URL = "https://www.saucedemo.com/"

    text_fields = {
        "Username": (By.ID, "user-name"),
        "Password": (By.ID, "password")
    }

    navigation_buttons = {
        "Login": (By.ID, "login-button")
    }

    messages = {
        "login error": (By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3")
    }

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.PAGE_URL)

    def close_page(self):
        self.driver.quit()

    def fill_out_field(self, field, text):
        self.driver.find_element(*self.text_fields[field]).send_keys(text)

    def click_button(self, button):
        self.driver.find_element(*self.navigation_buttons[button]).click()

    def get_error_message(self):
        return self.driver.find_element(*self.messages["login error"]).text
