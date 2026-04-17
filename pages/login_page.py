from pages.base_page import BasePage
from config.settings import get_ui_page_url

class LoginPage(BasePage):
    """登录页"""
    INPUT_USERNAME = "#account"
    INPUT_PASSWORD = "#password"
    BTN_SUBMIT = ".log-btn"
    TIP_ERROR = ".x-pass"

    def open_login_page(self):
        self.goto(get_ui_page_url(""), desc="打开登录页")

    def login(self, username, password):
        self.wait_for_element_visible(self.INPUT_USERNAME)
        self.input_text(self.INPUT_USERNAME, username)

        self.wait_for_element_visible(self.INPUT_PASSWORD)
        self.input_text(self.INPUT_PASSWORD, password)

        self.wait_for_element_visible(self.BTN_SUBMIT)
        self.click_element(self.BTN_SUBMIT)

    def get_error_tip(self):
        self.wait_for_element_visible(self.TIP_ERROR, timeout=3000)
        return self.page.locator(self.TIP_ERROR).text_content().strip()