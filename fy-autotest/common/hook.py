import json
import os.path
import time
from fasttest import driver, gvar, requests, logger


def _is_api_test(test) -> bool:
    """判断当前用例是否为接口测试（类上标记 _api_test_only = True）"""
    return getattr(test.__class__, '_api_test_only', False)


def setUpGlobal():
    # 接口测试：从配置中设置 base_url
    api_base_url = gvar.config.api_base_url if gvar.config else None
    if api_base_url:
        requests.set_base_url(api_base_url)


def tearDownGlobal():
    try:
        driver.stop()
    except:
        pass


def setUp(test):
    # 接口测试：跳过浏览器启动
    if _is_api_test(test):
        return
    driver.browser(gvar.config)


def tearDown(test):
    # 接口测试：把请求记录写入报告，跳过截图/视频
    if _is_api_test(test):
        if requests.call_log:
            test.request = list(requests.call_log)
            requests.clear_call_log()
        return
    try:
        # 保存截图
        screenshot_path = os.path.join(test.reports_assets, f'{time.time()}.png')
        driver.screenshot(path=screenshot_path)
        test.screenshot_path = screenshot_path
        # 保存视频
        video_path = driver.video()
        test.video_path = video_path
        # 保存请求
        request = driver.save_request([
            gvar.data.exchange.domains
        ])
        test.request = request
        # 关闭驱动
        driver.close()
    except Exception as e:
        logger.log_error(e)
 