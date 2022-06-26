class UtilTools:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def isElementExist(driver, element):
        flag = True
        browser = driver
        try:
            browser.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag