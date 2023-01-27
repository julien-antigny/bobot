import os
import pyperclip
from   bobotwin import BobotWin

class BobotNav(BobotWin):
    def __init__(self):
        pass

    def reload(self):
        self.ctrl("f5")

    def go_next_browser_tab(self):
        self.ctrl("\t")

    def go_prev_browser_tab(self):
        self.ctrl("shift", "\t")

    def open_browser_tab(self):
        self.ctrl("t")

    def open_new_browser(self):
        self.ctrl("n")

    def close_browser_tab(self):
        self.ctrl("w")

    def focus_search_bar(self):
        self.ctrl("l")

    def open_page(self, url: str):
        self.open_browser_tab()
        self.focus_search_bar()
        self.write(url)
        self.enter()

    def open_code_source_page(self):
        self.ctrl("u")

    def save_code_source_page(backup_path: str, backup_file: str, waiting_time: float = 0.5):
        assert waiting_time > 0
        assert os.path.exists(backup_path)

        self.open_code_source_page()
        self.ctrl("a")
        self.wait(waiting_time)
        self.ctrl("c")
        
        file  = backup_path if backup_path[-1] == "/" else f"{backup_path}/"
        file += backup_file if backup_file[-5] == ".html" else f"{backup_file}.html"

        with open(file, "w", encoding = "utf-8") as outfile:
            outfile.write(pyperclip.paste()

        self.close_browser_tab()
