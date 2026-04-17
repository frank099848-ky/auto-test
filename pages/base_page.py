# pages/base_page.py
from playwright.sync_api import Page, expect
# 1. 修正logger导入路径：从common目录导入
from common.logger import logger

class BasePage:
    """页面基类：封装所有页面通用的操作"""
    # 2. 移除 get_playwright_driver 相关逻辑，完全依赖外部传入的page对象
    def __init__(self, page: Page):
        # 只接收外部传入的page对象（来自conftest的playwright_page夹具）
        self.page = page
        self.logger = logger

    # 通用操作：输入文本
    def input_text(self, locator: str, text: str, desc: str = ""):
        """
        输入文本
        :param locator: 元素定位符（Playwright支持的格式：id/name/xpath/css等）
        :param text: 要输入的文本
        :param desc: 操作描述（用于日志）
        """
        self.logger.info(f"[{desc}] 输入文本：{text} 到元素：{locator}")
        self.page.locator(locator).fill(text)

    # 通用操作：点击元素
    def click_element(self, locator: str, desc: str = ""):
        """点击元素"""
        self.logger.info(f"[{desc}] 点击元素：{locator}")
        self.page.locator(locator).click()

    # 通用操作：等待元素可见
    def wait_for_element_visible(self, locator: str, timeout: int = 10000, desc: str = ""):
        """等待元素可见"""
        self.logger.info(f"[{desc}] 等待元素可见：{locator}")
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    # 通用操作：断言元素文本
    def assert_element_text(self, locator: str, expected_text: str, desc: str = ""):
        """断言元素文本"""
        self.logger.info(f"[{desc}] 断言元素{locator}的文本为：{expected_text}")
        expect(self.page.locator(locator)).to_have_text(expected_text)

    # 通用操作：跳转页面
    def goto(self, url: str, desc: str = ""):
        """跳转指定URL"""
        self.logger.info(f"[{desc}] 跳转URL：{url}")
        self.page.goto(url)