from poium import Page, PageElement,PageElements
from .base_page import BasePage

class Job51Page(Page,BasePage):
    """Job51 Page层"""
    search_input = PageElement(id_="kwdselectid")
    search_btn = PageElement(css = ".ush > button:nth-child(2)")
    zhankai_btn = PageElement(css="div.op:nth-child(16) > span:nth-child(1) > em:nth-child(1)")
    jiagezhankai_btn = PageElement(css="#filter_providesalary > span:nth-child(3)")
    jiageok_btn = PageElement(xpath="//*[@id='submit_providesalary']")


    
    #数组
    def getjiage_list(self):
        jiagebtn_list = []
        for i in range(8,13):
            csspath = "#multichoices_providesalary > ul:nth-child(2) > li:nth-child("+ str(i) +") > a:nth-child(1)"
            jiagebtn_list.append(self.by_css(csspath))
        return jiagebtn_list