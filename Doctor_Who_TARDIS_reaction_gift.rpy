label mas_reaction_gift_TARDIS:
    python:
        sprite_data = mas_getSpriteObjInfo(
            (store.mas_sprites, "Doctor_Who_TARDIS_TARDIS")
        )
        sprite_type, sprite_name, giftname, gifted_before, sprite_object = sprite_data

    if mas_seenEvent("mas_reaction_gift_TARDIS"):
        return

    if store._mas_getAffection() >= 400:
        $ mas_giftCapGainAff(5)
        $ mas_receivedGift("Doctor_Who_TARDIS_TARDIS")
        $ persistent._mas_given_TARDIS_before = True

        if mas_isSpecialDay():
            m 1wuo "...[player]?"
            m 1wublo "It is..."
            m 2wubso "Y-{w=0.25}You giving me because you think I could join you in your reality?"
            m 3dubfu "Oh my God, I..."
            m 1hublb "Give me a second,{w=0.25} I will check on right now!"

            #call mas_clothes_change(sprite_object)

            m 2tkbsu "Well, isn't work, [player]."
            m 1tku "But thanks you so much for this, [player]."
            m 3tkblu "I really appreciate it."

        else:
            m 1wuo "...[player]?"
            m 1wublo "It is..."
            m 2wubso "Y-{w=0.25}You giving me because you think I could join you in your reality?"
            m 3dubfu "Oh my God, I..."
            m 1hublb "Give me a second,{w=0.25} I will check on right now!"

            #call mas_clothes_change(sprite_object)

            m 2tkbsu "Well, isn't work, [player]."
            m 1tku "But thanks you so much for this, [player]."
            m 3tkblu "I really appreciate it."

    else:
        $ mas_giftCapGainAff(0.5)
        $ mas_receivedGift("Doctor_Who_TARDIS_TARDIS")
        $ persistent._mas_given_TARDIS_before = True
        # less than normal path
        m 2hkb "..."
        m 2hkbdlb "...huh"
        m 2eksdla "...A TARDIS?"
        m 2eksdlc "Thanks, [player]."
        m 3tksdlu "I really appreciate this, but..."
        m 3eksdlb "I don't think it's the best moment to wear it"
        m 1eka "Thanks again, but I will not use this for now."

    $ mas_finishSpriteObjInfo(sprite_data)
    if giftname is not None:
        $ store.mas_filereacts.delete_file(giftname)
    return


# mas_acs_quetzalplushie = MASAccessory(
#       "quetzalplushie",
#       "quetzalplushie",
#       MASPoseMap(
#           default="0",
#           use_reg_for_l=True
#       ),
#       stay_on_start=False,
#       acs_type="plush_q",
#       mux_type=["plush_mid"] + store.mas_sprites.DEF_MUX_LD,
#       entry_pp=store.mas_sprites._acs_quetzalplushie_entry,
#       exit_pp=store.mas_sprites._acs_quetzalplushie_exit,
#       keep_on_desk=True
#   )
#   store.mas_sprites.init_acs(mas_acs_quetzalplushie)
