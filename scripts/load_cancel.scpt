#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

if application appName is running then
    set pID to id of application "Google Chrome"
    tell application "System Events"
        set frontmost of application process appName to true
        tell application process appName
            --click menu item "中止" of menu 1 of menu bar item "表示" of menu bar 1
            key code 47 using {command down}
        end tell
    end tell
end if

delay 0.1

tell application homeApp
    activate
end tell
