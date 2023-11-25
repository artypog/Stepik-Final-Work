from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


link_global = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_global, 4)
    page.open()
    page.should_not_be_success_message()
    page.should_be_add_to_basket_button()
    page.add_to_basket()

    page.should_be_product_name()
    page.should_be_product_name_after_adding()
    page.should_be_equal_names()
    page.should_be_equal_prices()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        reg_link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, reg_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "qwertyuiop1234567890"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_global, 4)
        page.open()
        page.should_not_be_success_message()
        page.should_be_add_to_basket_button()
        page.add_to_basket()

        page.should_be_product_name()
        page.should_be_product_name_after_adding()
        page.should_be_equal_names()
        page.should_be_equal_prices()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_global, 4)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail(reason="There should be success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_global, 0)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_global, 0)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_disappear_message()


@pytest.mark.login_test
def test_guest_should_see_login_link_on_product_page(browser):
    local_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, local_link, 0)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    local_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, local_link, 4)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_global, 4)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


