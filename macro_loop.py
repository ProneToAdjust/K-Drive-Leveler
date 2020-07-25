from multiprocessing import Process
from leveler_macro import LevelerMacro
from time import sleep


class MacroLoop(Process):
    def __init__(self):
        super(MacroLoop, self).__init__()
        self.leveler_macro = None

    def run(self):
        while True:
            self.__execute_leveler_macro()

    def __execute_leveler_macro(self):
        self.leveler_macro = LevelerMacro()
        self.leveler_macro.daemon = True
        self.leveler_macro.start()
        self.leveler_macro.join()


if __name__ == "__main__":
    sleep(5)
    macro_loop = MacroLoop()
    macro_loop.start()
    sleep(5)
    macro_loop.kill()
