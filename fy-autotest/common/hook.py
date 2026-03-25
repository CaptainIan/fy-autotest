import json
import os.path
import time
from fasttest import driver, gvar, requests, logger

def setUpGlobal():
    pass

def tearDownGlobal():
    try:
        driver.stop()
    except:
        pass

def setUp(test):
    driver.browser(gvar.config)

def tearDown(test):
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
 