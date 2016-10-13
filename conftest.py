import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        url = request.config.getoption("--url")
        fixture = Application(browser=browser, url=url)

    else:
        if not fixture.is_valid():
            fixture = Application()
    username = request.config.getoption("--login")
    password = request.config.getoption("--pass")
    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--login", action="store", default="admin")
    parser.addoption("--pass", action="store", default="")
    parser.addoption("--url", action="store", default="http://localhost/addressbook/")