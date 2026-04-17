import requests
from config.settings import API_HOST
from common.logger import logger

class ApiClient:
    def __init__(self):
        self.base_url = API_HOST
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        url = self.base_url + url
        logger.info(f"请求地址：{url}")
        logger.info(f"请求参数：{kwargs}")
        res = self.session.request(method, url,** kwargs)
        logger.info(f"响应结果：{res.text}")
        return res

api = ApiClient()