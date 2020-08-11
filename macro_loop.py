from multiprocessing import Process
from time import sleep


class MacroLoop(Process):
    def __init__(self, leveler_macro):
        super(MacroLoop, self).__init__()
        self.leveler_macro = leveler_macro

    def run(self):
        while True:
            self.__execute_leveler_macro()

    def __execute_leveler_macro(self):
        leveler_macro = self.leveler_macro()
        leveler_macro.daemon = True
        leveler_macro.start()
        leveler_macro.join()


if __name__ == "__main__":
    from leveler_macro import LevelerMacro

    sleep(5)
    macro_loop = MacroLoop(LevelerMacro)
    macro_loop.start()
    sleep(5)
    macro_loop.kill()
