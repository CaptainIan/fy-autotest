import requests
import json


def get_login_token():
    """
    调用登录接口，返回AccessToken和RefreshToken（不存入全局变量）
    返回值：
        成功：(AccessToken, RefreshToken) 元组
        失败：(None, None)
    """
    # 1. 接口基础配置
    login_url = "https://dms-plus-api-uat.wilmar.cn/api/sso/identity/account/login"

    # 2. 请求头（完全匹配curl中的header）
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "c=zh-CN|uic=zh-CN",
        "access-control-allow-origin": "*",
        "captchakey": "3a1fe432-ee3b-2318-acee-b8b108894be5",
        "content-type": "application/json-patch+json; charset=UTF-8",
        "origin": "https://dms-plus-uat.wilmar.cn",
        "priority": "u=1, i",
        "referer": "https://dms-plus-uat.wilmar.cn/",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    # 3. 请求体（完全匹配curl中的data-raw）
    payload = {
        "Username": "10001",
        "Password": "SHGNpLI1YKnNtz0mPKeYaA==",
        "SourceSysType": 8388608,
        "CaptchaCode": "yj6n",
        "Key": "Je9RUA0gtCDm8yA2h/JXghDzZw4uk8ot6u3GaQOiTAuG5e7ZfAjEd3xPYt/iDu5f20W1qlkuGTBP991QauLM/eNTPY8yGFuuFH9PW+h8kTW1mqUPd3N4h2GfhKCixLsDgLKP7MY6VVqS/NX/k0gbc7UWUos0LoQNKfjLlwAC9v4="
    }

    try:
        # 4. 发送POST请求（关闭SSL验证，适配测试环境）
        response = requests.post(
            login_url,
            headers=headers,
            json=payload,
            verify=False
        )

        # 5. 检查请求是否成功
        response.raise_for_status()

        # 6. 解析返回数据
        result = response.json()
        # print("✅ 登录接口返回数据：")
        # print(json.dumps(result, indent=2, ensure_ascii=False))

        # 7. 提取核心字段并返回
        access_token = result.get("AccessToken", "")

        if not access_token:
            # print("❌ 接口返回数据中缺少AccessToken或RefreshToken！")
            return None

        # print("\n✅ 成功获取Token：")
        # print(f"AccessToken: {access_token[:20]}...（部分隐藏）")
        # print(f"RefreshToken: {refresh_token}")

        return access_token

    except requests.exceptions.RequestException as e:
        # 请求异常（网络错误、非200状态码等）
        print(f"❌ 登录接口请求失败：{str(e)}")
        if hasattr(response, "text"):
            print(f"❌ 接口返回内容：{response.text}")
        return None, None

    except json.JSONDecodeError as e:
        # JSON解析失败
        print(f"❌ 返回数据解析失败：{str(e)}")
        return None, None

    except Exception as e:
        # 其他未知异常
        print(f"❌ 未知错误：{str(e)}")
        return None, None


# 调用示例
if __name__ == "__main__":
    # 调用接口获取Token
    access_token, refresh_token = get_login_token()

