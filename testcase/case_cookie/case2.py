# -*- coding: utf-8 -*-

import requests
import json

def login():
        url = "https://beta.xdw.youxianvip.cn/api/omsAdmin/loginController/login"
        data = {"userName": "15154385201", "passWord": "123456"}
        data1 = json.dumps(data)
        header = {"Content-Type": "application/json"}
        res = requests.post(url, data=data1, headers=header).json()
            # json.dumps(res,sort_keys=False,indent=1,ensure_ascii=False)
            # token = res['data']['token']
#token = requests.utils.dict_from_cookiejar(token)
        print(res)
        #token = res['data']['token']
        # print(token)
        #return token


def get_data():
    print({'token': login()})
    url = "https://beta.xdw.youxianvip.cn/api/omsAdmin/omsSaleOrder/newOrderList/?&serviceType=OMS_ORDER"
    header = {
        'Authorization': login(),
        'Content-Type': 'application/json'
    }
    data = {"pageIndex": 1, "pageSize": 12, "searchConditionParams": []}
    data1 = json.dumps(data)
    res = requests.post(url=url, headers=header, data=data1)
    print(res.json())


if __name__ == '__main__':
    login()
    #get_data()