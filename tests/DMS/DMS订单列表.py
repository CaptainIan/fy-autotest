
from fasttest import TestCase, driver
from common import login, window

class TestCase(TestCase):

    def test_DMS_ORDER_LIST(self):
        """
        tc-p0: DMS 订单列表检查
        """
        window.web_window()
        login.login_dms_plus()
        driver.check('首页')
        driver.click('采购管理')
        driver.click('采购订单')
        driver.sleep(1)
        driver.check('PO26041010017')
        driver.sleep(1)
        driver.click('class=el-button el-button--default', index=1)
        driver.click('placeholder=请输入', index=1)
        driver.input('PO26041010017')
        driver.click('查询')
        driver.sleep(1)
        driver.check('西安比亚迪标签')
        driver.sleep(1)

