#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    set pID to id of application "Google Chrome"
    tell application "System Events"
        tell (process 1 whose bundle identifier is pID)
            set b1List to every button of window 1 whose subrole is "AXZoomButton"
            set targB to first item of b1List
            click targB
        end tell
    end tell
end if
