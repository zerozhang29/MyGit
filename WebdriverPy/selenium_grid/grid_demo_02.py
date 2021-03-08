from selenium.webdriver import Remote, DesiredCapabilities

# 引用Firefox浏览器配置
driver = Remote(command_executor='http://192.168.183.1:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.FIREFOX.copy())
driver.get("http://www.baidu.com")
# ……
