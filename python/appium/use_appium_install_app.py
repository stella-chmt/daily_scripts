

import os
from appium import webdriver
from time import sleep

def install_app_to_stimulator():
     # set up appium
    app = os.path.join(os.path.dirname(__file__),
                       '/Users/mengting/Downloads',
                       'DPScope.app')
    app = os.path.abspath(app)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'iOS',
            'platformVersion': '7.1',
            'deviceName': 'iPhone Simulator'
        })
    sleep(2)

install_app_to_stimulator()
