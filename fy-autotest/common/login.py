from fasttest import driver, gvar
import json
from common import dmsaApiLogin


class Login(object):


    def login_dms_plus(self, uri: str = '#/login') -> None:
        """
        dms登录
        """
        host = gvar.data.exchange.host
        login_url = f'{host}/{uri}'
        driver.page(login_url)
        access_token = dmsaApiLogin.get_login_token()
        bearer_token = f"Bearer {access_token}"
        WMP_expires_in = 86400
        driver.evaluate(f"window.sessionStorage.setItem('WMP_token', '{bearer_token}');")
        driver.evaluate(f"window.sessionStorage.setItem('WMP_userName', '{gvar.data.exchange.userId}');")
        driver.evaluate(f"window.sessionStorage.setItem('WMP_expires_in', '{WMP_expires_in}');")
        driver.reload()
        driver.waitfor(state="visible", selector="首页")


