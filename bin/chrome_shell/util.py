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
        msg += "      %s " % command_name + get_option_list(command_name) + "\n"
        msg += "click on mouse cursor, single/double/triple/right." + "\n"
    elif command_name == "mouse":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move mouse cursor, upper/lower/right/left." + "\n"
    elif command_name == "wmove":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move window, right/left." + "\n"
    elif command_name == "scroll":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "scroll window, upper/lower/right/left." + "\n"
    elif command_name == "wsize":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "change size of window, twice-height/half-height/twice-width/half-width/min-size/max-size/full-screen/normal-screen." + "\n"
    elif command_name == "tab":
        msg += "        %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "tab operation, new/close/next/back." + "\n"
    elif command_name == "back":
        msg += "       %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "back weg page, if exist history." + "\n"
    elif command_name == "next":
        msg += "       %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "next web page, if exist history." + "\n"
    elif command_name == "reload":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "reload web page." + "\n"
    elif command_name == "abort":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "cancel loading web page." + "\n"
    elif command_name == "home":
        msg += "       %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "move home of chrome." + "\n"
    elif command_name == "start":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "launch chrome application." + "\n"
    elif command_name == "restart":
        msg += "    %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "relaunch chrome application." + "\n"
    elif command_name == "stop":
        msg += "       %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "shutdown chrome application." + "\n"
    elif command_name == "wopen":
        msg += "      %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "open chrome window." + "\n"
    elif command_name == "wclose":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "close chrome window." + "\n"
    elif command_name == "search":
        msg += "     %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "search by your default search engine." + "\n"
    elif command_name == "url":
        msg += "        %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "go to url." + "\n"
    elif command_name == "typo":
        msg += "       %s "  % command_name + get_option_list(command_name) + "\n"
        msg += "input keyword to web form." + "\n"
    return msg


def get_usage_message():
    msg = "%prog SUBCOMMAND [OPTIONS]" + "\n"
    msg += "SUBCOMMAND:" + "\n"
    msg += "   activate " + "\n" + "activate chrome mode. `chrome_shell` command can be ommited in this mode." + "\n"
    msg += " deactivate " + "\n" + "deactivate chrome mode. in chrome mode, this command can be used. " + "\n"
    for i in command_dict:
        msg += get_message(i)
    msg = msg[: -1]
    return msg

def get_err_message(name):
    if command_fargs[name]:
        return "Command `%s` is needed option." % name
    else:
        return "Command `%s` is not needed option." % name

def get_err_option(name):
    return "Command `%s` option is `%s`" %(name, get_option_list(name))
