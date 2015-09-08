#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    tell application appName
        activate
        open location HomeURL
    end tell
end if
