#!/usr/bin/osascript
on run argv
    set x to item 1 of argv
    --set y to item 2 of argv
    if x = "r" then
        set x to "+20"
        set y to "+0"
    else if x = "l" then
        set x to "-20"
        set y to "+0"
    else if x = "u" then
        set x to "+0"
        set y to "-20"
    else if x = "d" then
        set x to "+0"
        set y to "+20"
    end if
    move_mouse(x, y)
end run

on move_mouse(x, y)
    --do shell script "/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby -e \"require 'osx/cocoa'\" -e \"OSX::CGWarpMouseCursorPosition(OSX::CGPointMake(" & x & "," & y & "))\""
    do shell script "./cliclick m:" & x & "," & y
end move_mouse
