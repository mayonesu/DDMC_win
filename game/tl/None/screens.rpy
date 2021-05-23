define config.default_language = "Japanese"

define readme_file = ""

init -2 python:
    def SaveName():
        import codecs
        try:
            with codecs.open(config.gamedir + "/name", "w", "utf-8") as f:
                f.write(player)
                f.close()
        except:
            pass
        if persistent.new_name:
            renpy.notify("Saved your name as file \"name\".You can load your name from the file after you reset the game.")

init -1 python:
    def FinishEnterName3():
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        if persistent.save_name == True:
            persistent.new_name = True
            SaveName()
        if persistent.monikabirth:
            renpy.jump_out_of_context("monika_birthday")
        else:
            renpy.jump_out_of_context("start")

    def DeleteNameFile():
        import os
        try: os.unlink(config.gamedir + "/name")
        except: pass

    def ddmm_default_achievement():
        ddmm_register_achievement("BAD_SAYORI", achievement_name_1, achievement_message_1)
        ddmm_register_achievement("BAD_YURI", achievement_name_2, achievement_message_2)
        ddmm_register_achievement("BAD_NATSUKI", achievement_name_3, achievement_message_3)
        ddmm_register_achievement("BAD_MONIKA", achievement_name_4, achievement_message_4)
        ddmm_register_achievement("WITHOUT_MONIKA", achievement_name_5, achievement_message_5)
        ddmm_register_achievement("NO_ONE", achievement_name_6, achievement_message_6)
        ddmm_register_achievement("THE_TRUTH", achievement_name_7, achievement_message_7)

    def change_button_layout():
        if persistent.gamepad:
            if persistent.change_buttons:
                config.pad_bindings["pad_a_press"] = [ "button_alternate", "history", "bar_deactivate" ]
                config.pad_bindings["pad_b_press"] = [ "dismiss", "button_select", "bar_activate", "bar_deactivate"]
                config.pad_bindings["pad_x_press"] = [ "hide_windows" ]
                config.pad_bindings["pad_y_press"] = [ "toggle_skip" ]
            else:
                config.pad_bindings["pad_a_press"] = [ "dismiss", "button_select", "bar_activate", "bar_deactivate"]
                config.pad_bindings["pad_b_press"] = [ "button_alternate", "history", "bar_deactivate" ]
                config.pad_bindings["pad_x_press"] = [ "toggle_skip" ]
                config.pad_bindings["pad_y_press"] = [ "hide_windows" ]

    def reset_volume():
        _preferences.volumes['music'] = 0.70
        _preferences.volumes['sfx'] = 0.70
        _preferences.volumes['voice'] = 1.00
    
    def reset_text_settings():
        _preferences.text_cps = 50
        _preferences.afm_time = 15

    def open_readme_url():
        import webbrowser
        if _preferences.language == None:
            webbrowser.open("https://ddlc-jp.tokyo/readme_document/README.html")
        else:
            webbrowser.open("https://ddlc-jp.tokyo/readme_document/README_jp.html")


label Set_chapter(chapter = ddmc_chapter):
    if chapter == 1:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter1")
    elif chapter == 2:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter2")
    elif chapter == 3:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter3")
    elif chapter == 4:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter4")
    elif chapter == 5:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter5")
    elif chapter == 6:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter6")
    elif chapter == 7:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter7")
    elif chapter == 8:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter8")
    elif chapter == 9:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter9")
    elif chapter == 10:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("chapter10")
    elif chapter == 11:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("bad_sayori")
    elif chapter == 12:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("bad_yuri")
    elif chapter == 13:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("bad_natsuki")
    elif chapter == 14:
        $ renpy.hide_screen("preferences")
        $ renpy.call_screen("bad_monika")
    else:
        $ renpy.utter_restart()
    return()

init -1 python:
    def FinishChangeName():
        if not player: return
        persistent.playername = persistent.change_name
        renpy.save_persistent()
        renpy.hide_screen("change_name")
        if persistent.save_name == True:
            SaveName()
        if persistent.change_language:
            persistent.change_language = False
            renpy.show_screen("dialog", message="Now reload the game for Language settings.", ok_action=renpy.reload_script)
        else:
            renpy.show_screen("dialog", message="Now reload the game for name changing.", ok_action=renpy.reload_script)

init -501 screen change_name(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        if _preferences.language == None:
            input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        else:
            input default "" value VariableInputValue("player") length 12 pixel_width 168 exclude "{}"
        hbox:
            xalign 0.5
            spacing 100
            textbutton _("OK") action ok_action
    if not persistent.change_language:
        key "K_ESCAPE" action [Play("sound", gui.activate_sound), Hide("change_name"),SetPersistent("change_name", ""),SetVariable("player",persistent.playername)]

    $ persistent.change_name = player
    $ renpy.save_persistent()


init -1 python:
    def UninstallMod():
        try:
            with open(config.gamedir + "/pythonpack", "w") as f:
                f.write("1")
        except:
            pass
        if _preferences.language == None:
            try:
                with open(config.basedir + "/lang", "w") as f:
                    f.write("en")
            except:
                pass
        else:
            try:
                with open(config.basedir + "/lang", "w") as f:
                    f.write("ja")
            except:
                pass
        import sys
        sys.path.remove(renpy.config.gamedir + '\\python-packages\\')
        renpy.change_language(None)
        persistent.ddmcmod_uninstall = True
        persistent.delete_pythonpack = True
        persistent.relaunch = True
        delete_all_saves()
        if persistent.relaunch == True:
            open(config.basedir + "/relaunch.vbs", "w").write(renpy.file("relaunch.vbs").read())
            import os
            import subprocess
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            cmd = "cscript " + config.basedir + "\\relaunch.vbs"
            subprocess.call(cmd, startupinfo=si)
            persistent.relaunch = False
            renpy.save_persistent()
            renpy.quit()
        return

    if persistent.ddmcmod_uninstall == True:
        import os
        try: os.unlink(config.basedir + "/game/scripts_ddmc.rpa")
        except: pass
        try: os.unlink(config.basedir + "/game/jp_ddmc.rpa")
        except: pass
        try: os.unlink(config.basedir + "/game/none_ddmc.rpa")
        except: pass
        persistent.ddmcmod_uninstall = False
        persistent.oncedeleted_ddmcmod = True
        persistent.delete_pythonfiles = False
        persistent.remove_pythonpack = False
        try: os.unlink(config.basedir + "/game/saves/persistent")
        except: pass
        try: os.unlink(config.savedir + "/persistent")
        except: pass
        try: os.unlink(config.basedir + "/lang")
        except: pass
        try: os.unlink(config.gamedir + "/pythonpack")
        except: pass
        try: os.unlink(config.gamedir + "/name")
        except: pass
        try: os.unlink(config.basedir + "/relaunch.vbs")
        except: pass
        try: os.unlink(config.basedir + "/music_filelist.txt")
        except: pass
        try: os.unlink(config.basedir + "/sfx_filelist.txt")
        except: pass
        #renpy.save_persistent()
        renpy.quit()

translate None python:
    readme_file = "README.html"

init -1 python:
    def FinishEnterName2():
        if not player: return
        persistent.new_name = True
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        quick_menu = True
        if persistent.save_name == True:
            SaveName()
        persistent.new_name = False
        renpy.show_screen("dialog", message="{b}CAUTION!!{/b}\nYou can't save or load in chapter mode!", ok_action=[Hide("dialog"),Hide("main_menu"),Hide("preferences"),ShowMenu("chapter1")])

#label say_tl(label_name):
#    if _preferences.language != None:
#        call expression label_name + "_" + str(_preferences.language)
#    else:
#        call expression label_name
#    return

translate None screen:
    screen navigation():
        key "K_ESCAPE" action Return()
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.8
            spacing gui.navigation_spacing
            if not persistent.autoload or not main_menu:
                if main_menu:
                    if persistent.playthrough == 1:
                        textbutton _("??n??≫?t?A????i≪") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName3)))
                    else:
                        if persistent.chapter == False and persistent.newyear == False and persistent.monikabirth == False:
                            textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName3)))
                        if persistent.chapter == True:
                            textbutton _("Chapter") action If(persistent.playername, true=Show(screen="dialog", message="{b}CAUTION!!{/b}\nYou can't save or load in chapter mode!", ok_action=[Hide("dialog"),Hide("main_menu"),Hide("preferences"),ShowMenu("chapter1")]), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName2)))
                        if persistent.chapter == False and persistent.newyear == True and _preferences.language != None:
                            textbutton _("New Year") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName3)))
                        if persistent.chapter == False and persistent.monikabirth == True and _preferences.language != None:
                            textbutton _("Just Monika") action If(persistent.playername, true=Start("monika_birthday"), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName3)))
                else:
                    textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                    if persistent.chapter == False and persistent.newyear == False and persistent.monikabirth == False:
                        textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

                if persistent.chapter == False and persistent.newyear == False and persistent.monikabirth == False:
                    textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=True)
                elif not main_menu:
                    if persistent.playthrough != 3:
                        textbutton _("Main Menu") action MainMenu()
                        if persistent.chapter == True:
                            textbutton _("Chapter") action Show(screen="dialog", message="{b}CAUTION!!{/b}\nYou can't save or load in chapter mode!", ok_action=[Hide("dialog"),Hide("preferences"),Jump("Set_chapter")])
                    else:
                        textbutton _("Main Menu") action NullAction()
                textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
                textbutton _("Credits") action [ShowMenu("credits"), SensitiveIf(renpy.get_screen("credits") == None)]
                if main_menu:
                    textbutton _("Sound Test") action Start("sound_test_not_debug")
                if renpy.variant("pc"):
                    textbutton _("Help") action [Function(open_readme_url), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
                    textbutton _("Quit") action Quit(confirm=not main_menu)
                if persistent.debug_mode:
                    textbutton _("Debug") action Start("debug_mode")
                    textbutton _("Reload") action renpy.utter_restart
            else:
                timer 1.75 action Start("autoload_yurikill")

translate None screen:
    screen preferences() tag menu:
        if renpy.mobile:
            $ cols = 2
        else:
            $ cols = 4

        use game_menu(_("Settings"), scroll="viewport"):
            vbox:
                xoffset 50
                hbox:
                    box_wrap True
                    if renpy.variant("pc"):
                        vbox:
                            style_prefix "radio"
                            label _("Display")
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    if config.developer:
                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable")
                            textbutton _("Left") action Preference("rollback side", "left")
                            textbutton _("Right") action Preference("rollback side", "right")
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")

                    vbox:
                        style_prefix "check"
                        label _("Rollback")
                        textbutton _("ON") action [SetField(config, "rollback_enabled", True),Show(screen="dialog", message="You can use \'Rollback\' with mouse wheel.", ok_action=Hide("dialog"))]
                        textbutton _("OFF") action SetField(config, "rollback_enabled", False)
                    vbox:
                        style_prefix "check"
                        label _("Animation")
                        textbutton _("Normal") action SetPersistent("save_graphic", False)
                        textbutton _("Light") action SetPersistent("save_graphic", True)
                hbox:
                    if main_menu and persistent.newyear == False and persistent.monikabirth == False:
                        vbox:
                            style_prefix "check"
                            label _("Chapter mode")
                            textbutton _("ON") action SetPersistent("chapter", True)
                            textbutton _("OFF") action SetPersistent("chapter", False)

                    if main_menu and persistent.chapter == False and persistent.monikabirth == False and _preferences.language != None:
                        vbox:
                            style_prefix "check"
                            label _("New Year Event")
                            textbutton _("ON") action SetPersistent("newyear", True)
                            textbutton _("OFF") action SetPersistent("newyear", False)

                    if persistent.playername:
                        vbox:
                            label _("")
                            textbutton _("Change player name"):
                                action [SetVariable("player", ""), Show(screen="change_name", message="Please enter your name you want to change.", ok_action=Function(FinishChangeName))]
                                style "navigation_button"
                    if main_menu:
                        vbox:
                            label _("")
                            textbutton _("Volume Setting"):
                                action Hide("preferences"),ShowMenu('sound_volume_main')
                                style "navigation_button"

                        vbox:
                            label _("")
                            textbutton _("Text Setting"):
                                action Hide("preferences"),ShowMenu('text_setting_main')
                                style "navigation_button"

                null height (4 * gui.pref_spacing)



                hbox:
                    box_wrap True
                    if not persistent.monikabirth and not persistent.newyear:
                        vbox:
                            style_prefix "check"
                            label _("Language")
                            textbutton _("English") action [SetPersistent("change_language",True),Language(None), SetVariable("player", ""), Show(screen="change_name", message="Please change your name", ok_action=[SetPersistent("change_language", True), Function(FinishChangeName)])]
                            $ languages = renpy.known_languages()
                            for language in languages:
                                textbutton _(language) action [SetPersistent("change_language",True),Language(language), SetVariable("player", ""), Show(screen="change_name", message="Please change your name", ok_action=[SetPersistent("change_language", True), Function(FinishChangeName)])]
                    vbox:
                        style_prefix "check"
                        label _("Auto")
                        textbutton _("Poem") action ToggleField(persistent, 'jpmode_auto_poem', true_value=True, false_value=False)

                    vbox:
                        style_prefix "check"
                        label _("Hide username")
                        textbutton _("ON") action SetPersistent("hideusername", True)
                        textbutton _("OFF") action [SetPersistent("hideusername", False),Show(screen="dialog", message="{b}CAUTION!{/b}\nIf you broadcasting or recording video now,\nplease be caraful displaying username!!", ok_action=Hide("dialog"))]

                    vbox:
                        style_prefix "check"
                        label _("Save name")
                        textbutton _("ON") action If(not renpy.loadable("name") and persistent.playername, true=[SetPersistent("save_name", True),Show(screen="confirm", message="Do you want to save name file?",yes_action=[Function(SaveName),Hide("confirm"),Show(screen="dialog", message="Now reload the game for \"save name\"setting", ok_action=renpy.reload_script)], no_action=Hide("confirm"))], false=SetPersistent("save_name", True))
                        textbutton _("OFF") action If(renpy.loadable("name"), true=[SetPersistent("save_name", False),Show(screen="confirm", message="Do you want to delete name file?",yes_action=[Function(DeleteNameFile),Hide("confirm"),Show(screen="dialog", message="Now reload the game for \"save name\"setting", ok_action=renpy.reload_script)], no_action=Hide("confirm"))], false=SetPersistent("save_name", False))

                    if main_menu and datetime.date.today().year == 2019 and datetime.date.today().month == 9 and datetime.date.today().day == 22 and _preferences.language != None and not persistent.chapter and not persistent.newyear:
                       vbox:
                            style_prefix "check"
                            label _("Monika")
                            textbutton _("ON") action SetPersistent("monikabirth", True)
                            textbutton _("OFF") action SetPersistent("monikabirth", False)
                hbox:
                    vbox:
                        style_prefix "check"
                        label _("Hide some horror effects")
                        textbutton _("ON") action SetPersistent("horror_effects", False)
                        textbutton _("OFF") action SetPersistent("horror_effects", True)

                    if ddmm_online:
                        vbox:
                            style_prefix "check"
                            label _("DDMM\nAchievement")
                            textbutton _("ON") action SetPersistent("ddmm_achievement", True),ddmm_default_achievement
                            textbutton _("OFF") action SetPersistent("ddmm_achievement", False)

                    vbox:
                        style_prefix "check"
                        label _("Gamepad")
                        textbutton _("ON") action [SetPersistent("gamepad", True),Show(screen="dialog", message="Now reload the game for Gamepad settings.", ok_action=renpy.reload_script)]
                        textbutton _("OFF") action [SetPersistent("gamepad", False),Show(screen="dialog", message="Now reload the game for Gamepad settings.", ok_action=renpy.reload_script)]

                    if persistent.gamepad:
                        vbox:
                            style_prefix "check"
                            label _("Change\nbutton layout")
                            textbutton _("ON") action SetPersistent("change_buttons", True),change_button_layout
                            textbutton _("OFF") action SetPersistent("change_buttons", False),change_button_layout

                    if renpy.loadable("debug") and config.console:
                        vbox:
                            style_prefix "check"
                            label _("Debug mode")
                            textbutton _("ON") action SetPersistent("debug_mode", True),change_button_layout
                            textbutton _("OFF") action SetPersistent("debug_mode", False),change_button_layout

        text "ddlc_v[config.version]":
            xalign 1.0 yalign 1.0
            xoffset -45 yoffset -30
            style "main_menu_version"

        text "ddmc_v2.4.1":
            xalign 1.0 yalign 1.0
            xoffset -43 yoffset -10
            style "main_menu_version"

translate None screen:
    screen name_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("player") length 12 pixel_width 168 exclude "{}"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action

translate None screen:
    screen music_tag_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("music_filename") length 12 pixel_width 168 exclude "{}"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action

translate None screen:
    screen voice_num_input(message, ok_action):
        modal True
        zorder 200
        style_prefix "confirm"
        add "gui/overlay/confirm.png"
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]
        frame:
            has vbox:
                xalign .5
                yalign .5
                spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input default "" value VariableInputValue("set_num") length 3 allow "0123456789"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK") action ok_action

translate None screen:
    screen quick_menu():


        zorder 100

        if quick_menu:


            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 0.995

                if not quick_menu_limit:
                    textbutton _("History") action ShowMenu('history')
                    textbutton _("Skip") action Skip()
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                if not quick_menu_limit:
                    if persistent.chapter == False and persistent.newyear == False and persistent.monikabirth == False:
                        textbutton _("Save") action ShowMenu('save')
                        textbutton _("Load") action ShowMenu('load')


                    textbutton _("Settings") action ShowMenu('preferences')
                textbutton _("Volume Setting") action ShowMenu('sound_volume_main')
                textbutton _("Text Setting") action ShowMenu('text_setting_main')

translate None screen:
    screen confirm(message, yes_action, no_action):


        modal True

        zorder 200

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch" xalign 0.5

            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action


translate None screen:
    screen fake_navigation():
        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.8

            spacing gui.navigation_spacing

            if persistent.normal_end == 1:
                textbutton _("New Game") action Start("normal_end2")
            elif persistent.normal_end == 2:
                textbutton _("New Game") action Start("normal_end2_2_main")
            else:
                textbutton _("New Game") action NullAction()
            textbutton _("Load Game") action NullAction()
            textbutton _("Settings") action NullAction()
            textbutton _("Help") action NullAction()
            textbutton _("Quit") action NullAction()


init -501 screen chapter1():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter1"),ShowMenu("preferences")]
    if persistent.chapter_seen[0]:
        add "bg/chapter1.png"
        style_prefix "game_menu"

        textbutton _("Start from Chapter 1"):
            style "return_button"
            xalign 0.5 ypos 700

            action SetPersistent("chapter_sel", True),Start()

        text ("Chapter 1: The story so far"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):

            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter1")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter1")
            else:
                action ShowMenu("preferences"), Hide("chapter1")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter2"), Hide("chapter1")
    else:
        add "bg/q.png"
        style_prefix "game_menu"

        textbutton _("Start from Chapter 1"):
            style "return_button"
            xalign 0.5 ypos 700

            action None

        text ("Chapter 1: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):

            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter1")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter1")
            else:
                action ShowMenu("preferences"), Hide("chapter1")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter2"), Hide("chapter1")

init -501 screen chapter2():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter2"),ShowMenu("preferences")]
    if persistent.chapter_seen[1]:
        add "bg/chapter2.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 2"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch2_main")

        text ("Chapter 2: Glorius morning"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter2")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter2")
            else:
                action ShowMenu("preferences"), Hide("chapter2")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter1"), Hide("chapter2")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter3"), Hide("chapter2")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 2"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 2: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter2")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter2")
            else:
                action ShowMenu("preferences"), Hide("chapter2")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter1"), Hide("chapter2")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter3"), Hide("chapter2")

init -501 screen chapter3():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter3"),ShowMenu("preferences")]
    if persistent.chapter_seen[2]:
        add "bg/chapter3.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 3"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch3_1_main")

        text ("Chapter 3: Today is school festival!"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter3")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter3")
            else:
                action ShowMenu("preferences"), Hide("chapter3")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter2"), Hide("chapter3")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter4"), Hide("chapter3")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 3"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 3: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter3")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter3")
            else:
                action ShowMenu("preferences"), Hide("chapter3")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter2"), Hide("chapter3")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter4"), Hide("chapter3")


init -501 screen chapter4():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter4"),ShowMenu("preferences")]
    if persistent.chapter_seen[3]:
        add "bg/chapter4.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 4"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch4_main")

        text ("Chapter 4: In front of club room"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter4")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter4")
            else:
                action ShowMenu("preferences"), Hide("chapter4")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter3"), Hide("chapter4")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter5"), Hide("chapter4")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 4"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 4: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter4")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter4")
            else:
                action ShowMenu("preferences"), Hide("chapter4")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter3"), Hide("chapter4")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter5"), Hide("chapter4")


init -501 screen chapter5():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter5"),ShowMenu("preferences")]
    if persistent.chapter_seen[4]:
        add "bg/chapter5.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 5"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch5_1_main")

        text ("Chapter 5: Preparation for school festival"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter5")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter5")
            else:
                action ShowMenu("preferences"), Hide("chapter5")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter4"), Hide("chapter5")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter6"), Hide("chapter5")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 5"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 5: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter5")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter5")
            else:
                action ShowMenu("preferences"), Hide("chapter5")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter4"), Hide("chapter5")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter6"), Hide("chapter5")


init -501 screen chapter6():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter6"),ShowMenu("preferences")]
    if persistent.chapter_seen[5]:
        add "bg/chapter6.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 6"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch6_1_main")

        text ("Chapter 6: Yuri and Natsuki's death"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter6")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter6")
            else:
                action ShowMenu("preferences"), Hide("chapter6")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter5"), Hide("chapter6")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter7"), Hide("chapter6")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 6"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 6: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter6")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter6")
            else:
                action ShowMenu("preferences"), Hide("chapter6")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter5"), Hide("chapter6")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter7"), Hide("chapter6")


init -501 screen chapter7():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter7"),ShowMenu("preferences")]
    if persistent.chapter_seen[6]:
        add "bg/chapter7.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 7"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch7_main")

        text ("Chapter 7: Just Monika"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter7")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter7")
            else:
                action ShowMenu("preferences"), Hide("chapter7")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter6"), Hide("chapter7")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter8"), Hide("chapter7")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 7"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 7: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter7")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter7")
            else:
                action ShowMenu("preferences"), Hide("chapter7")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter6"), Hide("chapter7")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter8"), Hide("chapter7")


init -501 screen chapter8():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter8"),ShowMenu("preferences")]
    if persistent.chapter_seen[7]:
        add "bg/chapter8.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 8"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch8_main")

        text ("Chapter 8: Do you believe in Monika?"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter8")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter8")
            else:
                action ShowMenu("preferences"), Hide("chapter8")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter7"), Hide("chapter8")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter9"), Hide("chapter8")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 8"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 8: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter8")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter8")
            else:
                action ShowMenu("preferences"), Hide("chapter8")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter7"), Hide("chapter8")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter9"), Hide("chapter8")


init -501 screen chapter9():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter9"),ShowMenu("preferences")]
    if persistent.chapter_seen[8]:
        add "bg/chapter9.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 9"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch9_main")

        text ("Chapter 9: What is the reality for you?"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter9")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter9")
            else:
                action ShowMenu("preferences"), Hide("chapter9")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter8"), Hide("chapter9")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter10"), Hide("chapter9")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 9"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 9: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter9")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter9")
            else:
                action ShowMenu("preferences"), Hide("chapter9")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter8"), Hide("chapter9")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter10"), Hide("chapter9")


init -501 screen chapter10():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter10"),ShowMenu("preferences")]
    if persistent.chapter_seen[9]:
        add "bg/chapter10.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 10"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("ch10_main")

        text ("Chapter 10: Parafait Grils"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter10")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter10")
            else:
                action ShowMenu("preferences"), Hide("chapter10")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter9"), Hide("chapter10")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_sayori"), Hide("chapter10")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start from Chapter 10"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Chapter 10: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter10")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter10")
            else:
                action ShowMenu("preferences"), Hide("chapter10")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter9"), Hide("chapter10")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_sayori"), Hide("chapter10")


init -501 screen bad_sayori():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("bad_sayori"),ShowMenu("preferences")]
    if persistent.chapter_seen[10]:
        add "bg/bad_sayori.png"
        style_prefix "game_menu"
        textbutton _("Start Bad Sayori"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("bad_sayori_main")

        text ("Bad End: Sayori side"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_sayori")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_sayori")
            else:
                action ShowMenu("preferences"), Hide("bad_sayori")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter10"), Hide("bad_sayori")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_yuri"), Hide("bad_sayori")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Bad ???"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Bad End: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_sayori")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_sayori")
            else:
                action ShowMenu("preferences"), Hide("bad_sayori")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter10"), Hide("bad_sayori")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_yuri"), Hide("bad_sayori")


init -501 screen bad_yuri():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("bad_yuri"),ShowMenu("preferences")]
    if persistent.chapter_seen[11]:
        add "bg/bad_yuri.png"
        style_prefix "game_menu"
        textbutton _("Start Bad Yuri"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("bad_yuri_main")

        text ("Bad End: Yuri side"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_yuri")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_yuri")
            else:
                action ShowMenu("preferences"), Hide("bad_yuri")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_sayori"), Hide("bad_yuri")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_natsuki"), Hide("bad_yuri")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Bad ???"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Bad End: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_yuri")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_yuri")
            else:
                action ShowMenu("preferences"), Hide("bad_yuri")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_sayori"), Hide("bad_yuri")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_natsuki"), Hide("bad_yuri")

init -501 screen bad_natsuki():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("bad_natsuki"),ShowMenu("preferences")]
    if persistent.chapter_seen[12]:
        add "bg/bad_natsuki.png"
        style_prefix "game_menu"
        textbutton _("Start Bad Natsuki"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("bad_natsuki_main")

        text ("Bad End: Natsuki side"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_natsuki")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_natsuki")
            else:
                action ShowMenu("preferences"), Hide("bad_nastuki")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_yuri"), Hide("bad_natsuki")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_monika"), Hide("bad_natsuki")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Bad ???"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Bad End: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_natsuki")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_natsuki")
            else:
                action ShowMenu("preferences"), Hide("bad_nastuki")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_yuri"), Hide("bad_natsuki")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("bad_monika"), Hide("bad_natsuki")


init -501 screen bad_monika():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("bad_monika"),ShowMenu("preferences")]
    if persistent.chapter_seen[13]:
        add "bg/bad_monika.png"
        style_prefix "game_menu"
        textbutton _("Start Bad Monika"):
            style "return_button"
            xalign 0.5 ypos 700
            action SetPersistent("chapter_sel", True),Start("bad_monika_main")

        text ("Bad End: Monika side"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_monika")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_monika")
            else:
                action ShowMenu("preferences"), Hide("bad_monika")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_natsuki"), Hide("bad_monika")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter_normal"), Hide("bad_monika")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Bad ???"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Bad End: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("bad_monika")
            elif debug_mode:
                action Jump("debug_mode"), Hide("bad_monika")
            else:
                action ShowMenu("preferences"), Hide("bad_monika")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_natsuki"), Hide("bad_monika")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter_normal"), Hide("bad_monika")

init -501 screen chapter_normal():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter_normal"),ShowMenu("preferences")]
    if persistent.chapter_seen[14]:
        add "bg/normal_end.png"
        style_prefix "game_menu"
        textbutton _("Start Normal End"):
            style "return_button"
            xalign 0.5 ypos 700
            action Show(screen="confirm", message="{b}CAUTION!!{/b}\nIf you see this end,you can't come back to the true title.\nAre you sure?",yes_action=[SetPersistent("chapter_sel", True),Start("normal_end")], no_action=Hide("confirm"))

        text ("Normal End: The world without Monika"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter_normal")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter_normal")
            else:
                action ShowMenu("preferences"), Hide("chapter_normal")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_monika"), Hide("chapter_normal")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter_normal2"), Hide("chapter_normal")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Normal End"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Normal End: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter_normal")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter_normal")
            else:
                action ShowMenu("preferences"), Hide("chapter_normal")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("bad_monika"), Hide("chapter_normal")

        textbutton _("Next..."):
            style "return_button"
            xpos 1150 ypos 400
            action ShowMenu("chapter_normal2"), Hide("chapter_normal")


init -501 screen chapter_normal2():
    if main_menu:
        key "mouseup_3" action Return()
    else:
        key "mouseup_3" action [Hide("chapter_normal2"),ShowMenu("preferences")]
    if persistent.chapter_seen[15]:
        add "bg/normal_end2.png"
        style_prefix "game_menu"
        textbutton _("Start Normal End2"):
            style "return_button"
            xalign 0.5 ypos 700
            action Show(screen="confirm", message="{b}CAUTION!!{/b}\nIf you see this end,you can't come back to the true title.\nAre you sure?",yes_action=[SetPersistent("chapter_sel", True),Start("normal_end2_2")], no_action=Hide("confirm"))

        text ("Normal End 2: No one is there. Only me."):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter_normal2")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter_normal2")
            else:
                action ShowMenu("preferences"), Hide("chapter_normal2")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter_normal"), Hide("chapter_normal2")
    else:
        add "bg/q.png"
        style_prefix "game_menu"
        textbutton _("Start Normal End2"):
            style "return_button"
            xalign 0.5 ypos 700
            action None

        text ("Normal End 2: ???"):
            style "return_button"
            xalign 0.5 ypos 100

        textbutton _("Return"):
            style "return_button"
            if main_menu:
                action ShowMenu("main_menu"), Hide("chapter_normal2")
            elif debug_mode:
                action Jump("debug_mode"), Hide("chapter_normal2")
            else:
                action ShowMenu("preferences"), Hide("chapter_normal2")

        textbutton _("Previous..."):
            style "return_button"
            xpos 50 ypos 400
            action ShowMenu("chapter_normal"), Hide("chapter_normal2")

init -1 style window_m is window:
    background Image("gui/m_namebox.png", xalign=0.5, yalign=1.0)
    outlines [(3, "#5b5", 0, 0), (1, "#5b5", 1, 1)]

init -1 style window_s is window:
    background Image("gui/s_namebox.png", xalign=0.5, yalign=1.0)

init -1 style window_y is window:
    background Image("gui/y_namebox.png", xalign=0.5, yalign=1.0)

init -1 style window_n is window:
    background Image("gui/n_namebox.png", xalign=0.5, yalign=1.0)

init -1 style window_mc is window:
    background Image("gui/mc_namebox.png", xalign=0.5, yalign=1.0)

init -1 style window_q is window:
    background Image("gui/q_namebox.png", xalign=0.5, yalign=1.0)

init -1 style main_menu_button is gui_button

init -1 style main_menu_button_text is gui_button_text

init -1 style navigation_button is gui_button

init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]

translate None screen:
    screen main_menu() tag menu:
        if persistent.normal_end == 0:
            style_prefix "main_menu"

            if persistent.ghost_menu:
                add "white"
                add "menu_art_y_ghost"
                add "menu_art_n_ghost"
            else:
                add "menu_bg"
                if chibi_title:
                    add "y_sticker_title"
                    add "n_sticker_title"
                else:
                    add "menu_art_y"
                    add "menu_art_n"
                frame



                
                use navigation
                if not ddmm_online:
                    vbox:
                        textbutton ("Delete Mod"):
                            action Show(screen="confirm", message="Are you sure you want to delete this mod?\nDDMC's save data will be also deleted", yes_action=Function(UninstallMod), no_action=Hide("confirm"))
                            style_prefix "main_menu_button"
                        textbutton ("Delete Savedata"):
                            action Show(screen="confirm", message="Are you sure you want to delete only save data?", yes_action=Function(delete_all_savedata), no_action=Hide("confirm"))
                            style_prefix "main_menu_button"

            if gui.show_name:

                vbox:
                    text "[config.name!t]":
                        style "main_menu_title"

                    text "[config.version]":
                        style "main_menu_version"

            if not persistent.ghost_menu:
                add "menu_particles"
                add "menu_particles"
                add "menu_particles"
                add "menu_logo"
            if persistent.ghost_menu:
                add "menu_art_s_ghost"
                add "menu_art_m_ghost"
            else:
                if persistent.playthrough == 1 or persistent.playthrough == 2:
                    add "menu_art_s_glitch"
                else:
                    if chibi_title:
                        add "s_sticker_title"
                    else:
                        add "menu_art_s"
                add "menu_particles"
                if persistent.playthrough != 4:
                    if chibi_title:
                        add "m_sticker_title"
                    else:
                        add "menu_art_m"
                add "menu_fade"

            key "K_ESCAPE" action Quit(confirm=False)
        else:
            style_prefix "main_menu"
            add "menu_bg"
            if persistent.normal_end == 1:
                add "menu_art_y"
                add "menu_art_n"
            frame
            use fake_navigation
            if not ddmm_online:
                vbox:
                    textbutton ("Delete Savedata"):
                        action Show(screen="confirm", message="Are you sure you want to delete only save data?", yes_action=Function(delete_all_savedata), no_action=Hide("confirm"))
                        style_prefix "main_menu_button"
            if persistent.normal_end == 1:
                add "menu_art_s"
            add "menu_particles"
            add "menu_particles"
            add "menu_particles"
            add "menu_logo"
            add "menu_fade"

            key "K_ESCAPE" action Quit(confirm=False),SetPersistent("chapter", False)

init -1 style main_menu_button:
    size_group "main_menu_button"
    properties gui.button_properties("main_menu_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style main_menu_button_text:
    properties gui.button_text_properties("main_menu_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]

image s_sticker_title:
    subpixel True
    "s_sticker"
    xcenter 510
    ycenter 500
    zoom 1.68
    menu_art_move(1.68, 510, 1.68)

image m_sticker_title:
    subpixel True
    "m_sticker"
    xcenter 1050
    ycenter 420
    zoom 1.68
    menu_art_move(1.68, 1050, 1.68)

image y_sticker_title:
    subpixel True
    "y_sticker"
    xcenter 600
    ycenter 185
    zoom 1.60
    menu_art_move(1.68, 600, 1.68)

image n_sticker_title:
    subpixel True
    "n_sticker"
    xcenter 850
    ycenter 235
    zoom 1.58
    menu_art_move(1.68, 850, 1.68)

init -501 screen credits() tag menu:






    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("DDLC Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("The Original Work : Doki Doki Literature Club! by Team Salvato\nProgramming : mayonesu @horizonmayone\nScripts : yamamotoNEW @yamnewb\nCollaborator : katykmas @sinokoki_fps\nTest Players : Natsukiket @natsukiket\nSpecial Thanks to: Chris_K\nSpecial Thanks to: Proudust @proudust\nBackground Art Works: Kimagure After\n")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size

init -501 screen sound_volume_main():
    add "bg/back.png"
    style_prefix "game_menu"
    hbox:
        style_prefix "slider"
        box_wrap True
        xalign 0.5 yalign 0.5
        vbox:
            if config.has_music:
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume")

            if config.has_sound:
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume")

            if config.has_voice:
                label _("Voice Volume")
                hbox:
                    bar value Preference("voice volume")
    hbox:
        xpos 220 yalign 0.8
        vbox:
            if not main_menu:
                xalign 0.25
                textbutton _("Back"):
                    style "return_button"
                    action Hide("sound_volume_main"),Return()
            else:
                textbutton _("Back"):
                    style "return_button"
                    action Hide("sound_volume_main"),ShowMenu("preferences")
        vbox:
            xalign 0.5
            textbutton _("Text Setting"):
                style "return_button"
                action Hide("sound_volume_main"),ShowMenu("text_setting_main")
        vbox:
            xpos 100
            textbutton _("Reset Volume"):
                action Function(reset_volume)
                style "return_button"

init -501 screen text_setting_main():
    add "bg/back.png"
    style_prefix "game_menu"
    hbox:
        style_prefix "slider"
        box_wrap True
        xalign 0.5 yalign 0.5
        vbox:
            label _("Text Speed")
            bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)
            label _("Auto-Forward Time")
            bar value Preference("auto-forward time")

    hbox:
        xpos 220 yalign 0.8
        vbox:
            if not main_menu:
                xalign 0.25
                textbutton _("Back"):
                    style "return_button"
                    action Hide("text_setting_main"),Return()
            else:
                xalign 0.25
                textbutton _("Back"):
                    style "return_button"
                    action Hide("text_setting_main"),ShowMenu("preferences")
        vbox:
            xalign 0.5
            textbutton _("Volume Setting"):
                style "return_button"
                action Hide("text_setting_main"),ShowMenu("sound_volume_main")
        vbox:
            xalign 0.75
            textbutton _("Reset Text Setting"):
                action Function(reset_text_settings)
                style "return_button"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
