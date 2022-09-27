init 501 python:
    def register_deco(deco,bg=mas_current_background):
        global MASImageTagDecoDefinition
        if bg.background_id != store.mas_background.MBG_DEF and MASImageTagDecoDefinition.get_adf(bg.background_id, deco) == None:
            MASImageTagDecoDefinition.register_img_same(
                deco,
                store.mas_background.MBG_DEF,
                bg.background_id
            )
