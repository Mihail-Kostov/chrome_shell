import os

VERSION = "0.1"
PROG = "chrome_shell"
SRC_DIR = os.path.dirname(__file__)
SCRIPT_DIR = SRC_DIR + "/../../scripts"

command_dict = ["click", "mouse", "wmove", "scroll", "wsize",
    "tab", "back", "next", "reload", "abort", "home", "start",
    "restart", "stop", "wopen", "wclose", "search", "url", "typo"]
command_fargs = {"click": True, "mouse": True, "wmove": True,
    "scroll": True, "wsize": True, "tab": True, "back": False,
    "next": False, "reload": False, "abort": False, "home": False,
    "start": False, "restart": False, "stop": False, "wopen": False,
    "wclose": False, "search": True, "url": True, "typo": True}
command_options = {"click": ["c", "dc", "tc", "rc"],
    "mouse": ["u", "d", "r", "l"], "wmove": ["r", "l"],
    "scroll": ["u", "d", "r", "l"],
    "wsize": ["hu", "hd", "wu", "wd", "min", "max", "full", "norm"],
    "tab": ["nw", "cl", "nx", "bk"],
    "back": [], "next": [], "reload": [], "abort": [], "home": [],
    "start": [], "restart": [], "stop": [], "wopen": [], "wclose": [],
    "search": ["search_keyword"], "url": ["url"], "typo": ["keyword"]}

