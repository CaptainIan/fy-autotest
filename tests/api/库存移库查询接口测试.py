"""
库存移库查询接口测试
基于 curl 命令自动生成

对应 curl:
curl 'https://kdsa1-api-uat.wilmar.cn/api/inventory/movestock/_search?pagesize=10&pagenum=1' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer xxx' \
  -H 'content-type: application/json; charset=UTF-8' \
  -H 'dms-platform: web-kds' \
  --data-raw '{...}'
"""
from fasttest import TestCase, requests, logger


class TestCase(TestCase):
    """
    库存移库查询接口测试
    
    对应 curl:
    curl 'https://kdsa1-api-uat.wilmar.cn/api/inventory/movestock/_search?pagesize=10&pagenum=1' \
      -H 'accept: application/json, text/plain, */*' \
      -H 'authorization: Bearer xxx' \
      -H 'content-type: application/json; charset=UTF-8' \
      -H 'dms-platform: web-kds' \
      --data-raw '{...}'
    """
    _api_test_only = True
    
    @classmethod
    def setUpClass(cls):
        """类级别初始化 - 设置认证信息"""
        # 设置 Bearer Token
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyYTMwZmFjMmFjNzhjNTUiLCJ0eXAiOiJhdCtqd3QifQ.eyJuYmYiOjE3NzYwNjY0MDUsImV4cCI6MTc3NjE1MjgwNSwiaXNzIjoiaHR0cHM6Ly9rZHNhMS1pbnRlcm5hbC11YXQud2lsbWFyLmNuIiwiYXVkIjoiS2RzQTEiLCJjbGllbnRfaWQiOiJrZHMtYTEtY2xpZW50Iiwic3ViIjoiMjAwMDkyODUyIiwiYXV0aF90aW1lIjoxNzc2MDY2NDA1LCJpZHAiOiJsb2NhbCIsImNvbXBhbnlpZCI6IjM0NzI0IiwiY29tcGFueXNpZCI6IjM0NzI0Iiwic3NvbmFtZSI6ImFkbWluIiwiYWNjb3VudCI6IjM0NzI0LmFkbWluIiwiaXNhZG1pbiI6IlRydWUiLCJiZWxvbmdfdHlwZSI6IjIiLCJlbXBsb3llZV9pZCI6IjAiLCJkb21haW5fbmFtZSI6IiIsInRlbmFudGlkIjoiMDNhNjUyMTEtM2Q3Mi00MzM5LTlhZGMtODQ1MTUxZjhhZGEwIiwiY3VzdG9tZXJfaWQiOiIwIiwiY3VzdG9tZXJfZ3JvdXBfaWQiOiIwIiwiaXNzYWxlcyI6IkZhbHNlIiwiaXNsb2dpc3RpY3MiOiJGYWxzZSIsInJvbGV0eXBlIjoiMCIsInVzYWJsZV9zeXN0ZW0iOiIzIiwic291cmNlX2lkIjoiLTEiLCJnb21zX2lkIjoiMCIsImdvbXNfdXNlcm5hbWUiOiIiLCJpYXQiOjE3NzYwNjY0MDUsInNjb3BlIjpbIktkc0ExIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.UaB4xTqcrK9cd1d2HWtwhUm1CrJOViuRCk6Fc2GyC6OetTtDj6_AknfAvImu0WTGF8nkKsZ8RfSt_MZ_4ekHdFxKmCC0uLD0o-F1FLuY6jyctHa0c7MG6pAezGob5bXJTXeWDNZLIWMPZeVlFzSEQ2bjuve16SlpbLjvCCJUg7Brnx9gHCEi8a-a7LPObzpexkOsFC-ics-pV7A4GVP7icb-esAc1smi_Bflk6fmrG9eSa2cqCAWqqAmAuWciWUhbD93gdlIMjHXs31wWA_rbAon6km3MotBxQSENEvL5gdAQhJ4odkDeu145dawVcnN_5W4Km8B1KB_ZsDRfugdRQ"
        requests.set_bearer_token(token)
        
        # 设置业务请求头
        requests.set_headers({
            "accept": "application/json, text/plain, */*",
            "accept-language": "c=zh-CN|uic=zh-CN",
            "dms-platform": "web-kds",
            "origin": "https://kdsa1-uat.wilmar.cn",
            "referer": "https://kdsa1-uat.wilmar.cn/",
            "x-requested-with": "XMLHttpRequest"
        })
    
    def test_movestock_search_p0(self):
        """
        TC-P0: 库存移库查询 - 正常场景（固定日期范围）
        """
        # 请求体（从 curl 的 --data-raw 获取）
        payload = {
            "BeginDoBillDate": "2026-01-13",
            "EndDoBillDate": "2026-04-13",
            "BillStatus": ["2", "3", "7", "14", "15", "16", "17"],
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        # 发送请求（从 curl 的 URL 获取路径和参数）
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 10, "pagenum": 1},
            json=payload
        )
        
        # 链式断言：状态码 200 + 字段存在
        response.assert_ok().assert_field("Items", "TotalCount")
        
        # 获取响应数据
        data = response.json()
        items = data.Items
        total_count = data.TotalCount
        
        logger.log_info(f"总记录数: {total_count}")
        logger.log_info(f"返回数据条数: {len(items)}")
        
        # 如果有数据，验证第一条数据结构
        if items:
            first_item = items[0]
            logger.log_info(f"第一条数据: BillNo={first_item.get('BillNo')}, SrcWareHouseName={first_item.get('SrcWareHouseName')}")
            # 验证关键字段存在
            assert "BillNo" in first_item, "缺少 BillNo 字段"
            assert "SrcWareHouseName" in first_item, "缺少 SrcWareHouseName 字段"
            assert "DestWareHouseName" in first_item, "缺少 DestWareHouseName 字段"
        
        logger.log_info("✅ 库存移库查询 P0 测试通过")
    
    def test_movestock_search_different_page(self):
        """
        TC-P0: 库存移库查询 - 分页查询
        """
        payload = {
            "BeginDoBillDate": "2026-01-13",
            "EndDoBillDate": "2026-04-13",
            "BillStatus": ["2", "3", "7", "14", "15", "16", "17"],
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        # 查询第二页
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 10, "pagenum": 2},
            json=payload
        )
        
        response.assert_ok().assert_field("Items", "TotalCount")
        
        data = response.json()
        logger.log_info(f"第二页查询，总记录数: {data.TotalCount}")
        logger.log_info("✅ 分页查询测试通过")
    
    def test_movestock_search_by_status(self):
        """
        TC-P0: 库存移库查询 - 按单据状态筛选
        """
        # 只查询状态为 "2"（已审核）的单据
        payload = {
            "BeginDoBillDate": "2026-01-13",
            "EndDoBillDate": "2026-04-13",
            "BillStatus": ["2"],  # 只查已审核
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 10, "pagenum": 1},
            json=payload
        )
        
        response.assert_ok().assert_field("Items", "TotalCount")
        
        data = response.json()
        items = data.Items
        
        # 验证返回的数据状态都是已审核
        if items:
            for item in items:
                assert item.get('BillStatus') == '2', f"单据状态应为已审核(2)，实际为: {item.get('BillStatus')}"
        
        logger.log_info(f"按状态筛选查询，返回数据条数: {len(items)}")
        logger.log_info("✅ 按单据状态筛选测试通过")
    
    def test_movestock_search_invalid_token(self):
        """
        TC-P1: 库存移库查询 - 无效 Token 场景
        """
        # 临时清除 Token
        requests.clear_token()
        
        payload = {
            "BeginDoBillDate": "2026-01-13",
            "EndDoBillDate": "2026-04-13",
            "BillStatus": ["2", "3", "7", "14", "15", "16", "17"],
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 10, "pagenum": 1},
            json=payload
        )
        
        # 验证返回 401 未授权
        response.assert_status_in(401, 403)
        logger.log_info(f"✅ 无效 Token 场景测试通过，返回状态码: {response.status_code}")
        
        # 恢复 Token
        self.setUpClass()
    
    def test_movestock_search_empty_date(self):
        """
        TC-P1: 库存移库查询 - 空日期范围（边界场景）
        """
        payload = {
            "BeginDoBillDate": "2026-04-13",
            "EndDoBillDate": "2026-01-13",  # 结束日期早于开始日期
            "BillStatus": ["2", "3", "7", "14", "15", "16", "17"],
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 10, "pagenum": 1},
            json=payload
        )
        
        # 验证接口正常返回（可能返回空数据或错误提示）
        response.assert_ok()
        data = response.json()
        
        logger.log_info(f"异常日期查询，返回数据条数: {len(data.Items)}")
        logger.log_info("✅ 空日期范围边界测试通过")
    
    def test_movestock_search_large_pagesize(self):
        """
        TC-P1: 库存移库查询 - 大分页边界场景
        """
        payload = {
            "BeginDoBillDate": "2026-01-13",
            "EndDoBillDate": "2026-04-13",
            "BillStatus": ["2", "3", "7", "14", "15", "16", "17"],
            "SrcWareHouseIds": [],
            "DestWareHouseIds": [],
            "CreateUserIds": [],
            "ProdIds": []
        }
        
        # 查询大分页（100条）
        response = requests.post(
            "/api/inventory/movestock/_search",
            params={"pagesize": 100, "pagenum": 1},
            json=payload
        )
        
        response.assert_ok().assert_field("Items", "TotalCount")
        
        data = response.json()
        logger.log_info(f"大分页查询，返回数据条数: {len(data.Items)}")
        logger.log_info("✅ 大分页边界测试通过")
