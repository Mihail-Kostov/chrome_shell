import os
from optparse import OptionParser
import chrome_shell.define as define
import chrome_shell.util as util

SRC_DIR = os.path.dirname(__file__)
SCRIPT_DIR = SRC_DIR + "/../../scripts"

class Command(object):
    def __init__(self, name, args):
        self.name = name.lower()
        self.args = args
        self.msg = "%prog SUBCOMMAND [OPTIONS]" + "\n" + "SUBCOMMAND:" + "\n"
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
        elif self.name == "abort":
            self.run_abort()
        elif self.name == "home":
            self.run_home()
        elif self.name == "start":
            self.run_start()
        elif self.name == "restart":
            self.run_restart()
        elif self.name == "stop":
            self.run_stop()
        elif self.name == "wopen":
            self.run_wopen()
        elif self.name == "wclose":
            self.run_wclose()
        elif self.name == "search":
            self.run_search()
        elif self.name == "url":
            self.run_url()
        elif self.name == "typo":
            self.run_typo()

    def check_args(self):
        if (len(self.args) != 0) == define.command_fargs[self.name]:
            return True
        else:
            #self.parser.print_help()
            self.parser.error(self.err_msg)
            return False

    def run_click(self):
        arg = self.args[0]
        path = SCRIPT_DIR + "/click.scpt"
        if os.path.exists(path) :
            pass
        else:
            self.parser.print_help()
            self.parser.error(util.get_err_option(self.name))
            return

        if arg.lower() == "c" or arg.lower() == "single" or arg.lower() == "s":
            path = path + " c"
        elif arg.lower() == "dc" or arg.lower() == "double" or arg.lower() == "d":
            path = path + " dc"
        elif arg.lower() == "tc" or arg.lower() == "triple" or arg.lower() == "t":
            path = path + " tc"
        elif arg.lower() == "rc" or arg.lower() == "right" or arg.lower() == "r":
            path = path + " rc"
        else:
            self.parser.error(util.get_err_option(self.name))
            return

        self.execute(path)
        return

    def run_mouse(self):
        path = SCRIPT_DIR + "/move_mouse.scpt"
        x = 0
        y = 0
        for key in self.args:
            if key.lower() == "u" or key.lower() == "up":
                y = y - 25
            elif key.lower() == "d" or key.lower() == "down":
                y = y + 25
            elif key.lower() == "r" or key.lower() == "right":
                x = x + 25
            elif key.lower() == "l" or key.lower() == "left":
                x = x - 25

        def convert_str(num):
            if num >= 0:
                return "+%d" %num
            else:
                return "%d" %num

        if (x != 0 or y != 0) and os.path.exists(path) :
            option = " %s %s" %(convert_str(x), convert_str(y))
            self.execute(path + option)
        else:
            self.parser.error(util.get_err_option(self.name))
        return

    def run_wmove(self):
        arg = self.args[0]
        path = ""
        if arg.lower() == "l" or arg.lower() == "left":
            path = SCRIPT_DIR + "/move_left.scpt"
        elif arg.lower() == "r" or arg.lower() == "right":
            path = SCRIPT_DIR + "/move_right.scpt"

        if path != "" and os.path.exists(path) :
            self.execute(path)
        else:
            self.parser.error(util.get_err_option(self.name))
        return

    def run_scroll(self):
        arg = self.args[0]
        path = ""
        if arg.lower() == "u" or arg.lower() == "up":
            path = SCRIPT_DIR + "/up_scroll.scpt"
        elif arg.lower() == "d" or arg.lower() == "down":
            path = SCRIPT_DIR + "/down_scroll.scpt"
        elif arg.lower() == "r" or arg.lower() == "right":
            path = SCRIPT_DIR + "/right_scroll.scpt"
        elif arg.lower() == "l" or arg.lower() == "left":
            path = SCRIPT_DIR + "/left_scroll.scpt"

        if path != "" and os.path.exists(path) :
            self.execute(path)
        else:
            self.parser.error(util.get_err_option(self.name))
        return

    def run_wsize(self):
        arg = self.args[0]
        path = ""
        if arg.lower() == "hu":
            path = SCRIPT_DIR + "/twice_h.scpt"
        elif arg.lower() == "hd":
            path = SCRIPT_DIR + "/half_h.scpt"
        elif arg.lower() == "wu":
            path = SCRIPT_DIR + "/twice_w.scpt"
        elif arg.lower() == "wd":
            path = SCRIPT_DIR + "/half_w.scpt"
        elif arg.lower() == "std" or arg.lower() == "standard" or arg.lower() == "max" :
            path = SCRIPT_DIR + "/maxsize.scpt"
        elif arg.lower() == "min" :
            path = SCRIPT_DIR + "/minsize.scpt"
        elif arg.lower() == "full" or arg.lower() == "presentation":
                path = SCRIPT_DIR + "/fill_title.scpt"
        elif arg.lower() == "norm" or arg.lower() == "normal":
                path = SCRIPT_DIR + "/return_fill_title.scpt"

        if path != "" and os.path.exists(path) :
            self.execute(path)
        else:
            self.parser.error(util.get_err_option(self.name))
        return

    def run_tab(self):
        arg = self.args[0]
        path = ""
        if arg.lower() == "nw" or arg.lower() == "new":
            path = SCRIPT_DIR + "/tab_new.scpt"
        elif arg.lower() == "cl" or arg.lower() == "close" or arg.lower() == "rm" or arg.lower() == "remove":
            path = SCRIPT_DIR + "/tab_remove.scpt"
        elif arg.lower() == "nx" or arg.lower() == "next" or arg.lower() == "r" or arg.lower() == "right":
            path = SCRIPT_DIR + "/tab_next.scpt"
        elif arg.lower() == "bk" or arg.lower() == "back" or arg.lower() == "l" or arg.lower() == "left":
            path = SCRIPT_DIR + "/tab_back.scpt"

        if path != "" and os.path.exists(path) :
            self.execute(path)
        else:
            self.parser.error(util.get_err_option(self.name))
        return

    def run_back(self):
        path = SCRIPT_DIR + "/back.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_next(self):
        path = SCRIPT_DIR + "/next.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_reload(self):
        path = SCRIPT_DIR + "/reload.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_abort(self):
        path = SCRIPT_DIR + "/load_cancel.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_home(self):
        path = SCRIPT_DIR + "/home.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_start(self):
        path = SCRIPT_DIR + "/activate.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_restart(self):
        path = SCRIPT_DIR + "/restart.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_stop(self):
        path = SCRIPT_DIR + "/quit.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_wopen(self):
        path = SCRIPT_DIR + "/reopen.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_wclose(self):
        path = SCRIPT_DIR + "/close.scpt"
        if os.path.exists(path):
            self.execute(path)
        return

    def run_search(self):
        path = SCRIPT_DIR + "/search.scpt"
        if os.path.exists(path):
            for arg in self.args:
                path += " " + arg
            self.execute(path)
        return

    def run_url(self):
        path = SCRIPT_DIR + "/open_url.scpt"
        if os.path.exists(path):
            path += " " + self.args[0]
            self.execute(path)
        return

    def run_typo(self):
        path = SCRIPT_DIR + "/typo.scpt"
        if os.path.exists(path):
            for arg in self.args:
                path += " " + arg
            self.execute(path)
        return

    def execute(self, path):
        os.system(path + " >/dev/null 2>&1")
