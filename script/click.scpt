#!/usr/bin/osascript
on run argv
    set x to item 1 of argv
    if (x = "c") or (x = "dc") or (x = "tc") then
        click(x)
    else if x = "rc" then
        set x to "c"
        right_click(x)
    end if
end run

on click(x)
    do shell script "./cliclick " & x & ":+0,+0"
end click

on right_click(x)
    tell application "System Events"
        key down control
        do shell script "./cliclick " & x & ":+0,+0"
        key up control
    end tell
end right_click
