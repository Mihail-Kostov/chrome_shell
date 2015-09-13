#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    set pID to id of application appName
    tell application "System Events"
        set homeApp to name of (path to frontmost application)
        set frontmost of application process appName to true
        tell application process appName
            set topWindow to window 1
            set topWindowSize to size of topWindow
            set topWindowPos to position of topWindow
            set posX to (item 1 of topWindowPos)
            set posY to (item 2 of topWindowPos)
            set w to (item 1 of topWindowSize)
            set h to (item 2 of topWindowSize) / 2
            tell topWindow
                set size to {w, h}
            end tell
        end tell

    end tell
end if
tell application homeApp
    activate
end tell
