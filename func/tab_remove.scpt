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
            click menu item "タブを閉じる" of menu 1 of menu bar item "ファイル" of menu bar 1
        end tell
    end tell
end if

tell application homeApp
    activate
end tell
