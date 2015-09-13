#!/usr/bin/osascript
set appName to "Google Chrome"

if application appName is running then
    my fill_title()
end if

on fill_title()
    tell application "Google Chrome"
        tell window 1
            enter presentation mode
        end tell
    end tell
end fill_title
