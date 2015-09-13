import os
from optparse import OptionParser
import chrome_shell.define as define
import chrome_shell.util as util

SRC_DIR = os.path.dirname(__file__)
SCRIPT_DIR = SRC_DIR + "/../../scripts"

class Command(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.msg = "%prog COMMAND [OPTIONS]" + "\n" + "COMMAND:" + "\n"
        self.msg += util.get_message(self.name)
        self.err_msg = util.get_err_message(self.name)
        self.parser = OptionParser(usage=self.msg[: -1], prog=define.PROG,
            version=define.VERSION, add_help_option=False)
        self.parser.disable_interspersed_args()

    def run(self):
        if self.check_args():
            pass
        else:
            return

        if self.name == "click":
            self.run_click()
        elif self.name == "mouse":
            self.run_mouse()
        elif self.name == "wmove":
            self.run_wmove()
        elif self.name == "scroll":
            self.run_scroll()
        elif self.name == "wsize":
            self.run_wsize()
        elif self.name == "tab":
            self.run_tab()
        elif self.name == "back":
            self.run_back()
        elif self.name == "next":
            self.run_next()
        elif self.name == "reload":
            self.run_reload()
        elif self.name == "cancel":
            self.run_cancel()
        elif self.name == "home":
            self.run_home()
        elif self.name == "launch":
            self.run_launch()
        elif self.name == "relaunch":
            self.run_relaunch()
        elif self.name == "quit":
            self.run_quit()
        elif self.name == "open":
            self.run_open()
        elif self.name == "close":
            self.run_close()
        elif self.name == "search":
            self.run_search()
        elif self.name == "url":
            self.run_url()

    def check_args(self):
        if (len(self.args) != 0) == define.command_fargs[self.name]:
            return True
        else:
            self.parser.print_help()
            self.parser.error(self.err_msg)
            return False

    def run_click(self):
        return

    def run_mouse(self):
        return

    def run_wmove(self):
        return

    def run_scroll(self):
        return

    def run_wsize(self):
        return

    def run_tab(self):
        return

    def run_back(self):
        path = SCRIPT_DIR + "/back.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_next(self):
        path = SCRIPT_DIR + "/next.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_reload(self):
        path = SCRIPT_DIR + "/reload.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_cancel(self):
        path = SCRIPT_DIR + "/load_cancel.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_home(self):
        path = SCRIPT_DIR + "/home.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_launch(self):
        path = SCRIPT_DIR + "/activate.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_relaunch(self):
        path = SCRIPT_DIR + "/restart.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_quit(self):
        path = SCRIPT_DIR + "/quite.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_open(self):
        path = SCRIPT_DIR + "/reopen.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_close(self):
        path = SCRIPT_DIR + "/close.scpt"
        if os.path.exists(path):
            os.system(path)
        return

    def run_search(self):
        return

    def run_url(self):
        return

