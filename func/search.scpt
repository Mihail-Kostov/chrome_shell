#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

set word_txt to "のんのんびより"
set the clipboard to word_txt
delay 0.5

tell application "System Events"
    set homeApp to name of (path to frontmost application)
end tell

if application appName is running then
    set pID to id of application "Google Chrome"
    tell application "System Events"
        set frontmost of application process appName to true
        tell application process appName
            click menu item "新しいタブ" of menu 1 of menu bar item "ファイル" of menu bar 1
        end tell

        delay 0.5
        tell application process appName
            key down {option}
            key down {command}
            key code 3
            key up {command}
            key up {option}

            delay 0.05
            keystroke "v" using {command down}

        end tell

    end tell
end if
tell application homeApp
    activate
end tell
