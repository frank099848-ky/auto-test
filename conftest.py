# conftest.py（新增标记注册）
import pytest
from playwright.sync_api import sync_playwright

# ========== 新增：注册自定义标记 ==========
def pytest_configure(config):
    # 注册ui标记，描述为“UI自动化测试用例”
    config.addinivalue_line(
        "markers", "ui: UI自动化测试用例"
    )
    # 可选：注册其他标记（如order、login）
    config.addinivalue_line(
        "markers", "order: 订单相关用例"
    )

# ========== 原有夹具逻辑不变 ==========
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

@pytest.fixture(scope="function")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500,
            args=["--start-maximized"]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def playwright_page(playwright_browser):
    context = playwright_browser.new_context(
        viewport=None,
        ignore_https_errors=True
    )
    page = context.new_page()
    page.on("console", lambda msg: print(f"页面控制台[{msg.type}]：{msg.text}") if msg.type == "error" else None)
    yield page
    page.close()
    context.close()