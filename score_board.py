from htmler import print_to_html
from driver import WebDriver


class ScoreBoard:

    def __init__(self):
        self.score_board = {}
        print_to_html(self.score_board, "results.html")
        self.driver = WebDriver()

    def add(self, name, score):
        self.score_board[name] = score
        print_to_html(self.score_board, "results.html")
        self.driver.refresh()
