# crome_shell

batting open/close command.

need to modify help message, add activate command.

## Usage: chrome_shell COMMAND [OPTIONS]
###COMMAND

    click [c|dc|tc|rc]

click on mouse cursor, single/double/triple/right.

    mouse [u|d|r|l]

move mouse cursor, upper/lower/right/left.

    wmove [u|d|r|l]

move window, upper/lower/right/left.

    scroll [u|d|r|l]

scroll window, upper/lower/right/left.

    wsize [hu|hd|wu|wd|std|full|norm]

change size of window, twice-height/half-height/twice-width/half-width/standard-size/full-screen/normal-screen.

    tab [nw|cl|nx|bk]

tab operation, new/close/next/back.

    back

back weg page, if exist history.

    next

next web page, if exist history.

    reload

reload web page.

    cancel

cancel loading web page.

    home

move home of chrome.

    launch

launch chrome application.

    relaunch

relaunch chrome application.

    quit

shutdown chrome application.

    open

open chrome window.

    close

close chrome window.

    search [search_keyword]

search by your default search engine.

    url [url]

go to url

###Options:

    --version   show program's version number and exit
    -h, --help  Show help
