from core.api_client import api

def test_api_demo_01():
    data = {
        "username": "17638063821",
        "password": "Meiyoumima.",
        "type": 0
    }

    res = api.request(
        method="post",
        url="/ajax/Newlogin?r=0.5819574925456303",
        json=data
    )

    # 打印看看返回什么
    print("返回结果：", res.text)

    # ✅ 断言：直接判断文字（不用json）
    assert "用户名或密码错误" in res.text

def test_api_demo_02():
    data = {
        "username": "19939906086",
        "password": "meiyoumima",
        "type": 0
    }

    res = api.request(
        method="post",
        url="/ajax/Newlogin?r=0.5819574925456303",
        json=data
    )

    # 打印看看返回什么
    print("返回结果：", res.text)

    # ✅ 断言：直接判断文字（不用json）
    assert "恭喜登录成功" in res.text