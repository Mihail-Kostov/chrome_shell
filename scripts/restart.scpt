#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

if application appName is running then
    tell application appName to quit
    repeat while application appName is running
        delay 0.1
    end repeat

    tell application appName
        activate
    end tell
    repeat while application appName is not running
        delay 0.1
    end repeat
end if
delay 0.3

tell application homeApp
    activate
end tell
