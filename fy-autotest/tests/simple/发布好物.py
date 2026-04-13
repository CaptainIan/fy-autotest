
from fasttest import TestCase, driver, gvar, logger
from common import common, login, window
from datetime import datetime
import random
from urllib.parse import urlparse, parse_qs

class TestCase(TestCase):

    def test_goods_publish(self):
        """
        tc-p0: 我的-个人信息检查、更新
        """
        date_string = datetime.now().strftime("%Y-%m-%d")
        goods_price = str(random.randint(0,100))
        goods_name = '自动化测试好物' + date_string + '-' + goods_price
        window.h5_window()
        login.login_spark()
        # 按系列筛选
        driver.click('橱窗')
        driver.click('添加好物商品')
        driver.check('发布')
        driver.click('去选择')
        driver.click('手机通讯')
        driver.click('确定')
        driver.click('placeholder=描述一下好物的品牌型号、货品来源')
        driver.input(goods_name)
        driver.mouse_click('placeholder=描述一下好物的品牌型号、货品来源', options={'x': 20, 'y': -80})
        common.upload('C2C/氢气球.jpg', '选择图片')
        driver.click('placeholder=请输入10~10000定价金额')
        driver.input(goods_price)
        driver.click('请选择')
        driver.check('自提或无须邮寄')
        driver.click('邮寄')
        driver.click('确认')
        driver.click('发布')
        driver.sleep(2)
        driver.check('关于卖家')
        parsed_url = urlparse(driver.url())
        query_params = parse_qs(parsed_url.query)
        id_value = query_params.get('id', [''])[0]
        logger.log_info('好物商品发布成功，商品id为：' + str(id_value) + ',商品名称为：' + goods_name)
        driver.sleep(5)

        logger.log_info('进入 alpha运营端审核 页面')
        window.web_window({'key': 'ALPHA_WINDOW'})
        login.login_alpha()
        for i in range(36):
            if driver.exist('内部管理系统', options={'timeout': 5}):
                logger.log_info('“内部管理系统”已经存在')
                break
        driver.goto("https://alpha-test-intranet.xunfeng.cn/wish-admin/ugc-review/" + id_value)
        for i in range(36):
            if driver.exist('审核通过', options={'timeout': 5}):
                driver.check("UGC内容审核")
                driver.click('审核通过')
                break









