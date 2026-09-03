from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.title = page.locator('[data-test="title"]')
        self.add_to_cart_sauce_labs_backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_to_cart_sauce_labs_bike_light = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.remove_from_cart_sauce_labs_backpack = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.shopping_cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.shopping_cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        
    def add_to_cart_backpack(self): 
        self.add_to_cart_sauce_labs_backpack.click() 

    def add_to_cart_bike_light(self): 
        self.add_to_cart_sauce_labs_bike_light.click()   

    def remove_from_cart_backpack(self):
        self.remove_from_cart_sauce_labs_backpack.click()

    def go_to_cart(self):
        self.shopping_cart_link.click()

        
        
