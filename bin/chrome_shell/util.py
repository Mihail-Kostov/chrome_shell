import os
from chrome_shell.define import VERSION, PROG, command_dict, command_fargs, command_options

def get_option_list(name):
    msg = ""
    if command_options.has_key(name):
        if len(command_options[name]) != 0:
            msg += "["
        for i in command_options[name]:
            msg += i + "|"
        if len(command_options[name]) != 0:
            msg = msg[: -1]
            msg += "]"
    return msg



def get_message(command_name):
    msg = ""
    if command_name == "click":
        msg += "    %s " % command_name + get_option_list(command_name) + "\n"
        msg += "click on mouse cursor, single/double/triple/right." + "\n"
    elif command_name == "mouse":
        msg += "    %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move mouse cursor, upper/lower/right/left." + "\n"
    elif command_name == "wmove":
        msg += "    %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move window, upper/lower/right/left." + "\n"
    elif command_name == "scroll":
        msg += "   %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "scroll window, upper/lower/right/left." + "\n"
    elif command_name == "wsize":
        msg += "    %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "change size of window, twice-height/half-height/twice-width/half-width/standard-size/full-screen/normal-screen." + "\n"
    elif command_name == "tab":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "tab operation, new/close/next/back." + "\n"
    elif command_name == "back":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "back weg page, if exist history." + "\n"
    elif command_name == "next":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "next web page, if exist history." + "\n"
    elif command_name == "reload":
        msg += "   %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "reload web page." + "\n"
    elif command_name == "cancel":
        msg += "   %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "cancel loading web page." + "\n"
    elif command_name == "home":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move home of chrome." + "\n"
    elif command_name == "launch":
        msg += "   %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "launch chrome application." + "\n"
    elif command_name == "relaunch":
        msg += " %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "relaunch chrome application." + "\n"
    elif command_name == "quit":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "shutdown chrome application." + "\n"
    elif command_name == "open":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "open chrome window." + "\n"
    elif command_name == "close":
        msg += "    %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "close chrome window." + "\n"
    elif command_name == "search":
        msg += "   %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "search by your default search engine." + "\n"
    elif command_name == "url":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "go to url." + "\n"
    return msg


def get_usage_message():
    msg = "%prog COMMAND [OPTIONS]" + "\n"
    msg += "COMMAND:" + "\n"
    for i in command_dict:
        msg += get_message(i)
    msg = msg[: -1]
    return msg

def get_err_message(name):
    if command_fargs[name]:
        return "Command `%s` is needed option." % name
    else:
        return "Command `%s` is not needed option." % name

