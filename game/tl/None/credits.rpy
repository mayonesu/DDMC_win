define credits_ypos_tl = 415

style subtitles is normal:
    xmaximum 1000

translate None image:
    image credits_logo:
        "tl/None/gui/logo.png"
        truecenter
        zoom 0.6 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0

image subtitles:
    ypos 680
    xoffset -25
    "null.png"
    9.3
    Text("Can you hear me…?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)
    1.9
    Text("Hi, it's me.",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)
    1.7
    Text("Um... So you know how I've been like, practicing piano and stuff?",style="normal") with Dissolve( 0.5 ,alpha= True)
    4.4
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("And ? I’m not really any good at it yet…like, at all.",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.3
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("But I wrote you a song",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    2.2
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("and I was kinda hoping that I could show it to you",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    2.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("because I worked really…really hard on it.",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.2
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("So…yeah!",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    1.8
    "null.png" with Dissolve( 0.5 ,alpha= True)

image lyrics:
    ypos 680
    xoffset -25
    "null.png"
    9.5
    Text("Have I found everybody a fun assignment to do today?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("When you're here, everything that we do is fun for them anyway",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("When I can't even read my own feelings",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What good are words when a smile says it all?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("And if this world won't write me an ending",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What will it take just for me to have it all?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    19.5
    Text("Does my pen only write bitter words for those who are dear to me?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    4.0
    Text("Is it love if I take you, or is it love if I set you free?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    8.0
    Text("The ink flows down into a dark puddle",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("How can I write love into reality?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("If I can't hear the sound of your heartbeat",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    4.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("What do you call love in your reality?",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    3.5
    "null.png" with Dissolve( 0.5 ,alpha= True)
    0.5
    Text("And in your reality, if I don't know how to love you",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    5.0
    "null.png" with Dissolve( 0.5 ,alpha= True)
    3.5
    Text("I'll leave you be",style="subtitles") with Dissolve( 0.5 ,alpha= True)
    2.0
    "null.png" with Dissolve( 0.5 ,alpha= True)

translate None label:
    label credits:
        if persistent.normal_end == 0 or persistent.normal_end == 2:
            $ delete_character("sayori")
            $ delete_character("natsuki")
            $ delete_character("yuri")
        elif persistent.clearall == True:
            $ persistent.normal_end = -1
        else:
            $ delete_character("monika")
        if renpy.variant("pc"):
            $ persistent.autoload = "credits"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        if persistent.normal_end == 0 or persistent.clearall == True:
            play music "bgm/end-voice.ogg" noloop

            show subtitles zorder 100

            show noise zorder 9:
                alpha 0.0
                linear 1.5 alpha 1.0
                time 2.0
                parallel:
                    0.05
                    choice:
                        alpha 0.5
                    choice:
                        alpha 0.75
                    choice:
                        alpha 1.0
                    repeat
                parallel:
                    linear 0.375 alpha 0.7
                    linear 0.375 alpha 1.0
                time 2.75
                alpha 0.95
                time 6.45
                alpha 0.3
                time 6.95
                alpha 0.9
                time 8.65
                linear 0.8 alpha 0
                alpha 0.5
                time 22.1
                alpha 0.85
                time 22.35
                alpha 0.5
                time 28.20
                alpha 0.3
                linear 0.45 alpha 0.9
                alpha 0.4
            show vignette zorder 10:
                alpha 0.75
                parallel:
                    0.36
                    alpha 0.75
                    repeat
                parallel:
                    0.49
                    alpha 0.7
                    repeat
            show end_glitch1 zorder 2
            show black as bar zorder 9:
                alpha 0.3
                size (1280,500)
                block:
                    ypos 720
                    linear 15 ypos -500
                    repeat

            pause 41
        pause 1.5
        scene black
        pause 1.0
        $ consolehistory = []
        call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "Playing audio \"ddlc.ogg\"...")
        pause 1.0
        call hideconsole
        if persistent.normal_end == 1: 
            play music "<to 50.0>tl/None/bgm/credits.ogg" noloop
        elif persistent.normal_end == 2:
            play music "bgm/s_kill_early.ogg"
        else:
            play music "<to 50.0>bgm/credits.ogg" noloop
        $ consolehistory = []

        if _preferences.language != None:
            $ credits_ypos=90
            show expression "mcredits_1a_" + str(_preferences.language) zorder 50
            show expression "mcredits_1b_" + str(_preferences.language) zorder 49
            show expression "mcredits_1c_" + str(_preferences.language) zorder 48
            show expression "mcredits_2a_" + str(_preferences.language) zorder 47
            show expression "mcredits_2b_" + str(_preferences.language) zorder 46
            show expression "mcredits_2c_" + str(_preferences.language) zorder 45
            show expression "mcredits_3_" + str(_preferences.language) zorder 44
            show expression "mcredits_4_" + str(_preferences.language) zorder 43
            show expression "mcredits_5_" + str(_preferences.language) zorder 42
            show expression "mcredits_6a_" + str(_preferences.language) zorder 41
            show expression "mcredits_6b_" + str(_preferences.language) zorder 40

        show mcredits_1a zorder 50
        show mcredits_1b zorder 49
        show mcredits_1c zorder 48
        show mcredits_2a zorder 47
        show mcredits_2b zorder 46
        show mcredits_2c zorder 45
        show mcredits_3 zorder 44
        show mcredits_4 zorder 43
        show mcredits_5 zorder 42
        show mcredits_6a zorder 41
        show mcredits_6b zorder 40
        show mcredits_7 zorder 51
        call hideconsole
        $ consolehistory = []

        if _preferences.language != None:
            show expression "mcredits_1a_" + str(_preferences.language) zorder 50
            show expression "mcredits_1b_" + str(_preferences.language) zorder 49
            show expression "mcredits_1c_" + str(_preferences.language) zorder 48
            show expression "mcredits_2a_" + str(_preferences.language) zorder 47
            show expression "mcredits_2b_" + str(_preferences.language) zorder 46
            show expression "mcredits_2c_" + str(_preferences.language) zorder 45
            show expression "mcredits_3_" + str(_preferences.language) zorder 44
            show expression "mcredits_4_" + str(_preferences.language) zorder 43
            show expression "mcredits_5_" + str(_preferences.language) zorder 42
            show expression "mcredits_6a_" + str(_preferences.language) zorder 41
            show expression "mcredits_6b_" + str(_preferences.language) zorder 40

        pause 50
        jump credits2

    label credits2:
        python:
            sayoriTime = renpy.random.random() * 4 + 4
            natsukiTime = renpy.random.random() * 4 + 4
            yuriTime = renpy.random.random() * 4 + 4
            monikaTime = renpy.random.random() * 4 + 4
            sayoriPos = 0
            natsukiPos = 0
            yuriPos = 0
            monikaPos = 0
            sayoriOffset = 0
            natsukiOffset = 0
            yuriOffset = 0
            monikaOffset = 0
            sayoriZoom = 1
            natsukiZoom = 1
            yuriZoom = 1
            monikaZoom = 1
            imagenum = 0
        scene black
        $ consolehistory = []
        if persistent.normal_end == 1: 
            play music "<from 50.0>tl/None/bgm/credits.ogg" noloop
        elif persistent.normal_end == 2:
            $ persistent.normal_end = 2
        else:
            play music "<from 50.0>bgm/credits.ogg" noloop
        $ starttime = datetime.datetime.now()
        pause 0.88
        show credits_logo
        if persistent.normal_end == 0 or persistent.clearall == True:
            show lyrics zorder 100
            if _preferences.language != None:
                show expression "lyrics_" + str(_preferences.language) zorder 101
        if persistent.clearall == True:
            $ persistent.normal_end = 1
        pause 9.12
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
        show credits_header "Concept & Game Design" as credits_header_1 at credits_text_scroll_left
        show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png deleted successfully.")
        show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
        show credits_header "Character Art" as credits_header_2 at credits_text_scroll_right
        show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png deleted successfully.")
        show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
        show credits_header "Background Art" as credits_header_1 at credits_text_scroll_left
        show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png deleted successfully.")
        show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
        show credits_header "Writing" as credits_header_2 at credits_text_scroll_right
        show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png deleted successfully.")
        show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
        show credits_header "Music" as credits_header_1 at credits_text_scroll_left
        show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png deleted successfully.")
        show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
        show credits_header "Vocals" as credits_header_2 at credits_text_scroll_right
        show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png deleted successfully.")
        show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
        show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
        show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_left
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png deleted successfully.")
        show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
        show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
        show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_right
        if persistent.normal_end == 0 or persistent.clearall == True:
            show s_sticker at credits_sticker_1
            show n_sticker at credits_sticker_2
            show y_sticker at credits_sticker_3
            show m_sticker at credits_sticker_4
        elif persistent.normal_end == 1:
            show s_sticker at credits_sticker_1
            show n_sticker at credits_sticker_2
            show y_sticker at credits_sticker_3
        else:
            $ persistent.normal_end = 2
        $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.normal_end == 1 or persistent.clearall == True: lockedtext = "_clearall"
        $ imagenum += 1
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png deleted successfully.")
        $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
        show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
        show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
        show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_left
        $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
        $ if persistent.clearall: lockedtext = "_clearall"
        $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.normal_end != 1:
            call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png deleted successfully.")
        show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
        show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
        show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_right
        $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
        if persistent.clearall == True:
            $ persistent.normal_end = 3
        if persistent.normal_end < 3:
            call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")
        else:
            call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png deleted successfully.")

        call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
        call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
        if persistent.normal_end == 0 and persistent.clearall == False:
            call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
            $ delete_character("monika")
        $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
        call hideconsole
        show credits_ts
        show credits_text "made with love by":
            zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
            linear 2.0 alpha 1
            4.5
            linear 2.0 alpha 0
        pause 9.3
        play sound page_turn
        if persistent.normal_end == 1:
            if _preferences.language == None:
                show image "bg/poem_normalE.jpg" with Dissolve(1)
            else:
                show image "tl/Japanese/bg/poem_normalJ.jpg" with Dissolve(1)
        elif persistent.normal_end == 2:
            stop music fadeout 1.0
            show image "bg/poem_null.jpg"
            with Dissolve(1)

        else:
            show poem_end with Dissolve(1)
        if persistent.clearall:
            python:
                try: renpy.file(config.basedir + "/DDMC_Thanks.pdf")
                except: open(config.basedir + "/DDMC_Thanks.pdf", "wb").write(renpy.file("DDMC_Thanks.pdf").read())
        if ddmm_online:
            python hide:
                for i in range(0,16):
                    if i == 0:
                         f = open(renpy.config.gamedir + "/chapter", "w")
                    else:
                        f = open(renpy.config.gamedir + "/chapter", "a")
                    if persistent.chapter_seen[i]:
                        f.write("1")
                    else:
                        f.write("0")
                    f.close()
        label postcredits_loop:
            if renpy.variant("pc"):
                $ persistent.autoload = "postcredits_loop"
            $ config.keymap['game_menu'] = []
            $ config.keymap['hide_windows'] = []
            $ renpy.display.behavior.clear_keymap_cache()
            $ quick_menu = False
            $ config.skipping = False
            $ config.allow_skipping = False
            if persistent.normal_end == 0 or persistent.normal_end == 2:
                $ delete_character("sayori")
                $ delete_character("natsuki")
                $ delete_character("yuri")
                $ delete_character("monika")
            elif persistent.clearall == True:
                $ persistent.normal_end = -1
            else:
                $ delete_character("monika")
            scene black
            if persistent.normal_end == 1:
                if _preferences.language == None:
                    show image "bg/poem_normalE.jpg"
                else:
                    show image "tl/Japanese/bg/poem_normalJ.jpg"
            elif persistent.normal_end == 2:
                show image "bg/poem_null.jpg"
            else:
                show poem_end
            $ pause()
            if persistent.normal_end == 2:
                call screen dialog(message="null", ok_action=Quit(confirm=False))

            elif persistent.clearall == True:
                call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.\nAdded DDMC_Thanks.pdf in the game folder.", ok_action=Quit(confirm=False))

            else:
                call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
