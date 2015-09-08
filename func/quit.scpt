#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    tell application appName to quit
    repeat while application appName is running
        delay 0.1
    end repeat
end if
