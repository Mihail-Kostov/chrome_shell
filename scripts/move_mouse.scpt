#!/usr/bin/osascript
on run argv
    set x to item 1 of argv
    if x = "r" then
        set x to "+20"
        set y to "+0"
    else if x = "l" then
        set x to "-20"
        set y to "+0"
    else if x = "u" then
        set x to "+0"
        set y to "-20"
    else if x = "d" then
        set x to "+0"
        set y to "+20"
    else if x = "r2" then
        set x to "+50"
        set y to "+0"
    else if x = "l2" then
        set x to "-50"
        set y to "+0"
    else if x = "u2" then
        set x to "+0"
        set y to "-50"
    else if x = "d2" then
        set x to "+0"
        set y to "+50"
    end if
    move_mouse(x, y)
end run

on move_mouse(x, y)
    tell application "Finder"
        set thisFolder to parent of (path to me) as text
    end tell
    set thisFolder to replaceText(thisFolder, ":", "/")
    set thisFolder to replaceText(thisFolder, "Macintosh HD", "")

    do shell script thisFolder & "cliclick m:" & x & "," & y
end move_mouse

on replaceText(theText, serchStr, replaceStr)
    set tmp to AppleScript's text item delimiters
    set AppleScript's text item delimiters to serchStr
    set theList to every text item of theText
    set AppleScript's text item delimiters to replaceStr
    set theText to theList as string
    set AppleScript's text item delimiters to tmp
    return theText
end replaceText

