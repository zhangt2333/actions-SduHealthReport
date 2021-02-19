# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2020 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333
# main.py 2021/2/13 23:31
import json
import re
import sys
import config
import spider
from uniform_login.uniform_login_spider import login

if __name__ == '__main__':
    config.data = json.loads(re.sub('#(.*)\n', '\n', sys.argv[1]).replace("'", '"'))
    spider.report(JSESSIONID=login(config.data['username'], config.data['password'], 'https://scenter.sdu.edu.cn/tp_fp/view'))