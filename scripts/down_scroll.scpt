#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

if application appName is running then
    set pID to id of application appName
    tell application "System Events"
        set frontmost of application process appName to true
        tell application process appName
            key code 121
        end tell

    end tell
end if
tell application homeApp
    activate
end tell
