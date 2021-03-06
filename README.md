# chrome_shell

This trminal command operate google chrome app on Mac OS X.

This command is tested on OSX 10.9.5, zsh 5.0.2 and bash 3.2.53 .

##Instllation

The recommended way to download and install chrome_shell is to execute theses statements in your shell:

    git clone https://github.com/kota999/shell-chrome.git

Please add the following line to the end of your ~/.bashrc:

    [[ -s <YOUR_CLONE_DIR>/etc/bashrc ]] && source <YOUR_CLONE_DIR>/etc/bashrc

##Demo

![Output sample](https://github.com/kota999/chrome_shell/raw/master/short_demo_chrome_mode.gif)

###Full size demo
demo.mp4 is full size demo, and demo_chrome_mode.mp4 is full size Chrome mode demo.

##Simple Usage

activate chrome mode.

    chrome activate

deactivate chrome mode.

    deactivate

operate chrome window.

    wopen                      # open chrome window
    wclose                     # close chrome window
    tab [new|rm|next|back]     # tab operation
    search <keyword>           # web search
    click [c|dc|tc|rc|ctn]     # single/double/triple/right click, click new tab
    back                       # move before web page
    next                   # move next web page

control mouse on chrome mode.

ESC+→ or ESC+← or ESC+↑ or ESC+↓  : move mouse and activate mouse control mode.<br>
→ or ← or ↑ or ↓                  : move mouse on mouse control mode. <br>
if you deactivate mouse control mode, you type any key.

##Usage: chrome_shell SUBCOMMAND [OPTIONS]

###Sub command:

    activate

activate chrome mode. `chrome_shell` command can be ommited in this mode.

    deactivate

deactivate chrome mode. in chrome mode, this command can be used.

    click [c|dc|tc|rc|ctn]

click on mouse cursor, single/double/triple/right/tab-new.

    mouse [u|d|r|l]

move mouse cursor, upper/lower/right/left.

    wmove [r|l]

move window, right/left.

    scroll [u|d|r|l]

scroll window, upper/lower/right/left.

    wsize [hu|hd|wu|wd|min|max|full|norm]

change size of window, twice-height/half-height/twice-width/half-width/min-size/max-size/full-screen/normal-screen.

    tab [nw|cl|nx|bk]

tab operation, new/close/next/back.

    back

back weg page, if exist history.

    next

next web page, if exist history.

    reload

reload web page.

    abort

cancel loading web page.

    home

move home of chrome.

    start

launch chrome application.

    restart

relaunch chrome application.

    stop

shutdown chrome application.

    wopen

open chrome window.

    wclose

close chrome window.

    search [search_keyword]

search by your default search engine.

    url [url]

go to url.

    typo [keyword]

input keyword to web form.

###Options:

    --version
show program's version number and exit

    -h, --help
Show help
