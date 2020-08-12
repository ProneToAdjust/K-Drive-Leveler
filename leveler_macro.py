import keyboard
import mouse
from time import sleep
from threading import Thread


class LevelerMacro(Thread):
    __KEYBOARD = 0
    __MOUSE = 0

    def __init__(self):
        super(LevelerMacro, self).__init__()
        self.movement_thread = None

        self.daemon = True
        
    def run(self):
        self.__execute_macro()

    def __execute_macro(self):
        # While moving forward, execute air routine
        self.movement_thread = Thread(target=self.__forward)
        self.movement_thread.daemon = True
        self.movement_thread.start()

        self.__air_routine()

        self.movement_thread.join()

        # While moving backwards, execute air routine
        self.movement_thread = Thread(target=self.__backward)
        self.movement_thread.daemon = True
        self.movement_thread.start()

        self.__air_routine()

        self.movement_thread.join()

    def __forward(self):
        self.__hold(self.__KEYBOARD, 'w', 5)

    def __backward(self):
        self.__hold(self.__KEYBOARD, 's', 5)

    def __air_routine(self):
        # Jump
        self.__hold(self.__KEYBOARD, 'space', 2)
        sleep(0.35)

        # Nose Planker
        mouse.press(mouse.RIGHT)
        sleep(0.075)
        mouse.release(mouse.RIGHT)
        sleep(0.35)

        # Copter
        keyboard.press_and_release('space')
        sleep(0.35)

        # Nose Planker
        mouse.press(mouse.RIGHT)
        sleep(0.075)
        mouse.release(mouse.RIGHT)
        sleep(0.35)

        # Copter
        keyboard.press_and_release('space')
        sleep(0.35)

        # Nose Planker
        mouse.press(mouse.RIGHT)
        sleep(0.075)
        mouse.release(mouse.RIGHT)
        sleep(0.35)

        # Copter
        keyboard.press_and_release('space')

    def __hold(self, peripheral, key, seconds):
        if peripheral == self.__KEYBOARD:
            keyboard.press(key)
            sleep(seconds)
            keyboard.release(key)
            
        elif peripheral == self.__MOUSE:
            mouse.press(key)
            sleep(seconds)
            mouse.release(key)


if __name__ == "__main__":
    leveler_macro = LevelerMacro()
    sleep(5)
    leveler_macro.start()
    leveler_macro.join()