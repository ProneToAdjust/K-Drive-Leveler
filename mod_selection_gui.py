from tkinter import Tk, Checkbutton, Label, IntVar, X, Button, BOTTOM


class ModSelectionGui:
    MACRO_RUNNING = 'Macro running'
    MACRO_STOPPED = 'Macro stopped'

    def __init__(self):
        self.__build_gui()

    def start(self):
        self.root.mainloop()

    def __build_gui(self):
        self.global_padx = 5
        self.global_pady = 1

        self.root = Tk()

        self.root.title('KDrive Leveler')

        self.root.minsize(180, 0)
        self.root.resizable(False, False)

        self.pop_top_var = IntVar()
        self.air_time_var = IntVar()
        self.venedro_hoverdrive_var = IntVar()
        self.poppin_vert_var = IntVar()

        # Mod Selection Header
        self.mod_selection_label = Label(text='Mods equipped:')
        self.mod_selection_label.pack(anchor='w', padx=self.global_padx)

        # Pop top
        self.pop_top = Checkbutton(
            text='Pop Top',
            variable=self.pop_top_var
            )
        self.pop_top.pack(anchor='w', padx=self.global_padx)

        # Air time
        self.air_time = Checkbutton(
            text='Air Time',
            variable=self.air_time_var
            )
        self.air_time.pack(anchor='w', padx=self.global_padx)

        # Venedro Hoverdrive
        self.venedro_hoverdrive = Checkbutton(
            text='Venedro Hoverdrive',
            variable=self.venedro_hoverdrive_var
            )
        self.venedro_hoverdrive.pack(anchor='w', padx=self.global_padx)

        # Poppin' vert
        self.poppin_vert = Checkbutton(
            text="Poppin' Vert",
            variable=self.poppin_vert_var
            )
        self.poppin_vert.pack(anchor='w', padx=self.global_padx)

        # Macro instruction
        self.macro_instruction = Label(
            text='Toggle macro (CTRL)',
            borderwidth=1,
            relief='sunken'
            )
        self.macro_instruction.pack(padx=self.global_padx, pady=(5,2), fill=X)

        # Macro status
        self.macro_status = Label(
            text='Macro stopped',
            borderwidth=1,
            relief='sunken'
            )
        self.macro_status.pack(padx=self.global_padx, pady=(2,5), fill=X)

    def get_checkbutton_values(self):
        checkbutton_states = {
            self.pop_top['text'] : self.pop_top_var.get(),
            self.air_time['text'] : self.air_time_var.get(),
            self.venedro_hoverdrive['text'] : self.venedro_hoverdrive_var.get(),
            self.poppin_vert['text'] : self.poppin_vert_var.get()
        }

        return checkbutton_states

    def toggle_macro_status_message(self):
        if self.macro_status['text'] == self.MACRO_STOPPED:
            self.macro_status['text'] = self.MACRO_RUNNING

        else:
            self.macro_status['text'] = self.MACRO_STOPPED

    def toggle_checkbutton_states(self):
        if self.pop_top['state'] == 'disabled':
            self.enable_checkbuttons()

        else:
            self.disable_checkbuttons()

    def enable_checkbuttons(self):
        self.pop_top['state'] = 'active'
        self.air_time['state'] = 'active'
        self.venedro_hoverdrive['state'] = 'active'
        self.poppin_vert['state'] = 'active'

    def disable_checkbuttons(self):
        self.pop_top['state'] = 'disabled'
        self.air_time['state'] = 'disabled'
        self.venedro_hoverdrive['state'] = 'disabled'
        self.poppin_vert['state'] = 'disabled'


if __name__ == "__main__":
    mod_selection_gui = ModSelectionGui()
    mod_selection_gui.start()
