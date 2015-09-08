#!/usr/bin/osascript
set appName to "Google Chrome"
set HomeURL to "https://www.google.co.jp"

if application appName is running then
    tell application appName to close window 1
end if
