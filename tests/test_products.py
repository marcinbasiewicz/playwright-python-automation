from playwright.sync_api import Page, expect


def test_user_can_sort_items_by_price_asc(page: Page, login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_by_price_asc()
    prices = inventory_page.get_and_convert_prices()
    sorted_prices = sorted(prices)
    assert sorted_prices == prices


def test_user_can_go_to_backpack_details(
    page: Page, login_page, inventory_page, product_details_page
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.open_backpack_details()
    expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")
    expect(product_details_page.back_to_inventory_button).to_be_visible()
    expect(product_details_page.product_name).to_have_text("Sauce Labs Backpack")
    expect(product_details_page.product_price).to_have_text("$29.99")
    expect(product_details_page.add_to_cart_button).to_be_visible()
