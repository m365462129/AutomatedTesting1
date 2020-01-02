from poium import Page, PageElement

class CategoryPage(Page):
    """CategoryPage层"""
    menu_ele = PageElement(css="#banner_left_ul > a:nth-child(1) > li:nth-child(1) > span:nth-child(1)")
    # buy_btn = PageElement(css=".learn_btn > span:nth-child(1)")