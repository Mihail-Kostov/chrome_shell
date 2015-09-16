#!/usr/bin/osascript
on run argv
    set x to item 1 of argv
    set y to item 2 of argv
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

