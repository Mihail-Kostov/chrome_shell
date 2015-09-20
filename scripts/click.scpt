#!/usr/bin/osascript


on run argv
    tell application "System Events"
        set homeApp to name of (path to frontmost application)
    end tell

    set x to item 1 of argv
    if (x = "c") or (x = "dc") or (x = "tc") then
        click(x)
    else if x = "rc" then
        set x to "c"
        right_click(x)
    else if x = "ctn" then
        set x to "c"
        click_tab_new(x)
    end if

    delay 0.2

    tell application homeApp
        activate
    end tell
end run

on click(x)
    tell application "Finder"
        set thisFolder to parent of (path to me) as text
    end tell
    set thisFolder to replaceText(thisFolder, ":", "/")
    set thisFolder to replaceText(thisFolder, "Macintosh HD", "")

    do shell script thisFolder & "cliclick " & x & ":+0,+0"
end click

on right_click(x)
    tell application "Finder"
        set thisFolder to parent of (path to me) as text
    end tell
    set thisFolder to replaceText(thisFolder, ":", "/")
    set thisFolder to replaceText(thisFolder, "Macintosh HD", "")

    tell application "System Events"
        key down control
        do shell script thisFolder  & "cliclick " & x & ":+0,+0"
        key up control
    end tell
end right_click

on click_tab_new(x)
    tell application "Finder"
        set thisFolder to parent of (path to me) as text
    end tell
    set thisFolder to replaceText(thisFolder, ":", "/")
    set thisFolder to replaceText(thisFolder, "Macintosh HD", "")

    tell application "System Events"
        key down command
        key down shift
        do shell script thisFolder  & "cliclick " & x & ":+0,+0"
        do shell script thisFolder  & "cliclick " & x & ":+0,+0"
        key up command
        key up shift
    end tell
end click_tab_new

on replaceText(theText, serchStr, replaceStr)
    set tmp to AppleScript's text item delimiters
    set AppleScript's text item delimiters to serchStr
    set theList to every text item of theText
    set AppleScript's text item delimiters to replaceStr
    set theText to theList as string
    set AppleScript's text item delimiters to tmp
    return theText
end replaceText

