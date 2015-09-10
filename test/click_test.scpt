-------設定項目　この回数だけクリックします
set theLimitTime to 60 as number

------おまじない
tell application "System Events"
    launch
    activate
end tell
--------この秒数の間にマウスをクリックしたい場所に移動します
delay 10
------------クリック回数カウント初期化
set theRepeatCnt to 0 as number

---------------★このスクリプトサンプルはChromiumです
tell application "Google Chrome"
    activate
    tell window 1
        tell active tab
            ----------繰り返しの始まり
            repeat while theRepeatCnt < theLimitTime
                ------------システムイベント
                tell application "System Events"
                    delay 1
                    ------------Chromiumのプロセスに対して実行します
                    tell process "Google Chrome"
                        ------------マウスキーのクリックにあたる5を実行
                        keystroke "5"
                        ----------click at {896, 157}
                    end tell
                    --------設定したリミットを超えたらリピートを抜ける
                    if theRepeatCnt = theLimitTime then exit repeat

                    ---------クリックした分カウントアップ
                    set theRepeatCnt to theRepeatCnt + 1
                    -------画面でカウント数見えるようにログする
                    log theRepeatCnt
                    ---------ここのディレイ値はお好みで
                    delay 5
                end tell
            end repeat
            -----------リピートの終了
        end tell
    end tell
end tell
--http://force4u.cocolog-nifty.com/skywalker/2013/07/system-eventsap.html
