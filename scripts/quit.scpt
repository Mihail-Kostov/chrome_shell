#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

tell application appName
    quit
    repeat while application appName is running
        delay 0.05
    end repeat
end tell

tell application homeApp
    activate
end tell
