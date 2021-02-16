# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2020 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# config.py 2021/2/13 22:52
import datetime
import time

# The data you need to fill
data = {
    # fill them:
    "username": 'fill-it',  # 学号
    "password": 'fill-it',  # 密码
    "ZXSJ": "fill-it",  # 手机
    "XM": "fill-it",  # 姓名
    "XSXB": "fill-it",  # 性别
    "NL": "fill-it",  # 年龄
    "FDYXMX": "fill-it",  # 辅导员姓名
    "SZDW": "fill-it",  # 学院全称
    "ZYMC": "fill-it",  # 专业全称
    "JJLXRXM": "fill-it",  # 家长姓名
    "JJLXRDH": "fill-it",  # 家长手机
    "JJLXRYBRGX": "fill-it",  # 和家长关系
    "sheng": "fill-it",  # 省
    "shi": "fill-it",  # 市
    "quxian": "fill-it",  # 区/县
    "DQJZDZ": "fill-it",  # 具体地址

    # choose once, then annotate others:
    "DQSFJJIA": "在家At home",
    # "DQSFJJIA": "在外Away from home",

    # choose once, then annotate others:
    "LXZT": "非学校所在城市Not in the city of the university",
    # "LXZT": "学校所在城市In the city of the university",
    # "LXZT": "境外Abroad",
}


# Don't edit this variables above

def get_DATA():
    return """
        LEFTheader:LEFT"code":0,"message":LEFT"title":"","detail":""RIGHTRIGHT,body:LEFTdataStores:LEFT"e5e7bda5-7283-4e9d-a086-37250633":LEFTrowSet:LEFT"primary":[LEFT"ZH":"{ZH}","_t":3,"XM":"{XM}","XSXB":"{XSXB}","NL":"{NL}","SZDW":"{SZDW}","ZYMC":"{ZYMC}","XSLX":"内地本科生Mainland undergraduate","ZXSJ":"{ZXSJ}","SBSJ":"{SBSJ}","FDYXMX":"{FDYXMX}","JJLXRXM":"{JJLXRXM}","JJLXRDH":"{JJLXRDH}","JJLXRYBRGX":"{JJLXRYBRGX}","LXZT":"非学校所在城市Not in the city of the university","DQSFJJIA":"{DQSFJJIA}","sheng_TEXT":"{sheng}","sheng":"{sheng}","shi_TEXT":"{shi}","shi":"{shi}","quxian_TEXT":"{quxian}","quxian":"{quxian}","DQJZDZ":"{DQJZDZ}","XQSFYQRBL":"否No","DRTW":"36.5","CLSJ":"{CLSJ}","BRSFFS":"否No","YWZZ":"无症状No symptoms","ZZLX":"","JJGDZ":"否No","JZGDZ":"否No","YSGDZ":"否No","YWZZGDZ":"无症状No symptoms","ZZLXGDZ":"","QTZZMS":"","ZKGDZ":"","SFJJYXGL":"否No","JJGLZT":"","YXGCX":"否No","JZYXGCZT":"","SFYSHQZ":"否No","QZQK":"","SFDGYQSQ":"否No","SFJCGYQ":"否No","SFJQZYQHZ":"否No","JRSFYJCS":"否No","EXCASE":"否No","EXCASECONTACT":"否No","EXFOURTEENFEVER":"否No","EXTEST":"否No","EXTESTRESULT":"否No","sflxs":"否 No","sqsfyyq":"否 No","FXQKGDZ":"","FXLYD":"","FXSJ":"","LXMDD":"","LXSJ":"","GRCN":"我承诺以上信息真实准确，并愿意承担相应法律责任。I promise that the above information is true and accurate, and I am willing to bear the corresponding legal responsibility.","FYZKGDZ":"","JZGC":"","JZGLDD":"","JJYXGC":"","JJYXGCDD":"",_o:LEFT"ZH":null,"XM":null,"XSXB":null,"NL":null,"SZDW":null,"ZYMC":null,"XSLX":null,"ZXSJ":null,"SBSJ":null,"FDYXMX":null,"JJLXRXM":null,"JJLXRDH":null,"JJLXRYBRGX":null,"LXZT":null,"DQSFJJIA":null,"sheng_TEXT":null,"sheng":null,"shi_TEXT":null,"shi":null,"quxian_TEXT":null,"quxian":null,"DQJZDZ":null,"XQSFYQRBL":null,"DRTW":null,"CLSJ":null,"BRSFFS":null,"YWZZ":null,"ZZLX":null,"JJGDZ":null,"JZGDZ":null,"YSGDZ":null,"YWZZGDZ":null,"ZZLXGDZ":null,"QTZZMS":null,"ZKGDZ":null,"SFJJYXGL":null,"JJGLZT":null,"YXGCX":null,"JZYXGCZT":null,"SFYSHQZ":null,"QZQK":null,"SFDGYQSQ":null,"SFJCGYQ":null,"SFJQZYQHZ":null,"JRSFYJCS":null,"EXCASE":null,"EXCASECONTACT":null,"EXFOURTEENFEVER":null,"EXTEST":null,"EXTESTRESULT":null,"sflxs":null,"sqsfyyq":null,"FXQKGDZ":null,"FXLYD":null,"FXSJ":null,"LXMDD":null,"LXSJ":null,"GRCN":null,"FYZKGDZ":null,"JZGC":null,"JZGLDD":null,"JJYXGC":null,"JJYXGCDD":nullRIGHTRIGHT],"filter":[],"delete":[]RIGHT,name:"e5e7bda5-7283-4e9d-a086-37250633",pageNumber:1,pageSize:2147483647,recordCount:1,rowSetName:"cecbfe49-f061-4a6a-95ff-09e39e92",parameters:LEFT"relatedcontrols":"body_0","primarykey":"pk_id","queryds":"e5e7bda5-7283-4e9d-a086-37250633"RIGHTRIGHT,"e5e7bda5-7283-4e9d-a086-37250633_record":LEFTrowSet:LEFT"primary":[],"filter":[],"delete":[]RIGHT,name:"e5e7bda5-7283-4e9d-a086-37250633_record",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"cecbfe49-f061-4a6a-95ff-09e39e92",parameters:LEFT"relatedcontrols":"body_0","primarykey":"pk_id","queryds":"e5e7bda5-7283-4e9d-a086-37250633"RIGHTRIGHT,"variable":LEFTrowSet:LEFT"primary":[LEFT"source":"interface","name":"SYS_USER","value":"{XM}","type":"string"RIGHT,LEFT"source":"interface","name":"SYS_UNIT","value":"{SZDW} ","type":"string"RIGHT,LEFT"source":"interface","name":"SYS_DATE","value":"{timestamp}","type":"date"RIGHT,LEFT"name":"1189060d-4465-4b53-89c2-c9f88457.ID_NUMBER","value":"{ZH}"RIGHT,LEFT"name":"1189060d-4465-4b53-89c2-c9f88457.USER_NAME","value":"{XM}"RIGHT,LEFT"name":"666d8a60-7108-4681-829d-545841c3.XB","value":"XSXB"RIGHT,LEFT"name":"666d8a60-7108-4681-829d-545841c3.SZYX","value":"{SZDW}"RIGHT,LEFT"name":"666d8a60-7108-4681-829d-545841c3.ZYMC","value":"{ZYMC}"RIGHT,LEFT"name":"1189060d-4465-4b53-89c2-c9f88457.MOBILE","value":"{ZXSJ}"RIGHT],"filter":[],"delete":[]RIGHT,name:"variable",pageNumber:1,pageSize:2147483647,recordCount:0,parameters:LEFTRIGHTRIGHTRIGHT,parameters:LEFT"formid":"d11d0d9b-d73a-4dad-b3c5-7d44b4ed","status":"select","privilegeId":"7374321285e4d36bbf3d274087454163","seqId":"","service_id":"41d9ad4a-f681-4872-a400-20a3b606d399","process":"674950f5-924b-463d-9eb6-21d5d1b6d9ef","strUserId":"","strUserIdCC":"","nextActId":""RIGHTRIGHTRIGHT
        """.strip().format(**data,
                           ZH=data['username'],
                           SBSJ=(datetime.utcfromtimestamp((time.time())) + timedelta(hours=8)).strftime('%Y-%m-%d'),
                           CLSJ=(datetime.utcfromtimestamp((time.time())) + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                           timestamp=str(int(round(time.time() * 1000)))).replace('LEFT', '{').replace('RIGHT', '}')


HEADERS = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "DNT":"1",
    "Host":"scenter.sdu.edu.cn",
    "Origin":"https://scenter.sdu.edu.cn",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}