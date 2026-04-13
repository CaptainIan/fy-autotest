import os
import copy
from faker import Faker
from fasttest import driver, gvar


class Common(object):

    def add_address(self, name: str, address: str) -> None:
        pass

    def check_address(self):
        pass

    def select_position(self) -> None:
        pass

    def upload(self, path: str, action: str, index: int = 0) -> None:
        driver.upload(f'{os.path.join(gvar.resource, path)}', action, index)
        if not driver.not_exist('重新上传', options={'timeout': 6}):
            driver.upload(f'{os.path.join(gvar.resource, path)}', '重新上传')
