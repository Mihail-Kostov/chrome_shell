#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    set pID to id of application "Google Chrome"
    tell application "System Events"
        set frontmost of application process appName to true
        tell application process appName
            click menu item "新しいタブ" of menu 1 of menu bar item "ファイル" of menu bar 1
        end tell
    end tell
end if
