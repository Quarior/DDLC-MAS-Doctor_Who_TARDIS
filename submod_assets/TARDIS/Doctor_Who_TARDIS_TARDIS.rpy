define TARDIS_take_off = "submods/Doctor_Who_TARDIS/submod_assets/TARDIS/tardis_take_off.mp3"
define TARDIS_travel_loop = "submods/Doctor_Who_TARDIS/submod_assets/TARDIS/tardis_travel_loop.mp3"
image image_TARDIS_normal_d = "submods/Doctor_Who_TARDIS/submod_assets/TARDIS/TARDIS_button_normal.png"
image image_TARDIS_normal_n = "submods/Doctor_Who_TARDIS/submod_assets/TARDIS/TARDIS_button_normal_n.png"
image image_TARDIS_normal = ConditionSwitch(
 "mas_current_background.isFltDay()", "image_TARDIS_normal_d",
 "True", "image_TARDIS_normal_n")
image image_TARDIS_hover = "submods/Doctor_Who_TARDIS/submod_assets/TARDIS/TARDIS_button_hover.png"

transform def_TARDIS_pos:
    xpos 903
    ypos 153

init 502 python:
    MASImageTagDecoDefinition.register_img(
        "image_TARDIS_normal",
        store.mas_background.MBG_DEF,
        MASAdvancedDecoFrame(at_list=[def_TARDIS_pos],zorder=7)
    )
