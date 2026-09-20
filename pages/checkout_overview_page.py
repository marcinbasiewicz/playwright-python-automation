from playwright.sync_api import Page


class CheckoutOverviewPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_title = page.locator('[data-test="title"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.item_total_price = page.locator('[data-test="subtotal-label"]')
        self.inventory_item_price = page.locator('[data-test="inventory-item-price"]')

    def finish_checkout(self):
        self.finish_button.click()

    def get_sum_of_item_prices(self):

        prices = self.inventory_item_price.all_text_contents()

        total = 0

        for price in prices:
            price = price.replace("$", "")
            price = float(price)
            total += price

        return total

    def get_item_total(self):

        price = self.item_total_price.text_content()
        price = price.replace("Item total: $", "")
        price = float(price)
        return price
