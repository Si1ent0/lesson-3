import pytest


@pytest.fixture()
def browser():
    print("браузер.")
    yield
    print("закрытие браузера")


@pytest.fixture()
def login_page(browser):
    print("login page!")
    pass


@pytest.fixture()
def user():
    print("files")
    return "username", "password"


def test_login(login_page, user):
    username, password =user
    assert username == "username"
    assert password == "password"
    pass