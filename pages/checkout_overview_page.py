from playwright.sync_api import Page


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_title = page.locator('[data-test="title"]')
        self.finish_button = page.locator('[data-test="finish"]')

    def finish_checkout(self):
        self.finish_button.click()
