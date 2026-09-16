from playwright.sync_api import Page


class CheckoutCompletePage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_title = page.locator('[data-test="title"]')
