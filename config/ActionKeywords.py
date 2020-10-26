# !/user/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class ActionKeywords:

    driver = WebDriver

    # 打开app
    def install_app(self,object,data):
        caps = {}
        # 如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["deviceName"] = "dfp"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["autoGrantPermission"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    #点击，data无实际值传入，仅为了通过反射机制统一地使用两个函数参数调用此函数。
    def click(self,object,data):
        pass

    #输入
    def input(self,object,data):
        pass















