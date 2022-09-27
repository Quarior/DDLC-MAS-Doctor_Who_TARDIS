################################################################################
## VARIABLES
################################################################################

init -1500 python:
    Init_Load = True
    import os
    directory_Doctor_Who_TARDIS = os.path.join(config.gamedir,"submods/Doctor_Who_TARDIS")
    Doctor_Who_TARDIS_file_inside_TARDIS = os.path.join(directory_Doctor_Who_TARDIS,"Doctor_Who_TARDIS_inside_TARDIS.txt")
    Doctor_Who_TARDIS_old_background = {}
    Doctor_Who_TARDIS_inside_TARDIS = 0
    TARDIS_Travel = False
    try:
        with open(Doctor_Who_TARDIS_file_inside_TARDIS, mode="r") as fileR:
            Doctor_Who_TARDIS_inside_TARDIS = int(fileR.read())
    except:
        with open(Doctor_Who_TARDIS_file_inside_TARDIS, mode="w") as fileW:
            fileW.write(str(Doctor_Who_TARDIS_inside_TARDIS))

################################################################################
## SCREENS
################################################################################

screen TARDIS_button():
    layer "master"
    zorder 7

    vbox:
        xpos 903
        ypos 153

        if not inside_TARDIS_console_room_F() and "hkb_overlay" in config.overlay_screens:
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    imagebutton:
                        idle "image_TARDIS_normal"
                else:
                    imagebutton:
                        idle "image_TARDIS_normal"
            elif store._mas_getAffection() >= 400:
                imagebutton:
                    idle "image_TARDIS_normal"
                    hover "image_TARDIS_hover"
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                    action Function(renpy.call,label="go_to_out_TARDIS_console_room",go_to=True)
            else:
                imagebutton:
                    idle "image_TARDIS_normal"

screen screen_inside_TARDIS_console_room_exit_door():
    layer "master"
    zorder 7

    vbox:
        xpos 973
        ypos 191

        if inside_TARDIS_console_room_F() and "hkb_overlay" in config.overlay_screens:
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    imagebutton:
                        idle "image_TARDIS_console_room_exit_door_pos"
                else:
                    imagebutton:
                        idle "image_TARDIS_console_room_exit_door_pos"
            else:
                imagebutton:
                    idle "image_TARDIS_console_room_exit_door_pos"
                    hover "image_TARDIS_console_room_exit_door_hover"
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                    action Function(renpy.call,label="go_to_out_TARDIS_console_room",go_to=False)

transform rotTextTARDISConsoleRoom:
    # Rotation for the text on the console
    rotate -4.50 # degrees

screen screen_inside_TARDIS_console_room_console():
    layer "master"
    zorder 8
    style_prefix "hkb"
    vbox:
        xpos 83
        ypos 366

        if inside_TARDIS_console_room_F() and "hkb_overlay" in config.overlay_screens:
            if store.mas_hotkeys.talk_enabled is False:
                if mas_submod_utils.current_label == "mas_piano_setupstart":
                    imagebutton:
                        idle "image_TARDIS_console_room_console_normal"
                else:
                    imagebutton:
                        idle "image_TARDIS_console_room_console_normal"
            else:
                imagebutton:
                    idle "image_TARDIS_console_room_console_normal"
                    hover "image_TARDIS_console_room_console_hover"
                    hover_sound gui.hover_sound
                    activate_sound gui.activate_sound
                    action Function(show_calendar)

    vbox:
        spacing 0
        xpos 83
        ypos 366
        xanchor 0
        yanchor 0

        $ textLocation = _("{horiz=True}Location: " + str(mas_current_background.prompt) + "{/horiz}")
        $ textTimeUTC = _("{horiz=True}Time: " + datetime.datetime.utcnow().strftime("%A %d %B %Y %H:%M:%S %z") + "{/horiz}")
        $ textTimeLocal = _("{horiz=True}Time: " + datetime.datetime.now().strftime("%A %d %B %Y %H:%M:%S %z") + "{/horiz}")
        default TimeTz = "UTC"
        default textTimeTz = _("{horiz=True}{size=12}To local timezone{/size}{/horiz}")

        if inside_TARDIS_console_room_F() and ("hkb_overlay" in config.overlay_screens or TARDIS_Travel):
            text textLocation xpos 2 ypos -10 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 size 12 adjust_spacing False at rotTextTARDISConsoleRoom
            if TARDIS_Travel:
                textbutton _("{horiz=True}{size=12}Space travel{/size}{/horiz}") xpos 3 ypos -100 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 at rotTextTARDISConsoleRoom
            else:
                textbutton _("{horiz=True}{size=12}Space travel{/size}{/horiz}") xpos 3 ypos -100 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 at rotTextTARDISConsoleRoom:
                    action Function(renpy.call,label="TARDIS_console_room_space_travel")
            if TimeTz == "UTC":
                $ textTime = textTimeUTC
                text textTime xpos 4 ypos -270 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 size 12 adjust_spacing True at rotTextTARDISConsoleRoom
                textbutton textTimeTz xpos 140 ypos -443 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 at rotTextTARDISConsoleRoom:
                    clicked [SetScreenVariable("textTime", textTimeUTC), SetScreenVariable("TimeTz", "Local"), SetScreenVariable("textTimeTz", _("{horiz=True}{size=12}To UTC timezone{/size}{/horiz}"))]
            else:
                $ textTime = textTimeLocal
                text textTime xpos 4 ypos -270 xanchor 0 yanchor 0 xmaximum 275 ymaximum 20 size 12 adjust_spacing False at rotTextTARDISConsoleRoom
                textbutton textTimeTz xpos 140 ypos -443 xanchor 0 yanchor 0 xmaximum 137 ymaximum 20 at rotTextTARDISConsoleRoom:
                    clicked [SetScreenVariable("textTime", textTimeLocal), SetScreenVariable("TimeTz", "UTC"), SetScreenVariable("textTimeTz", _("{horiz=True}{size=12}To local timezone{/size}{/horiz}"))]
            if TARDIS_Travel or mas_seenEvent("TARDIS_console_room_time_travel"):
                textbutton _("{horiz=True}{size=12}Time travel{/size}{/horiz}") xpos 4 ypos -553 xanchor 0 yanchor 0 xmaximum 137 ymaximum 20 at rotTextTARDISConsoleRoom
            else:
                textbutton _("{horiz=True}{size=12}Time travel{/size}{/horiz}") xpos 4 ypos -553 xanchor 0 yanchor 0 xmaximum 137 ymaximum 20 at rotTextTARDISConsoleRoom:
                    action Function(renpy.call,label="TARDIS_console_room_time_travel")


################################################################################
## FUNCTIONS/CLASSES
################################################################################

init python:
    def TARDISVisible(): # Check if the TARDIS screen it is visible
        return "TARDIS_button" in config.overlay_screens

    def inside_TARDIS_console_room_F(): # Check if we are inside the TARDIS
        global Doctor_Who_TARDIS_inside_TARDIS
        return bool(Doctor_Who_TARDIS_inside_TARDIS)

    def change_Doctor_Who_TARDIS_inside_TARDIS(value): # Function to change and update the Doctor_Who_TARDIS_inside_TARDIS
        global Doctor_Who_TARDIS_inside_TARDIS
        Doctor_Who_TARDIS_inside_TARDIS = value
        with open(Doctor_Who_TARDIS_file_inside_TARDIS, mode="w") as fileW:
            fileW.write(str(value))
        return value

    def TARDISButton(): # Function to displa/hide the TARDIS
        if not TARDISVisible() and not inside_TARDIS_console_room_F():
        # if mas_seenEvent("mas_reaction_gift_TARDIS") and not TARDISVisibleF() and not persistent.Doctor_Who_TARDIS_inside_TARDIS:
            config.overlay_screens.append("TARDIS_button")
        elif TARDISVisible() and inside_TARDIS_console_room_F():
            config.overlay_screens.remove("TARDIS_button")

    def TARDIS_console_room(bg=mas_current_background,display=True,now=not Init_Load):
            global MASImageTagDecoDefinition
            global Doctor_Who_TARDIS_old_background
            if mas_current_background != None: # Safety in case no background it is set
                if not Doctor_Who_TARDIS_old_background.get(bg):
                    Doctor_Who_TARDIS_old_background[bg] = {"hide_calendar": bg.hide_calendar, "entry_pp": bg.entry_pp, "exit_pp": bg.exit_pp, mas_background.EXP_SKIP_TRANSITION: None}
                    if mas_background.EXP_SKIP_TRANSITION in bg.ex_props:
                        Doctor_Who_TARDIS_old_background[bg][mas_background.EXP_SKIP_TRANSITION] = bg.ex_props[mas_background.EXP_SKIP_TRANSITION]
                bg.entry_pp = mas_background._Doctor_Who_TARDIS_entry
                bg.exit_pp = mas_background._Doctor_Who_TARDIS_exit
                if bg.background_id != store.mas_background.MBG_DEF:
                    mas_reset.ch30_reset(501)
                    register_deco("image_TARDIS_console_room",bg=bg)
                    register_deco("image_TARDIS_normal",bg=bg)
                change_Doctor_Who_TARDIS_inside_TARDIS(int(display))
                if display:
                    mas_showDecoTag("image_TARDIS_console_room",show_now=now)
                    mas_hideDecoTag("image_TARDIS_normal",hide_now=now)
                    if not "screen_inside_TARDIS_console_room_exit_door" in config.overlay_screens:
                        config.overlay_screens.append("screen_inside_TARDIS_console_room_exit_door")
                    if not "screen_inside_TARDIS_console_room_console" in config.overlay_screens:
                        config.overlay_screens.append("screen_inside_TARDIS_console_room_console")
                    bg.hide_calendar = True
                    renpy.hide_screen("calendar_overlay", layer="master")
                    bg.ex_props[mas_background.EXP_SKIP_TRANSITION] = True
                    store.mas_flagEVL("monika_change_background", "EVE", store.EV_FLAG_HFNAS)
                elif not display:
                    mas_hideDecoTag("image_TARDIS_console_room",hide_now=now)
                    mas_showDecoTag("image_TARDIS_normal",show_now=now)
                    if "screen_inside_TARDIS_console_room_exit_door" in config.overlay_screens:
                        config.overlay_screens.remove("screen_inside_TARDIS_console_room_exit_door")
                    if "screen_inside_TARDIS_console_room_console" in config.overlay_screens:
                        config.overlay_screens.remove("screen_inside_TARDIS_console_room_console")
                    bg.hide_calendar = Doctor_Who_TARDIS_old_background[bg]["hide_calendar"]
                    if not bg.hide_calendar:
                        renpy.show_screen("calendar_overlay", _layer="master")
                    bg.ex_props[mas_background.EXP_SKIP_TRANSITION] = Doctor_Who_TARDIS_old_background[bg][mas_background.EXP_SKIP_TRANSITION]
                    if store._mas_getAffection() >= 400:
                        store.mas_unflagEVL("monika_change_background", "EVE", store.EV_FLAG_HFNAS)
                TARDISButton() # Update the statut of display the TARDIS or not

init -2 python in mas_background:
    def _Doctor_Who_TARDIS_entry(_old, **kwargs):
        """
        Entry programming point of the background for the submod

        NOTE: ANYTHING IN THE `_old is None` CHECK WILL BE RUN **ON LOAD ONLY**
        IF IT IS IN THE CORRESPONDING 'else' BLOCK, IT WILL RUN WHEN THE BACKGROUND IS CHANGED DURING THE SESSION

        IF YOU WANT IT TO RUN IN BOTH CASES, SIMPLY PUT IT AFTER THE ELSE BLOCK
        """

        try:
            store.Doctor_Who_TARDIS_old_entry_pp(_old, **kwargs)
        except Exception:
            renpy.log(Exception)

        store.TARDIS_console_room(bg=_old,display=store.inside_TARDIS_console_room_F(),now=False)

        store.TARDISButton()

    def _Doctor_Who_TARDIS_exit(_new, **kwargs):
        """
        Exit programming point of the background for the submod
        """

        try:
            store.Doctor_Who_TARDIS_old_exit_pp(_new, **kwargs)
        except Exception:
            renpy.log(Exception)

        store.TARDIS_console_room(bg=_new,display=store.inside_TARDIS_console_room_F(),now=False)

        store.TARDISButton()

################################################################################
## STARTUP
################################################################################

init 999 python:
    mas_reset.ch30_reset(0)
    TARDIS_console_room(bg=mas_current_background,display=inside_TARDIS_console_room_F(),now=not Init_Load) # Able/Disable the console room of the TARDIS
    Init_Load = False
    TARDISButton()
