import keyboard
import mouse
from mod_selection_gui import ModSelectionGui
from macro_loop import MacroLoop
from leveler_macro import LevelerMacro
from multiprocessing import freeze_support


class KDriveLeveler: 
    def __init__(self):
        self.macro_loop = None
        self.exit_keypress_listener = None

        self.mod_selection_gui = ModSelectionGui()

    def start(self):
        self.__start_exit_keypress_listener()
        self.mod_selection_gui.start()
        pass

    def stop(self):
        pass

    def __start_exit_keypress_listener(self):
        keyboard.on_press_key('ctrl', self.__on_press)

    def __on_press(self, key):
        self.__toggle_macro_loop()
        self.mod_selection_gui.toggle_checkbutton_states()
        self.mod_selection_gui.toggle_macro_status_message()

    def __toggle_macro_loop(self):
        if self.macro_loop is not None and self.macro_loop.is_alive():
            self.__stop_macro_loop()
            self.__release_keys()
        
        else:
            # Restart macro loop
            self.__start_macro_loop()

    def __start_macro_loop(self):
        checkbutton_values = self.mod_selection_gui.get_checkbutton_values()

        movement_time, jump_charge_time, after_jump_time, trick_cycles = self.__calculate_macro_timings(checkbutton_values)

        leveler_macro = LevelerMacro(
            movement_time, 
            jump_charge_time, 
            after_jump_time, 
            trick_cycles
            )

        self.macro_loop = MacroLoop(leveler_macro)
        self.macro_loop.start() 

    def __stop_macro_loop(self):
        if self.macro_loop is not None and self.macro_loop.is_alive():
            self.macro_loop.kill()

    def __release_keys(self):
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release('space')
        mouse.release(mouse.RIGHT)

    def __calculate_macro_timings(self, checkbutton_values):
        pop_top = checkbutton_values['Pop Top']
        air_time = checkbutton_values['Air Time']
        venedro_hoverdrive = checkbutton_values['Venedro Hoverdrive']
        poppin_vert = checkbutton_values["Poppin' Vert"]

        # Default macro timings
        movement_time = 5
        jump_charge_time = 2
        after_jump_time = 0.35
        trick_cycles = 3

        if pop_top:
            jump_charge_time = 1
            movement_time -= 1

        if poppin_vert:
            after_jump_time = 2
            movement_time += 2

        if air_time and venedro_hoverdrive:
            trick_cycles += 1
            movement_time += 1
        
        elif air_time ^ venedro_hoverdrive:
            movement_time += 0.5


        return movement_time, jump_charge_time, after_jump_time, trick_cycles

def main():
    k_drive_leveler = KDriveLeveler()
    k_drive_leveler.start()


if __name__ == "__main__":
    freeze_support()
    main()
