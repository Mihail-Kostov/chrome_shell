#!/usr/bin/osascript
on run argv
    set appName to "Google Chrome"
    set HomeURL to "https://www.google.co.jp"

    --set word_txt to "のんのんびより"
    --set word_txt to item 1 of argv
    set word_txt to ""
    repeat with char_i in argv
        set word_txt to word_txt & char_i & "\\ "
    end repeat

    tell application "System Events"
        set homeApp to name of (path to frontmost application)
    end tell

    if application appName is running then
        set pID to id of application "Google Chrome"
        tell application "System Events"
            set frontmost of application process appName to true
            --tell application process appName
                --click menu item "新しいタブ" of menu 1 of menu bar item "ファイル" of menu bar 1
            --end tell

            delay 0.5
            tell application process appName
                key down {option}
                key down {command}
                key code 3
                key up {command}
                key up {option}

                do shell script "./paste " & word_txt

                delay 0.05
                keystroke "v" using {command down}
                delay 0.1
                key code 76

            end tell

        end tell
    end if
    tell application homeApp
        activate
    end tell
end run
