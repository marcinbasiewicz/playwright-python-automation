from playwright.sync_api import Page, expect


def test_user_can_add_product_to_cart(
    page: Page,
    login_page,
    inventory_page
):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(inventory_page.shopping_cart_badge).to_have_text("1")


def test_user_can_add_two_products_to_cart(
    page: Page,
    login_page,
    inventory_page
):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.add_to_cart_bike_light()


    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(inventory_page.shopping_cart_badge).to_have_text("2")

def test_user_can_add_and_remove_product_from_cart(
    page: Page,
    login_page,
    inventory_page
):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()
    
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

    inventory_page.remove_from_cart_backpack()
    
    expect(inventory_page.shopping_cart_badge).to_be_hidden()


def test_user_can_add_backpack_to_cart_and_see_item_and_price_in_cart(
    page: Page,
    login_page,
    inventory_page,
    cart_page
):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()

    inventory_page.go_to_cart()
    expect(page).to_have_url(
            "https://www.saucedemo.com/cart.html"
        )
    expect(cart_page.inventory_item_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.inventory_item_price).to_have_text("$29.99")


def test_user_can_remove_backpack_from_cart(
    page: Page,
    login_page,
    inventory_page,
    cart_page
):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()

    inventory_page.go_to_cart()
    
    cart_page.remove_backpack()

    expect(cart_page.shopping_cart_badge).to_be_hidden()
    expect(cart_page.inventory_item_name).to_be_hidden()


def test_user_can_add_two_products_and_see_details(
    page: Page,
    login_page,
    inventory_page,
    cart_page
    ):
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.add_to_cart_bike_light()
    inventory_page.go_to_cart()

    products_names = cart_page.inventory_item_name.all_text_contents()
    assert "Sauce Labs Backpack" in products_names
    assert "Sauce Labs Bike Light" in  products_names
   

    backpack = cart_page.get_product("Sauce Labs Backpack")
    backpack_price = cart_page.get_product_price(backpack)
    expect(backpack_price).to_have_text("$29.99")

    bike_light = cart_page.get_product("Sauce Labs Bike Light")
    bike_light_price = cart_page.get_product_price(bike_light)
    expect(bike_light_price).to_have_text("$9.99")
    