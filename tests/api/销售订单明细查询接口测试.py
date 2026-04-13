"""
销售订单明细查询接口测试
基于 curl 命令自动生成
"""
from fasttest import TestCase, requests, logger


class TestCase(TestCase):
    """
    销售订单明细查询接口测试
    
    对应 curl:
    curl 'https://kdsa1-api-uat.wilmar.cn/api/analysis/saleordertable/detail/search?pageSize=10&pageNum=1' \
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
        token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyYTMwZmFjMmFjNzhjNTUiLCJ0eXAiOiJhdCtqd3QifQ.eyJuYmYiOjE3NzU3OTA1MTksImV4cCI6MTc3NTg3NjkxOSwiaXNzIjoiaHR0cHM6Ly9rZHNhMS1pbnRlcm5hbC11YXQud2lsbWFyLmNuIiwiYXVkIjoiS2RzQTEiLCJjbGllbnRfaWQiOiJrZHMtYTEtY2xpZW50Iiwic3ViIjoiMjAwMDkyODUyIiwiYXV0aF90aW1lIjoxNzc1NzkwNTE4LCJpZHAiOiJsb2NhbCIsImNvbXBhbnlpZCI6IjM0NzI0IiwiY29tcGFueXNpZCI6IjM0NzI0Iiwic3NvbmFtZSI6ImFkbWluIiwiYWNjb3VudCI6IjM0NzI0LmFkbWluIiwiaXNhZG1pbiI6IlRydWUiLCJiZWxvbmdfdHlwZSI6IjIiLCJlbXBsb3llZV9pZCI6IjAiLCJkb21haW5fbmFtZSI6IiIsInRlbmFudGlkIjoiMDNhNjUyMTEtM2Q3Mi00MzM5LTlhZGMtODQ1MTUxZjhhZGEwIiwiY3VzdG9tZXJfaWQiOiIwIiwiY3VzdG9tZXJfZ3JvdXBfaWQiOiIwIiwiaXNzYWxlcyI6IkZhbHNlIiwiaXNsb2dpc3RpY3MiOiJGYWxzZSIsInJvbGV0eXBlIjoiMCIsInVzYWJsZV9zeXN0ZW0iOiIzIiwic291cmNlX2lkIjoiLTEiLCJnb21zX2lkIjoiMCIsImdvbXNfdXNlcm5hbWUiOiIiLCJpYXQiOjE3NzU3OTA1MTksInNjb3BlIjpbIktkc0ExIiwib2ZmbGluZV9hY2Nlc3MiXSwiYW1yIjpbInB3ZCJdfQ.hntGKW0Rr4_XdcwMyfB7sDq6HJklKhJp7Z5dwoAPFPdennyUSduCNCYq6hn31TAy2Uga1tovGSlQ3wEocTToldEgj3p_drP5pGKufpvetJxlNCXOcqURKvVjU9W1d2dAymXfeheRjh-Sw9uSoZPL800GlwprBOr1r_vOUutfRpTa3iaTUHf9pX5HIBjvp8Dhc3W7hwo1Rl8vpE2MeLNpvHqJT8Z1GMOq7v0q3VBGb3NAf-W_phssgaE9rNMJCLByGKR3j6CjBJ8QSP-Trb4sZKATnVq4AN97qG6q6cQc9nDm-PpbzwPWtUo7ET-x8FcGnxfvxAxAUwnq4G65nqq0mw"
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
    
    def test_sale_order_detail_search_p0(self):
        """
        DMS-SALES041301---TC-P0: 销售订单明细查询 - 正常场景（固定日期）
        """
        # 请求体（从 curl 的 --data-raw 获取）
        payload = {
            "BeginBillDate": "2026-04-03",
            "EndBillDate": "2026-04-10",
            "DistributorContractIds": [],
            "DistributorIds": [],
            "BranchIds": [],
            "BillTypeSubIds": [],
            "BillStatuss": ["3", "4", "5", "6"],
            "ItemTypes": [],
            "CustChannelTypeIds": [],
            "CustTypeIds": [],
            "CustDefinedTypeIds": [],
            "CustIds": [],
            "WareHouseIds": [],
            "CustSystemIds": [],
            "EmpIds": [],
            "BussLineIds": [],
            "ProdLineIds": [],
            "ProdIds": [],
            "SourceSysTypes": [],
            "BillTypeIds": [5]
        }
        
        # 发送请求（从 curl 的 URL 获取路径和参数）
        response = requests.post(
            "/api/analysis/saleordertable/detail/search",
            params={"pageSize": 10, "pageNum": 1},
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
            logger.log_info(f"第一条数据: BillNo={first_item.get('BillNo')}, CustName={first_item.get('CustName')}")
            # 验证关键字段存在
            assert "BillNo" in first_item, "缺少 BillNo 字段"
            assert "CustName" in first_item, "缺少 CustName 字段"
        
        logger.log_info("✅ 销售订单明细查询 P0 测试通过")
    
    def test_sale_order_detail_search_different_page(self):
        """
        DMS-SALES041303---TC-P0: 销售订单明细查询 - 分页查询
        """
        payload = {
            "BeginBillDate": "2026-04-03",
            "EndBillDate": "2026-04-10",
            "DistributorContractIds": [],
            "DistributorIds": [],
            "BranchIds": [],
            "BillTypeSubIds": [],
            "BillStatuss": ["3", "4", "5", "6"],
            "ItemTypes": [],
            "CustChannelTypeIds": [],
            "CustTypeIds": [],
            "CustDefinedTypeIds": [],
            "CustIds": [],
            "WareHouseIds": [],
            "CustSystemIds": [],
            "EmpIds": [],
            "BussLineIds": [],
            "ProdLineIds": [],
            "ProdIds": [],
            "SourceSysTypes": [],
            "BillTypeIds": [5]
        }
        
        # 查询第二页
        response = requests.post(
            "/api/analysis/saleordertable/detail/search",
            params={"pageSize": 10, "pageNum": 2},
            json=payload
        )
        
        response.assert_ok().assert_field("Items", "TotalCount")
        
        data = response.json()
        logger.log_info(f"第二页查询，总记录数: {data.TotalCount}")
        logger.log_info("✅ 分页查询测试通过")
    
    def test_sale_order_detail_search_invalid_token(self):
        """
        DMS-SALES041303---TC-P1: 销售订单明细查询 - 无效 Token 场景
        """
        # 临时清除 Token
        requests.clear_token()
        
        payload = {
            "BeginBillDate": "2026-04-03",
            "EndBillDate": "2026-04-10",
            "BillStatuss": ["3", "4", "5", "6"],
            "BillTypeIds": [5]
        }
        
        response = requests.post(
            "/api/analysis/saleordertable/detail/search",
            params={"pageSize": 10, "pageNum": 1},
            json=payload
        )
        
        # 验证返回 401 未授权
        response.assert_status_in(401, 403)
        logger.log_info(f"✅ 无效 Token 场景测试通过，返回状态码: {response.status_code}")
        
        # 恢复 Token
        self.setUpClass()
    
    def test_sale_order_detail_search_empty_date(self):
        """
        DMS-SALES041304---TC-P1: 销售订单明细查询 - 空日期范围（边界场景）
        """
        payload = {
            "BeginBillDate": "2026-04-10",
            "EndBillDate": "2026-04-03",  # 结束日期早于开始日期
            "DistributorContractIds": [],
            "DistributorIds": [],
            "BranchIds": [],
            "BillTypeSubIds": [],
            "BillStatuss": ["3", "4", "5", "6"],
            "ItemTypes": [],
            "CustChannelTypeIds": [],
            "CustTypeIds": [],
            "CustDefinedTypeIds": [],
            "CustIds": [],
            "WareHouseIds": [],
            "CustSystemIds": [],
            "EmpIds": [],
            "BussLineIds": [],
            "ProdLineIds": [],
            "ProdIds": [],
            "SourceSysTypes": [],
            "BillTypeIds": [5]
        }
        
        response = requests.post(
            "/api/analysis/saleordertable/detail/search",
            params={"pageSize": 10, "pageNum": 1},
            json=payload
        )
        
        # 验证接口正常返回（可能返回空数据或错误提示）
        response.assert_ok()
        data = response.json()
        
        logger.log_info(f"异常日期查询，返回数据条数: {len(data.Items)}")
        logger.log_info("✅ 空日期范围边界测试通过")
