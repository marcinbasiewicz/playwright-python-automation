from playwright.sync_api import Page


class ProductDetailsPage:

    def __init__(self, page: Page):
        self.page = page

        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.product_price = page.locator('[data-test="inventory-item-price"]')
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.back_to_inventory_button = page.locator('[data-test="back-to-products"]')
