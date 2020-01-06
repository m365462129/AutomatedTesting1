from poium import Page, PageElement,PageElements

class BaiduPage(Page):
    search_input = PageElement(id_="kw",describe="搜索框")
    search_button = PageElement(id_="su",describe="搜索按钮")
    settings = PageElement(link_text="设置",describe="设置下拉框")
    search_settings = PageElement(css=".setpref",describe="搜索设置选项")
    save_settings = PageElement(css=".prefpanelgo",describe="保存设置")

    search_result = PageElements(xpath="//div/h3/a",describe="搜索结果")