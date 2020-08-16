import keyboard
import mouse
from macro_loop import MacroLoop
from leveler_macro import LevelerMacro
from multiprocessing import freeze_support


class KDriveLeveler: 
    def __init__(self):
        self.macro_loop = None
        self.exit_keypress_listener = None

    def start(self):
        self.__start_exit_keypress_listener()
        pass

    def stop(self):
        pass

    def __start_exit_keypress_listener(self):
        keyboard.on_press_key('ctrl', self.__on_press)

    def __on_press(self, key):
        self.__toggle_macro_loop()

    def __toggle_macro_loop(self):
        if self.macro_loop is not None and self.macro_loop.is_alive():
            self.__stop_macro_loop()
            self.__release_keys()
            print('Macro stopped')
        
        else:
            # Restart macro loop
            self.__start_macro_loop()

    def __start_macro_loop(self):
        self.macro_loop = MacroLoop(LevelerMacro())
        self.macro_loop.start() 
        print('Macro started')

    def __stop_macro_loop(self):
        if self.macro_loop is not None and self.macro_loop.is_alive():
            self.macro_loop.kill()

    def __release_keys(self):
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release('space')
        mouse.release(mouse.RIGHT)


def main():
    print('Press CTRL to toggle the macro')

    k_drive_leveler = KDriveLeveler()
    k_drive_leveler.start()

    while True:
        pass


if __name__ == "__main__":
    freeze_support()
    main()
