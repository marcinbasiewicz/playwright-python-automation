import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)