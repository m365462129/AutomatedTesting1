from poium import Page, PageElement

class Job51Page(Page):
    """Job51 Page层"""
    search_input = PageElement(id_="kwdselectid")
    search_btn = PageElement(css = ".ush > button:nth-child(2)")