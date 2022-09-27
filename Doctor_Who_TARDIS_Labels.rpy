label go_to_out_TARDIS_console_room(go_to):
    $ HKBHideButtons()
    scene black
    with dissolve_scene_full
    pause 2
    $ TARDIS_console_room(bg=mas_current_background,display=go_to,now=not Init_Load)
    $ HKBShowButtons()
    return

label TARDIS_console_room_space_travel:
    # Copy of monika_change_background
    m 1hua "Sure!"

    #FALL THROUGH

label TARDIS_monika_change_background_loop:
    # Copy of monika_change_background_loop

    show monika 1eua at t21

    $ renpy.say(m, "Where would you like to go?", interact=False)

    python:
        # build menu list
        import store.mas_background as mas_background
        import store.mas_moods as mas_moods

        # we assume that we will always have more than 1
        # default should always be at the top
        backgrounds = [(mas_background_def.prompt, mas_background_def, False, False)]

        #o31 just gets o31 enabled BGs
        other_backgrounds = list()

        #TODO: I don't really like this, but we limit to only o31 supported bgs during the o31 event
        if persistent._mas_o31_in_o31_mode:
            other_backgrounds = [
                (mbg_obj.prompt, mbg_obj, False, False)
                for mbg_id, mbg_obj in mas_background.BACKGROUND_MAP.iteritems()
                if mbg_id != "spaceroom" and mbg_obj.unlocked and mas_doesBackgroundHaveHolidayDeco(MAS_O31_DECO_TAGS, mbg_id)
            ]

        #D25 supporting bgs
        elif persistent._mas_d25_deco_active:
            other_backgrounds = [
                (mbg_obj.prompt, mbg_obj, False, False)
                for mbg_id, mbg_obj in mas_background.BACKGROUND_MAP.iteritems()
                if mbg_id != "spaceroom" and mbg_obj.unlocked and mas_doesBackgroundHaveHolidayDeco(mas_d25_utils.DECO_TAGS, mbg_id)
            ]

        #Non holiday specific bg sel
        else:
            # build other backgrounds list
            other_backgrounds = [
                (mbg_obj.prompt, mbg_obj, False, False)
                for mbg_id, mbg_obj in mas_background.BACKGROUND_MAP.iteritems()
                if mbg_id != "spaceroom" and mbg_obj.unlocked
            ]

        # sort other backgrounds list
        other_backgrounds.sort()

        # build full list
        backgrounds.extend(other_backgrounds)

        # now add final quit item
        final_item = (mas_background.BACKGROUND_RETURN, False, False, False, 20)

    # call scrollable pane
    call screen mas_gen_scrollable_menu(backgrounds, mas_ui.SCROLLABLE_MENU_TXT_MEDIUM_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, final_item)

    $ sel_background = _return

    show monika at t11

    # return value False? then return
    if sel_background is False:
        return "prompt"

    if sel_background == mas_current_background:
        m 1hua "We're here right now, silly."
        m "Try again~"
        jump monika_change_background_loop

    python:
        skip_leadin = mas_background.EXP_SKIP_LEADIN in sel_background.ex_props
        if inside_TARDIS_console_room_F():
            skip_transition = True
        else:
            skip_transition = mas_background.EXP_SKIP_TRANSITION in sel_background.ex_props
        skip_outro = mas_background.EXP_SKIP_OUTRO in sel_background.ex_props

    # UI shields + buttons
    # NOTE: buttons are in here since there is no consistency if placed in
    # the bg change label.
    $ mas_RaiseShield_core()
    $ HKBHideButtons()
    $ TARDIS_Travel = True

    call TARDIS_mas_background_change(sel_background, skip_leadin=skip_leadin, skip_transition=skip_transition, skip_outro=skip_outro, set_persistent=True)

    $ HKBShowButtons()
    $ TARDIS_Travel = False
    $ mas_DropShield_core()

    return

#Generic background changing label, can be used if we wanted a sort of story related change
label TARDIS_mas_background_change(new_bg, skip_leadin=False, skip_transition=True, skip_outro=False, set_persistent=False):
    # otherwise, we can change the background now
    if not skip_leadin and inside_TARDIS_console_room_F():
        play sound "{0}".format(TARDIS_take_off)
        m 1eua "Alright!"
        m 1hua "Let's go, [player]!"
    elif not skip_leadin and not inside_TARDIS_console_room_F():
        m 1eua "Alright!"
        m 1hua "Let's go, [player]!"

    #Little transition
    if not skip_transition:
        hide monika
        scene black
        with dissolve
        pause 2.0

    elif skip_transition and inside_TARDIS_console_room_F():
        $ renpy.sound.play("<loop 0.5>{0}".format(TARDIS_travel_loop), fadein=1, loop=True)
        scene image_Doctor_Who_Vortex
        show image_TARDIS_console_room
        show monika 1hua at i11
        with dissolve
        pause 4.0


    python:

        #Set persistent
        if set_persistent:
            persistent._mas_current_background = new_bg.background_id

        #Store the old bg for use later
        old_bg = mas_current_background

        #Otherwise, If we're disabling progressive AND hiding masks, weather isn't supported here
        #so we lock to clear
        if new_bg.disable_progressive and new_bg.hide_masks:
            mas_weather.temp_weather_storage = mas_current_weather
            mas_changeWeather(mas_weather_def, new_bg=new_bg)

        else:
            if mas_weather.temp_weather_storage is not None:
                mas_changeWeather(mas_weather.temp_weather_storage, new_bg=new_bg)
                #Now reset the temp storage for weather
                mas_weather.temp_weather_storage = None

            else:
                #If we don't have tempstor, run the startup weather
                mas_startupWeather()

            #Then we unlock the weather sel here
            mas_unlockEVL("monika_change_weather", "EVE")

        #If we've disabled progressive and hidden masks, then we shouldn't allow weather change
        #NOTE: If you intend to force a weather for your background, set it via prog points
        if new_bg.disable_progressive:
            mas_lockEVL("monika_change_weather", "EVE")

        #Finally, change the background
        change_info = mas_changeBackground(new_bg)

    #Now redraw the room
    if skip_transition and inside_TARDIS_console_room_F():
        $ renpy.sound.stop(channel=u'sound', fadeout=1)
        call spaceroom(scene_change=not skip_transition, dissolve_all=False, bg_change_info=change_info)

    else:
        call spaceroom(scene_change=not skip_transition, dissolve_all=True, bg_change_info=change_info, force_exp="monika 1hua")

    if not skip_outro:
        m 1eua "Here we are!"
        m "Let me know if you want to go somewhere else, okay?"
    return

label TARDIS_console_room_time_travel:
    m 3ekb "I'm sorry [player], but time travel is disabled.\nI think I should disable this button."
    return
