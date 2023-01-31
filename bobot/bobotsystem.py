from mechanism import Mechanism

class BobotSystem(Mechanism):
    def __init__(self, system: str):
        assert system in ["Windows", "Linux"]
        self.system = system

    def enter(self):
        """Press on enter """
        self.press("enter")

    def left_tab(self):
        """ Press on left tab """
        self.press("\t")

    def right_tab(self):
        """ Press on right tab """
        sefl.press("shift", "\t")

    def ctrl(self, key: str):
        """ Press on ctrl + key """
        self.press("ctrlleft", key)

    def ctrl_c(self):
        """ Ctrl V """
        self.ctrl("c")

    def ctrl_v(self):
        """ Ctrl V """
        if self.system == "Windows" : self.ctrl("v")
        if self.system == "Linux"   : self.press("ctrlleft", "shift", "v")

    def ctrl_a(self):
        """ Ctrl A """
        self.press("ctrlleft", "a")

    def write_with_cp(self, text: str):
        self.copy(text)
        self.ctrl_v()
        self.copy("")
    
    def menu(self):
        """ Open the menu """
        self.press("win")

    def go_left_desk(self):
        """ Move to left desktop """
        if self.system == "Windows" : self.press("ctrlleft", "win", "left")
        if self.system == "Linux"   : self.press("ctrlleft", "alt", "left")

    def go_right_desk(self):
        """ Move to right desktop """
        if self.system == "Windows" : self.press("ctrlleft", "win", "right")
        if self.system == "Linux"   : self.press("ctrlleft", "alt", "right")

    def switch_win(self):
        """ Switch window """
        self.press("alt", "\t")
