from playwright.sync_api import Page, expect


def test_user_cannot_access_inventory_page_after_logout(
    page: Page, login_page, inventory_page
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.open_menu()
    inventory_page.logout()
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(login_page.error_message).to_contain_text(
        "You can only access '/inventory.html' when you are logged in"
    )
