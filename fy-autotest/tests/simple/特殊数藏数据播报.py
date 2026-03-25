import requests
import sys
import pymysql
from fasttest import TestCase, driver, gvar, logger



# 飞书机器人 Webhook 地址
feishu_webhook = ''
db_config_t = {
            'user': gvar.data.dc.user,
            'password': gvar.data.dc.password,
            'host': gvar.data.dc.host,
            'port': int(gvar.data.dc.port),
            'database': gvar.data.dc.database
        }


def query_dc_count(dc_ids):
    global connection
    try:
        # 连接到数据库
        connection = pymysql.connect(**db_config_t)
        with connection.cursor() as cursor:

            placeholders = ', '.join(['%s'] * len(dc_ids))
            query = "select d.collection_id ,COUNT(1)  from xf_dc.DC_TICKETS d WHERE d.collection_id in ("+placeholders+") and d.active_status = 1 GROUP by d.collection_id;"

            cursor.execute(query, dc_ids)

        # 获取查询结果
            results = cursor.fetchall()
            return results
    except pymysql.Error as e:
        print("操作数据库时出错:" + e)
    finally:
        # 关闭数据库连接
        if connection:
            connection.close()


def assemble_message(lst,dc_ids):
    message_result = ['特殊系列数藏业务情况','当前环境为TEST']
    first_elements = [item[0] for item in lst]
    for dc_id in dc_ids:
        if dc_id not in first_elements:
            lst.append((dc_id, 0))
    lst.sort(key=lambda x: x[0])
    for dc_id, count in lst:
        info = "夏·新蝉噪·创，数藏id:" + str(dc_id) + ",  激活数量:" + str(count)
        message_result.append(info)
    final_message_result = "\n".join(message_result)
    return final_message_result


def send_to_feishu(message):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    try:
        response = requests.post(feishu_webhook, json=data, headers=headers)
        response.raise_for_status()
        print("消息已成功发送到飞书群")
    except requests.RequestException as err:
        print("发送消息到飞书群时出错: " + err)


class TestCase(TestCase):

    def test_dc_data_to_feishu(self):

    # xf_dc_mysql_connect = sys.argv[1]
    # xf_dc_ids_str = sys.argv[2]
    # xf_dc_host, xf_dc_user, xf_dc_pass, xf_dc_port = xf_dc_mysql_connect.split('|')
    # db_config1 = {
    #     'user': xf_dc_user,
    #     'password': xf_dc_pass,
    #     'host': xf_dc_host,
    #     'port': int(xf_dc_port),
    #     'database': 'xf_dc',
    # }
        db_config_p = {
            'user': gvar.data.dc.user,
            'password': gvar.data.dc.password,
            'host': gvar.data.dc.host,
            'port': gvar.data.dc.host,
            'database': gvar.data.dc.database,
        }

        #xf_dc_ids = [int(i) for i in xf_dc_ids_str.split(',')]
        xf_dc_ids = [11827, 11828, 11829, 11830, 11832, 11833]
        count = list(query_dc_count(xf_dc_ids))
        print(count)
        message = assemble_message(count,xf_dc_ids)
        print(message)
        send_to_feishu(message)


