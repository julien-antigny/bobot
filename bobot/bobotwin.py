from mechanism import Mechanism

class BobotWin(Mechanism):
    def __init__(self):
        pass

    def enter(self):
        """Press on enter """
        self.press("enter")

    def write(self, text: str):
        self.copy(text)
        self.ctrl("v")
        self.copy("")

    def left_tab(self):
        """ Press on left tab """
        self.press("\t")

    def right_tab(self):
        """ Press on right tab """
        sefl.press("shift", "\t")

    def ctrl(self, key: str):
        """ Press on ctrl + key """
        self.press("ctrlleft", key)

    def win(self):
        """ Press on windows button """
        self.press("win")

    def go_left_desktop(self):
        """ Move to left desktop """
        self.press("ctrlleft", "win", "left")

    def go_right_desktop(self):
        """ Move to right desktop """
        self.press("ctrlleft", "win", "right")

    def switch_win(self):
        """ Switch window """
        self.press("alt", "\t")
