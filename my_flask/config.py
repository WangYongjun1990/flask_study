# -*- coding:utf-8 -*-

"""
File Name: `config`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/12 11:48
"""


class Config:
    # SECRET_KEY = os.urandom (24)
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://autotestuat:Autotestuat@123@192.168.10.2:3306/autotest_result?"
    #                            "charset=utf8")
    # SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://yongjun.wang:1qaz@WSX@192.168.10.2:3306/mitest_platform?"
    #                            "charset=utf8")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mitest_platform?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True

    JSON_AS_ASCII = False
