# -*- coding: utf-8 -*-

import requests
import json


def login():

    url = "https://beta.xdw.youxianvip.cn/api/omsAdmin/loginController/login"
    data = {
      "userName": "15154385201",
      "passWord": "123456"
     }
    res = requests.post(url, data).json()
    json.dumps(res, sort_keys=True, indent=10)
    print(res['data']['token'])

