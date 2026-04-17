import pytest
import os
import subprocess
from config.settings import REPORT_DIR  # 导入配置的报告路径

if __name__ == "__main__":
    # 1. 定义pytest运行参数（关键：每个参数独立成字符串）
    pytest_args = [
        "test_cases/",  # 要执行的用例目录
        "-v",  # 显示详细日志
        "--tb=short",  # 简化错误信息
        "--alluredir", f"{REPORT_DIR}/allure-results",  # 分开写！不是--alluredir=xxx
        "--clean-alluredir"  # 清空旧的allure结果（可选）
    ]

    # 2. 执行pytest用例
    pytest.main(pytest_args)

    # 3. 生成Allure报告（先判断allure是否安装，避免报错）
    # allure_results = f"{REPORT_DIR}/allure-results"
    # allure_report = f"{REPORT_DIR}/allure-report"

    # try:
    #     # 生成报告命令（--clean清空旧报告）
    #     subprocess.run(
    #         ["allure", "generate", allure_results, "-o", allure_report, "--clean"],
    #         check=True,  # 执行失败时抛出异常
    #         shell=True  # Windows系统需要加shell=True
    #     )
    #     print(f"\n✅ 报告已生成：{allure_report}/index.html")
    # except subprocess.CalledProcessError as e:
    #     print(f"\n❌ 生成Allure报告失败：{e}")
    #     print("⚠️  请先安装Allure并配置环境变量，或跳过报告生成步骤")
    # except FileNotFoundError:
    #     print("\n❌ 未找到allure命令！请先安装Allure并配置环境变量")