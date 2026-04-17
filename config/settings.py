# config/settings.py（只修改ENV相关行，其他不变）
import os
import configparser

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE_PATH = os.path.join(BASE_DIR, "config/config.ini")

# 初始化配置解析器
conf = configparser.ConfigParser()
try:
    conf.read(CONFIG_FILE_PATH, encoding="utf-8")
except FileNotFoundError:
    raise FileNotFoundError(f"配置文件不存在！请检查路径：{CONFIG_FILE_PATH}")
except Exception as e:
    raise Exception(f"读取配置文件失败：{str(e)}")

# ========== 修复ENV读取逻辑（核心修改） ==========
# 读取active_env并清理多余字符（空格、注释）
raw_env = conf.get("ENV", "active_env", fallback="test")
# 只保留第一个空格前的内容（去掉注释），并去除首尾空格
ENV = raw_env.strip().split()[0]  # 比如把"test  # 注释"变成"test"

# 读取配置（现在能正确找到[test]节）
API_HOST = conf.get(ENV, "api_host", fallback="")
UI_URL = conf.get(ENV, "ui_url", fallback="")

# 其他路径/方法不变...
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_DIR = os.path.join(BASE_DIR, "logs")

def get_ui_page_url(page_path: str) -> str:
    if not UI_URL:
        raise ValueError(f"当前环境[{ENV}]的ui_url配置为空！请检查config.ini")
    return f"{UI_URL.rstrip('/')}/{page_path.lstrip('/')}"

def get_config(section: str, option: str, fallback: str = "") -> str:
    return conf.get(section, option, fallback=fallback)