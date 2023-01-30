import os
import pyperclip
from   bobotwin import BobotWin

class BobotBrowser(BobotWin):
    def __init__(self):
        pass

    def open_brave_with_powershell(self, url = "", incognito = False):
        """ Open Brave with a powershell command """
        incognito = "--incognito" if incognito else ""
        cmd = f"start brave \"{incognito} {url}\""
        os.system(cmd)

    def open_firefox_with_term_ubuntu(self, url = "", incognito = False):
        """ Open Firefox with terminal ubuntu """
        incognito = "--private-window" if incognito else ""
        cmd = f"firefox \"{incognito} {url}\""
        os.system(cmd)

    def reload(self):
        """ Reload page """
        self.ctrl("f5")

    def go_next_browser_tab(self):
        """ Go next browser tab """
        self.ctrl("\t")

    def go_prev_browser_tab(self):
        """ Go preview browser tab """
        self.ctrl("shift", "\t")

    def open_browser_tab(self):
        """ Open new browser tab """
        self.ctrl("t")

    def open_new_browser(self):
        """ Open new browser """
        self.ctrl("n")

    def close_browser_tab(self):
        """ Close browser tab """
        self.ctrl("w")

    def focus_search_bar(self):
        """ Focus cursor on search bar """
        self.ctrl("l")

    def open_page(self, url: str):
        """ Open a new page """
        self.open_browser_tab()
        self.focus_search_bar()
        self.write(url)
        self.enter()

    def open_page_code_source(self):
        """ Open page's code source """
        self.ctrl("u")

    def open_console(self, browser = "brave"):
        """ Open browser console """
        if browser == "brave": self.open_brave_console()
        if browser == "firefox": self.open_firefox_console()

    def open_brave_console(self):
        """ Open brave console """
        self.press("ctrlleft", "shift", "j")

    def open_firefox_console(self):
        """ Open firefox console """
        self.press("ctrlleft", "shift", "k")

    def save_text_of_page(self, backup_path: str, backup_file: str, waiting_time: float = 0.5):
        """ Save text of web page """
        assert waiting_time > 0
        assert os.path.exists(backup_path)

        self.ctrl("a")
        self.wait(waiting_time)
        self.ctrl("c")
        
        file  = backup_path if backup_path[-1] == "/" else f"{backup_path}/"
        file += backup_file if ".html" in backup_file  else f"{backup_file}.html"

        with open(file, "w", encoding = "utf-8") as outfile:
            print(self.paste()
            outfile.write(self.paste())
    
    def save_page_code_source(self, backup_path: str, backup_file: str, waiting_time: float = 0.5):
        """ Save page code source """
        self.open_code_source_page()
        self.wait(waiting_time)
        self.save_text_of_page(backup_path, back_file, waiting_time)
