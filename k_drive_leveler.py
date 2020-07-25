import keyboard
from macro_loop import MacroLoop
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
            self.macro_loop.kill()
            print('Macro stopped')
        
        else:
            # Restart macro loop
            self.__start_macro_loop()

    def __start_macro_loop(self):
        self.macro_loop = MacroLoop()
        self.macro_loop.start() 
        print('Macro started')


def main():
    print('Press CTRL to toggle the macro')

    k_drive_leveler = KDriveLeveler()
    k_drive_leveler.start()

    while True:
        pass


if __name__ == "__main__":
    freeze_support()
    main()
