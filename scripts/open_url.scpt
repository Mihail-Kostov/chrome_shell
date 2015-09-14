#!/usr/bin/osascript
on run argv
    set appName to "Google Chrome"
    set url_option to item 1 of argv

    tell application "System Events"
        set homeApp to name of (path to frontmost application)
    end tell

    if application appName is running then
        tell application appName
            activate
            open location url_option
        end tell
        repeat while application appName is not running
            delay 0.1
        end repeat
    end if
    delay 0.15

    tell application homeApp
        activate
    end tell
end run

