from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    """首页"""
    USER_INFO = ".jk_mr27"

    def assert_login_success(self, phone):
        expect(self.page.locator(self.USER_INFO)).to_contain_text(f"{phone[:3]}*****{phone[-3:]}")