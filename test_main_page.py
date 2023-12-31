from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)                   # инициализируем Page Object, передаем в конструктор драйвер и url адрес
        page.open()                                      # открываем страницу
        page.go_to_login_page()                          # выполняем метод страницы — переходим на страницу логина
        page2 = LoginPage(browser, browser.current_url)  # переходим на странницу Login
        page2.should_be_login_page()                     # проверяем корректность страницы login

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


