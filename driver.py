from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///C:/michael/work/Hackend/projects/HanukkahWinners/results.html")

    def refresh(self):
        self.driver.refresh()
