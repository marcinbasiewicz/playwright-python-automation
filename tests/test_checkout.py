import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        ("", "", "", "First Name is required"),
        ("Jan", "", "", "Last Name is required"),
        ("Jan", "Kowalski", "", "Postal Code is required"),
    ],
    ids=["missing-first_name", "missing-last_name", "missing-postal_code"],
)
def test_user_cannot_go_to_overview_without_valid_info(
    page: Page,
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    first_name,
    last_name,
    postal_code,
    expected_error,
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    checkout_page.continue_checkout()
    expect(checkout_page.error_message).to_contain_text(expected_error)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")


def test_user_can_go_to_checkout_overview_with_valid_info(
    page: Page,
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    checkout_overview_page,
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info("Jan", "Kowalski", "90-001")
    checkout_page.continue_checkout()
    expect(checkout_overview_page.checkout_title).to_have_text("Checkout: Overview")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")


def test_user_can_complete_checkout(
    page: Page,
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    checkout_overview_page,
    checkout_complete_page,
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info("Jan", "Kowalski", "90-001")
    checkout_page.continue_checkout()
    checkout_overview_page.finish_checkout()
    expect(checkout_complete_page.checkout_title).to_have_text("Checkout: Complete")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")


def test_item_total_equals_sum_of_item_prices(
    page: Page,
    login_page,
    inventory_page,
    cart_page,
    checkout_page,
    checkout_overview_page,
):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_to_cart_backpack()
    inventory_page.add_to_cart_bike_light()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info("Jan", "Kowalski", "90-001")
    checkout_page.continue_checkout()
    sum_of_item_prices = checkout_overview_page.get_sum_of_item_prices()
    item_total = checkout_overview_page.get_item_total()

    assert sum_of_item_prices == item_total
