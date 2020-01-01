import time

class BasePage:
    """
    基础pagen层，封装一些常用方法。
    """
    def __init__(self, driver):
        self.driver = driver

    # 打开页面url
    def openurl(self, url=None):
        if url is not None:
            self.url = url
            self.driver.get(url)
        else:
            self.driver.get(self.url)

    # id 定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    # xpath 定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # css 定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)
        
    # name 定位
    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    # class 定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text，仅使用xpath定位
    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)

    # 封装休眠时间
    def sleep(self, sec):
        time.sleep(sec)