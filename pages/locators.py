from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGSTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGSTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGSTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
