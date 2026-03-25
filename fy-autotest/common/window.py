import copy
from fasttest import driver, gvar


class Window(object):

    def h5_window(self, options: dict = {}) -> None:
        key = options.get('key', 'DEFAULT_WINDOW')
        host = options.get('host', gvar.data.exchange.sfa_host)
        cp_gvar = copy.deepcopy(gvar)
        device_info = driver.devices('iPhone 14')
        device_info.update({
            'viewport': {'width': 390, 'height': 960},
            'user_agent': 'Mozilla/5.0 (Linux; Android 16; PGEM10 Build/BP2A.250605.015; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.135 Mobile Safari/537.36'
        })
        context = {k: v for d in [cp_gvar.config.context, device_info, options] for k, v in d.items() if v is not None}
        context['base_url'] = host
        cp_gvar.config['context'] = context
        driver.window(key=key, config=cp_gvar.config)

    def web_window(self, options: dict = {}) -> None:
        key = options.get('key', 'DEFAULT_WINDOW')
        cp_gvar = copy.deepcopy(gvar)
        driver.window(key=key, config=cp_gvar.config)
