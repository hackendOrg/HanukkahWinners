from htmler import print_to_html
from driver import WebDriver
from operator import itemgetter


class ScoreBoard:

    def __init__(self):
        self.score_board = {}
        print_to_html({}, "results.html")
        self.driver = WebDriver()

    def add(self, name, score):
        self.score_board[name] = score
        tmp_list = self.get_sorted_key()
        tmp_list.reverse()
        print_to_html(tmp_list, "results.html")
        self.driver.refresh()

    def get_sorted_key(self):
        return sorted(self.score_board.items(), key=lambda kv: kv[1])