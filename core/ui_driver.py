from playwright.sync_api import sync_playwright
from common.logger import logger
from config.settings import UI_URL

class UiDriver:
    def __init__(self):
        self.pw = sync_playwright().start()
        # 这里改成 chromium 就对了！
        self.browser = self.pw.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        logger.info("✅ Playwright 启动成功")

    def open(self, path=""):
        self.page.goto(UI_URL + path)

    def quit(self):
        self.browser.close()
        self.pw.stop()
        logger.info("✅ 浏览器已关闭")

# 全局对象
ui = UiDriver()