from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class UserGenerationKeyboard:



    @staticmethod
    def country_buttons():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        world_button = KeyboardButton(text='Весь мир🌎')
        ua_button = KeyboardButton(text='Украина🇺🇦')
        ru_button = KeyboardButton(text='Россия🇷🇺')
        by_button = KeyboardButton(text='Беларусь⬜️🟥⬜️')
        others_button = KeyboardButton(text = 'Остальные страны')
        keyboard.add(world_button, ua_button, ru_button, by_button, others_button)
        return keyboard
    @staticmethod
    def other_countries():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        eu_button = KeyboardButton(text='Европа')
        asia_button = KeyboardButton(text='Азия')
        africa_button = KeyboardButton(text = 'Африка')
        usa_button = KeyboardButton('Америка')
        australia_button = KeyboardButton('Австралия🇦🇺')
        back_button = KeyboardButton('🔙Назад')

        keyboard.add(eu_button, asia_button, africa_button, usa_button, australia_button, back_button)
        return keyboard


    @staticmethod
    def europe_countries():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        east_eu_button = KeyboardButton(text = 'Восточная Европа')
        west_eu_button = KeyboardButton(text='Западная Европа')
        south_eu_button = KeyboardButton(text='Южная Европа')
        north_eu_button = KeyboardButton(text = 'Северная Европа')
        back_eu_button = KeyboardButton(text='🔙Остальные страны')
        keyboard.add(east_eu_button, west_eu_button, south_eu_button, north_eu_button, back_eu_button)
        return keyboard
    
    @staticmethod
    def east_europe():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        cz_button = KeyboardButton(text = 'Чехия🇨🇿')
        bg_button = KeyboardButton(text='Болгария🇧🇬')
        hu_button = KeyboardButton(text='Венгрия🇭🇺')
        md_button = KeyboardButton(text='Молдавия🇲🇩')
        pl_button = KeyboardButton(text='Польша🇵🇱')
        ro_button = KeyboardButton(text='Румыния🇷🇴')
        sk_button = KeyboardButton(text='Словакия🇸🇰')
        back_eus_button = KeyboardButton(text = '🔙Регионы Европы')
        keyboard.add(cz_button, bg_button, hu_button, md_button, pl_button, ro_button, sk_button, back_eus_button)
        return keyboard

    @staticmethod
    def west_europe():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        at_button = KeyboardButton(text='Австрия🇦🇹')
        be_button = KeyboardButton(text ='Бельгия🇧🇪')
        gb_button = KeyboardButton(text='Великобритания🇬🇧')
        de_button = KeyboardButton(text='Германия🇩🇪')
        ie_button = KeyboardButton(text='Ирландия🇮🇪')
        li_button = KeyboardButton(text='Лихтенштейн🇱🇮')
        lu_button = KeyboardButton(text='Люксембург🇱🇺')
        mc_button = KeyboardButton(text='Монако🇲🇨')
        nl_button = KeyboardButton(text='Нидерланды🇳🇱')
        fr_button = KeyboardButton(text='Франция🇫🇷')
        ch_button = KeyboardButton(text='Швейцария🇨🇭')



        back_eus_button = KeyboardButton(text = '🔙Регионы Европы')
        keyboard.add(at_button, be_button, gb_button, de_button, ie_button, li_button, lu_button, mc_button,nl_button, fr_button, ch_button, back_eus_button)
        return keyboard

    @staticmethod
    def south_europe():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        al_button = KeyboardButton(text='Албания🇦🇱')
        ad_button = KeyboardButton(text='Андорра🇦🇩')
        ba_button = KeyboardButton(text='Босния и Герцеговина🇧🇦')
        gr_button = KeyboardButton(text='Греция🇬🇷')
        es_button = KeyboardButton(text='Испания🇪🇸')
        it_button = KeyboardButton(text='Италия🇮🇹')
        cy_button = KeyboardButton(text='Кипр🇨🇾')
        mt_button = KeyboardButton(text='Мальта🇲🇹')
        pt_button = KeyboardButton(text='Португалия🇵🇹')
        sm_button = KeyboardButton(text='Сан-Марино🇸🇲')
        mk_button = KeyboardButton(text='Македония🇲🇰')
        rs_button = KeyboardButton(text='Сербия🇷🇸')
        si_button = KeyboardButton(text='Словения🇸🇮')
        hr_button = KeyboardButton(text='Хорватия🇭🇷')
        me_button = KeyboardButton(text='Черногория🇲🇪')


        back_eus_button = KeyboardButton(text = '🔙Регионы Европы')
        keyboard.add(al_button, ad_button, ba_button, gr_button, es_button, it_button, cy_button, mt_button, pt_button, sm_button, mk_button, rs_button, si_button, hr_button, me_button, back_eus_button)
        return keyboard

    @staticmethod
    def north_europe():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        dk_button = KeyboardButton(text='Дания🇩🇰')
        is_button = KeyboardButton(text='Исландия🇮🇸')
        lv_button = KeyboardButton(text='Латвия🇱🇻')
        lt_button = KeyboardButton(text='Литва🇱🇹')
        no_button = KeyboardButton(text='Норвегия🇳🇴')
        fi_button = KeyboardButton(text='Финляндия🇫🇮')
        se_button = KeyboardButton(text='Швеция🇸🇪')
        ee_button = KeyboardButton(text='Эстония🇪🇪')




        back_eus_button = KeyboardButton(text = '🔙Регионы Европы')
        keyboard.add(dk_button, is_button, lv_button, lt_button, no_button, fi_button, se_button, ee_button, back_eus_button)
        return keyboard


    @staticmethod
    def asian_countries():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        east_asian_button = KeyboardButton(text = 'Восточная Азия')
        west_asian_button = KeyboardButton(text='Западная Азия')
        southeast_asian_button = KeyboardButton(text='Юго-Восточная Азия')
        south_asian_button = KeyboardButton(text = 'Южная Азия')
        middle_asian_button = KeyboardButton(text = 'Центральная Азия')
        back_eu_button = KeyboardButton(text='🔙Остальные страны')
        keyboard.add(east_asian_button, west_asian_button, southeast_asian_button, south_asian_button, middle_asian_button, back_eu_button)
        return keyboard

    @staticmethod
    def east_asia():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        cn_button = KeyboardButton(text='Китай🇨🇳')
        jp_button = KeyboardButton(text='Япония🇯🇵')
        kr_button = KeyboardButton(text='Южная Корея🇰🇷')
        kp_button = KeyboardButton(text='Северная Корея🇰🇵')
        mn_button = KeyboardButton(text='Монголия🇲🇳')




        back_asia_button = KeyboardButton(text='🔙Регионы Азии')
        keyboard.add(cn_button, jp_button, kr_button, kp_button, mn_button, back_asia_button)
        return keyboard
    
    @staticmethod
    def west_asia():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        am_button = KeyboardButton(text='Армения🇦🇲')
        lb_button = KeyboardButton(text='Ливан🇱🇧')
        sy_button = KeyboardButton(text='Сирия🇸🇾')
        bh_button = KeyboardButton(text='Бахрейн🇧🇭')
        az_button = KeyboardButton(text='Азербайджан🇦🇿')
        jo_button = KeyboardButton(text='Иордания🇯🇴')
        ye_button = KeyboardButton(text='Йемен🇾🇪')
        qa_button = KeyboardButton(text='Катар🇶🇦')
        iq_button = KeyboardButton(text='Ирак🇮🇶')
        kw_button = KeyboardButton(text='Кувейт🇰🇼')
        ae_button = KeyboardButton(text='Арабские Эмираты🇦🇪')
        om_button = KeyboardButton(text='Оман🇴🇲')
        sa_button = KeyboardButton(text='Саудовская Аравия🇸🇦')
        tr_button = KeyboardButton(text='Турция🇹🇷')

        back_asia_button = KeyboardButton(text='🔙Регионы Азии')
        keyboard.add(am_button, lb_button, sy_button, bh_button, az_button, jo_button, ye_button, qa_button, iq_button, kw_button, ae_button, om_button, sa_button, tr_button, back_asia_button)
        return keyboard
    
    @staticmethod
    def southest_asia():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        th_button = KeyboardButton(text='Таиланд🇹🇭')
        vn_button = KeyboardButton(text='Вьетнам🇻🇳')
        id_button = KeyboardButton(text='Индонезия🇮🇩')
        bn_button = KeyboardButton(text='Бруней🇧🇳')
        kh_button = KeyboardButton(text='Камбоджа🇰🇭')
        la_button = KeyboardButton(text='Лаос🇱🇦')
        tl_button = KeyboardButton(text='Тимор - Леште🇹🇱')
        my_button = KeyboardButton(text='Малайзия🇲🇾')
        sg_button = KeyboardButton(text='Сингапур🇸🇬')
        ph_button = KeyboardButton(text='Филиппины🇵🇭')



        back_asia_button = KeyboardButton(text='🔙Регионы Азии')
        keyboard.add(th_button, vn_button, id_button, bn_button, kh_button, la_button, tl_button, my_button, sg_button, ph_button, back_asia_button)
        return keyboard
    
    @staticmethod
    def south_asia():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        in_button = KeyboardButton(text='Индия🇮🇳')
        pk_button = KeyboardButton(text='Пакистан🇵🇰')
        bd_button = KeyboardButton(text='Бангладеш🇧🇩')
        ir_button = KeyboardButton(text='Иран🇮🇷')
        af_button = KeyboardButton(text='Афганистан🇦🇫')
        mv_button = KeyboardButton(text='Мальдивы🇲🇻')
        bt_button = KeyboardButton(text='Бутан🇧🇹')
        np_button = KeyboardButton(text='Непал🇳🇵')
        lk_button = KeyboardButton(text='Шри-Ланка🇱🇰')





        back_asia_button = KeyboardButton(text='🔙Регионы Азии')
        keyboard.add(in_button, pk_button, bd_button, ir_button, af_button, mv_button, bt_button, np_button, lk_button, back_asia_button)
        return keyboard

    @staticmethod
    def middle_asia():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        kg_button = KeyboardButton(text='Киргизия🇰🇬')
        tj_button = KeyboardButton(text='Таджикистан🇹🇯')
        kz_button = KeyboardButton(text='Казахстан🇰🇿')
        uz_button = KeyboardButton(text='Узбекистан🇺🇿')




        back_asia_button = KeyboardButton(text='🔙Регионы Азии')
        keyboard.add(kg_button, tj_button, kz_button, uz_button, back_asia_button)
        return keyboard

    @staticmethod
    def african_countries():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        north_africa = KeyboardButton(text='Северная Африка')
        east_africa = KeyboardButton(text='Восточная Африка')
        west_africa = KeyboardButton(text='Западная Африка')
        middle_africa = KeyboardButton(text='Центральная Африка')
        south_africa = KeyboardButton(text='Южная Африка')

        back_eu_button = KeyboardButton(text='🔙Остальные страны')
        keyboard.add(north_africa, east_africa, west_africa, middle_africa, south_africa, back_eu_button)
        return keyboard
    
    @staticmethod
    def north_africa():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        eg_button = KeyboardButton(text='Египет🇪🇬')
        tn_button = KeyboardButton(text='Тунис🇹🇳')
        dz_button = KeyboardButton(text='Алжир🇩🇿')
        ly_button = KeyboardButton(text='Ливия🇱🇾')
        eh_button = KeyboardButton(text='Западная Сахара🇪🇭')
        ma_button = KeyboardButton(text='Марокко🇲🇦')
        mr_button = KeyboardButton(text='Мавритания🇲🇷')


        back_africa_button = KeyboardButton(text='🔙Регионы Африки')
        keyboard.add(eg_button, tn_button, dz_button, ly_button, eh_button, ma_button, mr_button, back_africa_button)
        return keyboard
    
    @staticmethod
    def east_africa():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ke_button = KeyboardButton(text='Кения🇰🇪')
        mz_button = KeyboardButton(text='Мозамбик🇲🇿')
        bi_button = KeyboardButton(text='Бурунди🇧🇮')
        mg_button = KeyboardButton(text='Мадагаскар🇲🇬')
        rw_button = KeyboardButton(text='Руанда🇷🇼')
        so_button = KeyboardButton(text='Сомали🇸🇴')
        et_button = KeyboardButton(text='Эфиопия🇪🇹')
        ug_button = KeyboardButton(text='Уганда🇺🇬')
        dj_button = KeyboardButton(text='Джибути🇩🇯')
        sc_button = KeyboardButton(text='Сейшелы🇸🇨')
        er_button = KeyboardButton(text='Эритрея🇪🇷')




        back_africa_button = KeyboardButton(text='🔙Регионы Африки')
        keyboard.add(ke_button, mz_button, bi_button, mg_button, rw_button, so_button, et_button, ug_button, dj_button, sc_button, er_button, back_africa_button)
        return keyboard


    @staticmethod
    def west_africa():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ng_button = KeyboardButton(text='Нигерия🇳🇬')
        gh_button = KeyboardButton(text=' Гана🇬🇭')
        sl_button = KeyboardButton(text='Сьерра-Леоне🇸🇱')
        ci_button = KeyboardButton(text="Кот д'Ивуар🇨🇮")
        bf_button = KeyboardButton(text='Буркина-Фасо🇧🇫')
        sn_button = KeyboardButton(text='Сенегал🇸🇳')
        ml_button = KeyboardButton(text='Мали🇲🇱')
        bj_button = KeyboardButton(text='Бенин🇧🇯')
        gm_button = KeyboardButton(text='Гамбия🇬🇲')
        cm_button = KeyboardButton(text='Камерун🇨🇲')
        lr_button = KeyboardButton(text='Либерия🇱🇷')

        back_africa_button = KeyboardButton(text='🔙Регионы Африки')
        keyboard.add(ng_button, gh_button, sl_button, ci_button, bf_button, sn_button, ml_button, bj_button, gm_button, cm_button, lr_button, back_africa_button)
        return keyboard


    @staticmethod
    def middle_africa():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        cg_button = KeyboardButton(text='Конго🇨🇬')
        ao_button = KeyboardButton(text='Ангола🇦🇴')
        gq_button = KeyboardButton(text='Гвинея🇬🇶')
        st_button = KeyboardButton(text='Сан-Томе и Принсипи🇸🇹')
        td_button = KeyboardButton(text='Чад🇹🇩')
        ga_button = KeyboardButton(text='Габон🇬🇦')
        cf_button = KeyboardButton(text='ЦАР🇨🇫')


        back_africa_button = KeyboardButton(text='🔙Регионы Африки')
        keyboard.add(cg_button, ao_button, gq_button, st_button, td_button, ga_button, cf_button, back_africa_button)
        return keyboard
    
    @staticmethod
    def south_africa():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        zw_button = KeyboardButton(text='Зимбабве🇿🇼')
        mu_button = KeyboardButton(text='Маврикий🇲🇺')
        ls_button = KeyboardButton(text='Лесото🇱🇸')
        bw_button = KeyboardButton(text='Ботсвана🇧🇼')
        za_button = KeyboardButton(text='ЮАР🇿🇦')


        back_africa_button = KeyboardButton(text='🔙Регионы Африки')
        keyboard.add(zw_button, mu_button, ls_button, bw_button, za_button, back_africa_button)
        return keyboard
    
    @staticmethod
    def american_countries():
        keboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        north_america = KeyboardButton(text='Северная Америка')
        south_america = KeyboardButton(text='Южная Америка')
        middle_america = KeyboardButton(text='Центральная Америка')
        karib_america = KeyboardButton(text='Карибский регион')

        back_eu_button = KeyboardButton(text='🔙Остальные страны')
        keboard.add(north_america, south_america, middle_america, karib_america, back_eu_button)
        return keboard
    
    @staticmethod
    def north_america():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ca_button = KeyboardButton(text='Канада🇨🇦')
        mx_button = KeyboardButton(text='Мексика🇲🇽')
        us_button = KeyboardButton(text='США🇺🇸')


        back_america_buton = KeyboardButton(text='🔙Регионы Америки')
        keyboard.add(ca_button, mx_button, us_button, back_america_buton)
        return keyboard

    @staticmethod
    def south_america():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ar_button = KeyboardButton(text='Аргентина🇦🇷')
        bo_button = KeyboardButton(text='Боливия🇧🇴')
        br_button = KeyboardButton(text='Бразилия🇧🇷')
        ve_button = KeyboardButton(text='Венесуэла🇻🇪')
        gy_button = KeyboardButton(text='Гайана🇬🇾')
        co_button = KeyboardButton(text='Колумбия🇨🇴')
        py_button = KeyboardButton(text='Парагвай🇵🇾')
        pe_button = KeyboardButton(text='Перу🇵🇪')
        sr_button = KeyboardButton(text='Суринам🇸🇷')
        uy_button = KeyboardButton(text='Уругвай🇺🇾')
        cl_button = KeyboardButton(text='Чили🇨🇱')
        ec_button = KeyboardButton(text='Эквадор🇪🇨')




        back_america_buton = KeyboardButton(text='🔙Регионы Америки')
        keyboard.add(ar_button, bo_button, br_button, ve_button, gy_button, co_button, py_button, pe_button, sr_button, uy_button, cl_button, ec_button, back_america_buton)
        return keyboard
    
    @staticmethod
    def middle_america():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


        back_america_buton = KeyboardButton(text='🔙Регионы Америки')
        keyboard.add()
        return keyboard












