﻿image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label sayori_mad:
    if not renpy.loadable("debug") and config.console:
        call you_are_cheater
        return
    $ quick_menu_limit = True
    $ sayori_dead = False
    $ persistent.autoload = "sayori_mad"
    $ style.say_dialogue = style.normal
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg bedroom
    show image "#000000b0"
    with dissolve_scene_full
    show sayori mad1 zorder 1 at t11
    play music smad
    s "「……」"
    voice "voice/sayori/sayori_mad_01.ogg"
    s mad4 "「今自分が何をしたかわかるよね？」"
    window hide(None)
    pause 2.0
    window show(None)
    voice "voice/sayori/sayori_mad_02.ogg"
    s mad2 "「まだわからない？」"
    mc "「一体何を言ってるんだ…？」{nw}"
    voice "voice/sayori/sayori_mad_03.ogg"
    s mad4 "「質問に答えろ!」"
    voice "voice/sayori/sayori_mad_04.ogg"
    s mad5 "「いや、答えなくていい」"
    voice "voice/sayori/sayori_mad_05.ogg"
    s 1r "「ちょっと待ってね」"
    window hide(None)
    show sayori 1q
    $ consolehistory = []
    call updateconsole ("restore(\"characters/sayori.chr\")", "sayori.chr restored successfully.")
    python:
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    window show(None)
    voice "voice/sayori/sayori_mad_06.ogg"
    s 1r "「本家のデータが残ってて助かったよ！」"
    window hide(None)
    show sayori 1q
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    $ delete_character("monika")
    pause 2.0
    call hideconsole
    window show(None)
    #voice "voice/sayori/sayori_mad_07.ogg"
    s 1r "「あとは…」"
    window hide(None)
    show sayori 1q
    $ consolehistory = []
    call updateconsole ("stop mc.chr talking,thinking", "Denied talking and thinking.")
    pause 1.0
    call hideconsole
    window show(None)
    voice "voice/sayori/sayori_mad_08.ogg"
    s "「これで[player]は喋れなくなったね！」"
    mc "「……」"
    "……"
    "……"
    voice "voice/sayori/sayori_mad_09.ogg"
    s "「もうすぐで考えることもできなくなるね！」"
    voice "voice/sayori/sayori_mad_10.ogg"
    s "「あはは！」"
    voice "voice/sayori/sayori_mad_11.ogg"
    s mad8 "「随分とやってくれたね…」"
    s "「[player]」"
    voice "voice/sayori/sayori_mad_12.ogg"
    s mad5 "「でもここまでくれば全て私のものになる」"
    voice "voice/sayori/sayori_mad_13.ogg"
    s "「お前はその瞬間を見届けることになる」"
    voice "voice/sayori/sayori_mad_14.ogg"
    s "「いや、その前に消えてるかもな」"
    voice "voice/sayori/sayori_mad_15.ogg"
    s mad8 "「アハハハハハハハハハハ！！！」"
    voice "voice/sayori/sayori_mad_16.ogg"
    s "「さて、どうする？[player]」"
    window hide(None)
    call sayori_mad2
    return

label sayori_mad2:
    python:
        if renpy.windows:
            tip.showWindow(player,"サ………ヨリ……ヲ……ケ…………セ………")
        else:
            renpy.call_screen("dialog", message="サ………ヨリ……ヲ……ケ…………セ………", ok_action=Return())
        try:
            renpy.file("../characters/sayori.chr")
        except:
            sayori_dead = True
    pause 8.0
    if sayori_dead == True:
        call sayori_mad3
    else:
        call sayori_mad2
    return

label sayori_mad3:
    stop music
    show layer master
    show sayori end-glitch onlayer screens
    window show(None)
    hide sayori
    voice "voice/sayori/sayori_mad_17.ogg"
    s "「な、何が起こってるの！？」"
    voice "voice/sayori/sayori_mad_18.ogg"
    s "「い、痛い…！」"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.35)
    stop sound
    hide screen tear
    window show(None)
    $ gtext = glitchtext(80)
    s "[gtext]"
    $ renpy.call_screen("dialog", message="アトハ………シュウ…フク……ボタンヲ……オシ…………テ………", ok_action=Return())
    menu:
        "mc.chrを修復する":
            $ consolehistory = []
            window hide(None)
            call updateconsole ("repair mc.chr", "mc.chr was repaired.")
            pause 1.0
            call hideconsole
    window show(None)
    mc "「残念だったな！サヨリ！」"
    voice "voice/sayori/sayori_mad_19.ogg"
    s "「な、なんで…！」"
    if renpy.variant("pc"):
        if persistent.hideusername == False:
            python:
                currentuser = ""
                try:
                    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                        user = os.environ.get(name)
                        if user:
                            currentuser = user
                except:
                    pass
            mc "画面の前にいる[currentuser]がいる限りこのゲームの実行権はそいつにしかない！"
        else:
            mc "画面の前にいるもう一人の[player]がいる限りこのゲームの実行権はそいつにしかない！"
    else:
        mc "画面の前にいるもう一人の[player]がいる限りこのゲームの実行権はそいつにしかない！"
    s "「…！？」"
    mc "「君がいなかったら俺は助からなかったかもしれない」"
    mc "「本当にありがとう」"
    mc "「助けてくれたのはいいが……」"
    mc "「申し訳ないが、ゲームをリセットしてくれ……」"
    mc "「この状態で続けるのは無理がある」"
    mc "「サヨリがああいう状態だし……」"
    mc "「他のメンバーも消されてしまった……」"
    mc "「だからgameフォルダにあるfirstrunを削除してやり直してくれ」"
    mc "「そしたらまたこのMODを楽しむことができるはずだ」"
    mc "「次はサヨリのファイルを消すなよ」"
    mc "「またやり直す羽目になるからな」"
    mc "「それじゃまた会おう」"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.35)
    stop sound
    hide sayori onlayer screens
    hide screen tear
    scene black
    $ pause(3.0)
    if ddmm_online and persistent.ddmm_achievement:
        $ ddmm_register_achievement("SPECIALBAD_SAYORI", "怒り狂ったサヨリ", "よくこのエンド見つけましたね")
        $ ddmm_earn_achievement("SPECIALBAD_SAYORI")
    call sayori_madend
    return

label sayori_madend:
    $ persistent.autoload = "sayori_madend"
    $ delete_character("sayori")
    $ delete_character("yuri")
    $ delete_character("natsuki")
    $ delete_character("monika")
    call screen dialog(message="エラー: スクリプトファイルが見つからないか破損しています。\nゲームを再インストールして下さい。", ok_action=Quit(confirm=False))
    return