from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.inventory_item_name = page.locator('[data-test="inventory-item-name"]')
        self.inventory_item_price = page.locator('[data-test="inventory-item-price"]')
        self.remove_backpack_from_cart = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')

    def remove_backpack(self):
        self.remove_backpack_from_cart.click()

    def get_product(self, product_name):
        return self.cart_items.filter(has_text=product_name)

    def get_product_price(self, product):
        return product.locator('[data-test="inventory-item-price"]')
    
        