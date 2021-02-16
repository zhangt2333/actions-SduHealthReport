# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2020 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# spider.py.py 2021/2/13 21:27
import requests
import config


def report(JSESSIONID):
    try:
        config.HEADERS['Cookie'] = 'JSESSIONID=' + JSESSIONID
        config.HEADERS['Content-Type'] = 'text/plain;charset=UTF-8'
        config.HEADERS['Referer'] = 'https://scenter.sdu.edu.cn/tp_fp/formParser?status=select&formid=d11d0d9b-d73a-4dad-b3c5-7d44b4ed&service_id=41d9ad4a-f681-4872-a400-20a3b606d399&process=674950f5-924b-463d-9eb6-21d5d1b6d9ef&seqId=&privilegeId=7374321285e4d36bbf3d274087454163'
        response = requests.post(
            url='https://scenter.sdu.edu.cn/tp_fp/formParser?status=update&formid=d11d0d9b-d73a-4dad-b3c5-7d44b4ed&workflowAction=startProcess&seqId=&workitemid=&process=674950f5-924b-463d-9eb6-21d5d1b6d9ef',
            headers=config.HEADERS,
            data=config.DATA.encode('utf-8')
        )
        if response.status_code != 200:
            return False
        print('========= report SUCCESS =========')
        config.HEADERS['Content-Type'] = 'application/json;charset=UTF-8'
        config.HEADERS['Referer'] = 'https://scenter.sdu.edu.cn/tp_fp/view?m=fp'
        response = requests.post(
            url='https://scenter.sdu.edu.cn/tp_fp/fp/formHome/updateVisit',
            headers=config.HEADERS,
            data=dict(server_id="41d9ad4a-f681-4872-a400-20a3b606d399")
        )
        if response.status_code == 200:
            print('========= updateVisit SUCCESS =========')
            return True
    except Exception as e:
        print(e)
        return False