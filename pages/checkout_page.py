from playwright.sync_api import Page

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.continue_button = page.locator('[data-test="continue"]')
        self.error_message = page.locator('[data-test="error"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')


    def continue_checkout(self):
        self.continue_button.click()

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        