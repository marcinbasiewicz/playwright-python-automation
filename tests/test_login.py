import pytest
from playwright.sync_api import Page, expect


def test_user_can_login_with_valid_credentials(
    page: Page,
    login_page,
    inventory_page
):
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    
    expect(inventory_page.title).to_have_text("Products")


def test_user_cannot_login_with_invalid_password(
    page: Page,
    login_page
):
    login_page.login(
        "standard_user",
        "wrong_password"
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/"
    )

    expect(
        login_page.error_message
    ).to_contain_text(
        "Username and password do not match"
    )


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_login_validation(
    page: Page,
    login_page,
    username,
    password,
    expected_error,
):
    login_page.login(
        username,
        password
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/"
    )

    expect(
        login_page.error_message
    ).to_contain_text(
        expected_error
    )