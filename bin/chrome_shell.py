#!/usr/bin/env python
import os
import sys
from optparse import OptionParser
import chrome_shell.command as cmd
import chrome_shell.define as define

BIN_DIR = os.path.dirname(__file__)
SCRIPT_DIR = BIN_DIR + "/../scripts"

parser = OptionParser(usage=define.get_usage_message(),
    prog=define.PROG, version=define.VERSION, add_help_option=False)
parser.add_option("-h", "--help", dest="help",
    action="store_true", help="Show help")
parser.disable_interspersed_args()


def main():
    options, args = parser.parse_args(sys.argv[1:])
    if options.help and not args:
        args = ["help"]
    if not args:
        args = ["help"]
    command_name = args[0].lower()
    if command_name not in define.command_dict:
        if command_name == "help":
            parser.print_help()
        else:
            parser.error("Unknown command: `%s`" % command_name)
        return
    command = cmd.Command(command_name, args[1:])
    command.run()

if __name__ == "__main__":
    main()
