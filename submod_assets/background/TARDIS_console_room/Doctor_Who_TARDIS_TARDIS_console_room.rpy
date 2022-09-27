image image_TARDIS_console_room = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room.png"

image image_TARDIS_console_room_exit_door_pos = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room_exit_door_pos.png"
image image_TARDIS_console_room_exit_door_normal = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room_exit_door_normal.png"
image image_TARDIS_console_room_exit_door_hover = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room_exit_door_hover.png"

image image_TARDIS_console_room_console_normal = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room_console_normal.png"
image image_TARDIS_console_room_console_hover = "submods/Doctor_Who_TARDIS/submod_assets/background/TARDIS_console_room/TARDIS_console_room_console_hover.png"

init 502 python:
    MASImageTagDecoDefinition.register_img(
        "image_TARDIS_console_room",
        store.mas_background.MBG_DEF,
        MASAdvancedDecoFrame(zorder=7)
    )
