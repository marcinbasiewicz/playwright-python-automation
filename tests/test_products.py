from playwright.sync_api import Page

def test_user_can_sort_items_by_price_asc(
    page: Page,
    login_page,
    inventory_page):

    login_page.login("standard_user","secret_sauce")
    inventory_page.sort_by_price_asc()
    prices = inventory_page.get_and_convert_prices()
    sorted_prices = sorted(prices)
    assert sorted_prices == prices    
