import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

# 测试数据
test_data = {
    "success": ("19939906086", "meiyoumima"),
    "fail": ("19939906086", "111111111")
}


@pytest.mark.ui
def test_login_success(playwright_page):
    """登录成功"""
    login = LoginPage(playwright_page)
    home = HomePage(playwright_page)

    login.open_login_page()
    login.login(*test_data["success"])
    home.assert_login_success(test_data["success"][0])


@pytest.mark.ui
def test_login_fail(playwright_page):
    """登录失败"""
    login = LoginPage(playwright_page)

    login.open_login_page()
    login.login(*test_data["fail"])

    # assert any(k in login.get_error_tip() for k in ["账号", "密码", "错误"])
    assert "账号或密码错误" in login.get_error_tip()