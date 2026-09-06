import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        ("", "", "", "First Name is required"),
        ("Jan", "", "", "Last Name is required"),
        ("Jan", "Kowalski", "", "Postal Code is required")
    ]
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
    expected_error
):
    login_page.login(
                "standard_user",
                "secret_sauce"
            )
    inventory_page.add_to_cart_backpack()
    inventory_page.go_to_cart()
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info(
        first_name,
        last_name,
        postal_code
    )
    checkout_page.continue_checkout()
    expect(checkout_page.error_message).to_contain_text(expected_error)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    