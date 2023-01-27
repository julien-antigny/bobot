import pyperclip
from time import sleep
import pyautogui as pt
from typing import Tuple

class Mechanism:
    def __init__(self):
        pass

    def get_position(self) -> Tuple[int, int]:
        """ Get cursor position """
        position = pt.position()
        return (position.x, position.y)

    def move_to(self, x: int, y: int):
        """ Move the cursor to the pixel (x, y) """
        assert x > 0 and y > 0
        pt.moveTo(x, y)

    def left_click(self, x: int, y: int):
        """ Make a left click on the pixel (x, y) """
        assert x > 0 and y > 0
        pt.click(x, y)

    def right_click(self, x: int, y: int):
        """ Make a right click on the pixel (x, y) """
        assert x > 0 and y > 0
        pt.click(x = x, y = y, button = "right")

    def press(self, *keys: str):
        """ Press the keys on the keyboard """
        pt.hotkey(*keys)

    def scroll(self, x: int):
        """ Scroll """
        pt.scroll(x)

    def left_click_with_key_pressed(self, key: str, x: int, y: int):
        """ Make a left click with key_pressed """
        with pt.hold(key):
            pt.click(x = x, y = y)
 
    def right_click_with_key_pressed(self, key: str, x: int, y: int):
        """ Make a right click with key_pressed """
        with pt.hold(key):
            pt.click(x = x, y = y, button = "right")

    def wait(self, waiting_time: float):
        """ Wait """
        assert waiting_time > 0
        sleep(waiting_time)

    def copy(self, text: str):
        """ Add a text in  clipboard """
        pyperclip.copy(text)

    def paste(self):
        """ Paste the current text from the clipboard """
        pyperclip.paste()
