#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

if application appName is running then
    tell application appName
        activate
        reopen
    end tell
end if

tell application homeApp
    activate
end tell
