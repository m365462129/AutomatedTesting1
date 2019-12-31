from poium import Page, PageElement

class LoginOrderPage(Page):
    """LoginOrderPagePage层"""
    video_ele = PageElement(css=".type_content > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)")
    buy_btn = PageElement(css=".learn_btn > span:nth-child(1)")