import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True


# pytest будет искать и выполнять только те тесты, которые помечены меткой smoke и не помечены меткой beta_users!
# если где-то нет smoke можно вычеркнуть из списка,
# если где-то есть skip то это можно вычеркнуть даже если рядом smoke,
# skip он и для всех в классе skip и для каждой функции skip  - это можно вычеркнуть,
# если встретился beta_users это можно вычеркнуть даже если рядом smoke,
# остальные без smoke тоже можно вычеркнуть.
