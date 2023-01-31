import os
import pyperclip
from   bobotwin    import BobotWin
from   bobotubuntu import BobotUbuntu

class BobotFirefox:
    VERSION_SYSTEMES = ["windows", "ubuntu"]

    def __init__(self, system_type: str):
        assert system_type in BobotBrowser.VERSION_SYSTEMES

        self.system_type = system_type

        if self.system_type == "windows":
            self.system = BobotWin()
        else:
            self.system = BobotUbuntu()

    def reload_page(self):
        self.system.press("f5")

    def go_next_browser_tab(self):
        self.system.ctrl("\t")

    def go_prev_browser_tab(self):
        self.system.ctrl("shift", "\t")

    def open_browser_tab(self):
        self.system.ctrl("t")

    def close_browser_tab(self):
        self.system.ctrl("w")

    def open_new_browser(self):
        self.system.ctrl("n")

    def focus_search_bar(self):
        self.system.ctrl("l")

    def open_page(self, url: str):
        self.open_browser_tab()
        self.focus_search_bar()
        self.system.write(url)
        self.system.enter()

    def open_page_code_source(self):
        self.system.ctrl("u")

    def save_text_of_page(self, backup_path: str, backup_file: str, waiting_time: float = 0.5):
        """ Save text of web page """
        assert waiting_time > 0
        assert os.path.exists(backup_path)

        self.system.ctrl("a")
        self.system.wait(waiting_time)
        self.system.ctrl_c()
        
        file  = backup_path if backup_path[-1] == "/" else f"{backup_path}/"
        file += backup_file if ".html" in backup_file  else f"{backup_file}.html"

        with open(file, "w", encoding = "utf-8") as outfile:
            outfile.write(self.system.paste())

    def save_page_code_source(self, backup_path: str, backup_file: str, waiting_time: float = 0.5):
        """ Save page code source """
        self.open_code_source_page()
        self.system.wait(waiting_time)
        self.save_text_of_page(backup_path, back_file, waiting_time)