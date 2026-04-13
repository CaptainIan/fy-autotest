"""
示例接口测试 - 基于 curl 转换
请将您的 curl 命令提供给我，我会帮您生成对应的测试用例

示例 curl:
curl -X POST "https://api.example.com/endpoint" \
  -H "Authorization: Bearer token" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
"""
from fasttest import TestCase, requests, logger


class TestCase(TestCase):
    """
    示例接口测试
    
    用例标记：_api_test_only = True 表示纯接口测试，不会启动浏览器
    """
    _api_test_only = True
    
    @classmethod
    def setUpClass(cls):
        """类级别初始化 - 设置认证信息"""
        # 设置 Bearer Token（从 curl 的 -H "Authorization: Bearer xxx" 获取）
        token = "your-token-here"
        requests.set_bearer_token(token)
        
        # 设置其他请求头（从 curl 的 -H 参数获取）
        requests.set_headers({
            "custom-header": "value"
        })
    
    def test_example_api_p0(self):
        """
        TC-P0: 示例接口测试 - 正常场景
        
        对应 curl:
        curl -X POST "https://api.example.com/endpoint" \
          -H "Authorization: Bearer token" \
          -H "Content-Type: application/json" \
          -d '{"key": "value"}'
        """
        # 请求体（从 curl 的 -d 参数获取）
        payload = {
            "key": "value"
        }
        
        # 发送请求
        response = requests.post(
            "/endpoint",  # 从 curl 的 URL 获取路径部分
            json=payload
        )
        
        # 链式断言：状态码 200 + 字段存在
        response.assert_ok().assert_field("code", "data", "message")
        
        # 获取响应数据
        data = response.json()
        
        # 业务断言
        logger.log_info(f"响应码: {data.code}")
        logger.log_info(f"响应消息: {data.message}")
        
        logger.log_info("✅ 示例接口测试通过")
    
    def test_example_api_invalid_token(self):
        """
        TC-P1: 示例接口测试 - 无效 Token 场景
        """
        # 临时清除 Token
        requests.clear_token()
        
        payload = {
            "key": "value"
        }
        
        response = requests.post(
            "/endpoint",
            json=payload
        )
        
        # 验证返回 401 未授权
        response.assert_status_in(401, 403)
        logger.log_info(f"✅ 无效 Token 场景测试通过，返回状态码: {response.status_code}")
        
        # 恢复 Token
        self.setUpClass()


# ==================== 请提供您的 curl，我会生成对应的测试用例 ====================
# 
# 格式示例：
# curl -X POST "https://kdsa1-api-uat.wilmar.cn/api/saleorder/create" \
#   -H "Authorization: Bearer eyJhbG..." \
#   -H "Content-Type: application/json" \
#   -d '{
#     "CustId": "12345",
#     "Products": [{"Id": "1", "Qty": 10}]
#   }'
#
# 我会帮您转换为：
# 1. 设置 Token 和 Headers
# 2. 构建请求体
# 3. 链式断言
# 4. 业务验证
