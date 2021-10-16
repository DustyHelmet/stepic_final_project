from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By



class PageObject(BasePage):
	def add_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()


	def should_be_add_to_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "add to basket button not found"