#!/usr/bin/osascript
on run argv
    set appName to "Google Chrome"

    set word_txt to ""
    repeat with char_i in argv
        set word_txt to word_txt & char_i & "\\ "
    end repeat

    tell application "Finder"
        set thisFolder to parent of (path to me) as text
    end tell
    set thisFolder to replaceText(thisFolder, ":", "/")
    set thisFolder to replaceText(thisFolder, "Macintosh HD", "")

    tell application "System Events"
        set homeApp to name of (path to frontmost application)
    end tell

    if application appName is running then
        set pID to id of application "Google Chrome"
        tell application "System Events"
            set frontmost of application process appName to true

            delay 0.5
            tell application process appName

                do shell script thisFolder & "paste " & word_txt

                delay 0.05
                keystroke "v" using {command down}
                delay 0.1
                key code 76

            end tell

        end tell
    end if

    tell application homeApp
        activate
    end tell
end run

on replaceText(theText, serchStr, replaceStr)
    set tmp to AppleScript's text item delimiters
    set AppleScript's text item delimiters to serchStr
    set theList to every text item of theText
    set AppleScript's text item delimiters to replaceStr
    set theText to theList as string
    set AppleScript's text item delimiters to tmp
    return theText
end replaceText

