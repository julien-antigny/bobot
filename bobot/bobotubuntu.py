from mechanism import Mechanism

class BobotUbuntu(Mechanism):
    def __init__(self):
        pass

    def enter(self):
        """Press on enter """
        self.press("enter")

    def write(self, text: str):
        self.copy(text)
        self.press("ctrlleft", "shift", "v")
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

    def go_left_desktop(self):
        """ Move to left desktop """
        self.press("ctrlleft", "alt", "left")

    def go_right_desktop(self):
        """ Move to right desktop """
        self.press("ctrlleft", "alt", "right")

    def switch_win(self):
        """ Switch window """
        self.press("alt", "\t")
