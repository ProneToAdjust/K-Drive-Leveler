import keyboard
import mouse
from time import sleep
from threading import Thread


class LevelerMacro():
    __KEYBOARD = 0
    __MOUSE = 0

    def __init__(
        self, 
        movement_time=5, 
        jump_charge_time=2, 
        after_jump_time=0.35, 
        trick_cycles=3
        ):
        super(LevelerMacro, self).__init__()
        self.movement_time = movement_time
        self.jump_charge_time = jump_charge_time
        self.after_jump_time = after_jump_time
        self.trick_cycles = trick_cycles

        self.movement_thread = None

        self.daemon = True

    def start(self):
        self.__execute_macro(
            self.movement_time, 
            self.jump_charge_time, 
            self.after_jump_time, 
            self.trick_cycles
            )

    def __execute_macro(
        self, 
        movement_time, 
        jump_charge_time, 
        after_jump_time, 
        trick_cycles
        ):
        # While moving forward, execute air routine
        self.movement_thread = Thread(target=self.__forward, args=[movement_time])
        self.movement_thread.daemon = True
        self.movement_thread.start()

        self.__air_routine(jump_charge_time, after_jump_time, trick_cycles)

        self.movement_thread.join()

        # While moving backwards, execute air routine
        self.movement_thread = Thread(target=self.__backward, args=[movement_time])
        self.movement_thread.daemon = True
        self.movement_thread.start()

        self.__air_routine(jump_charge_time, after_jump_time, trick_cycles)

        self.movement_thread.join()

    def __forward(self, seconds):
        self.__hold(self.__KEYBOARD, 'w', seconds)

    def __backward(self, seconds):
        self.__hold(self.__KEYBOARD, 's', seconds)

    def __air_routine(self, jump_charge_time, after_jump_time, trick_cycles):
        # Jump
        self.__hold(self.__KEYBOARD, 'space', jump_charge_time)

        # After jump delay
        sleep(after_jump_time)

        last_loop = trick_cycles - 1

        for loop in range(trick_cycles):
            # Nose Planker
            mouse.press(mouse.RIGHT)
            sleep(0.075)
            mouse.release(mouse.RIGHT)

            # Delay
            sleep(0.35)

            # Copter
            keyboard.press_and_release('space')

            if loop is not last_loop:
                # Delay
                sleep(0.35)

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
    movement_time = 5
    jump_charge_time = 2
    after_jump_time = 0.35
    trick_cycles = 3

    leveler_macro = LevelerMacro()
    sleep(5)
    leveler_macro.start()
