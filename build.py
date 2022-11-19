KV='''

           
MDNavigationLayout:
    # MDTopAppBar:
    #     id: title
    #     #pos_hint: {'x':0,'y':.9}
    #     title: 'NB-IT Dictionary'
    #     left_action_items: [['menu', lambda x: nav_d.set_state('toggle')]] 
    #     #left_action_items: [['power', lambda x: app.on_close()]]

    ScreenManager:
        Screen:
            BoxLayout:
                MDTopAppBar:
                    id: bottom
                    title: 'NB-IT Dictionary'
                    elevation: 4
                    left_action_items: [['menu', lambda x: nav_d.set_state('toggle')]] 
            # Image:
            #     pos_hint: {'x': .1, 'y':9}
            #     size_hint: 1, None
            #     size: '120dp', '120dp'
            #     source: 'NBIT.png'
            MDFloatingActionButtonSpeedDial:
                id: speed_dial 
                data: app.data
                type: 'large'
                callback: app.callback
                hint_animation: False
            # GridLayout:
            #     pos_hint: {'x':0,'y':0}
            #     #size_hint:1,.8
            #     cols:2
            #     height: '30dp'
            FloatLayout:
                MDTextField:
                    id: input
                    icon_left: 'pencil'
                    pos_hint_x: '0'
                    pos_hint:{'x': 0, 'y':.9}
                    mode: 'rectangle'
                    size_hint: 1, None
                    fill_color: 0,0,0,.2
                    hint_text: 'Cerca'
                    on_text: app.src(self.text)
                    #required: True
                # MDIconButton:
                #     id: src
                #     pos_hint:{'x': .85, 'y':.9}
                #     icon: 'magnify'
                #     size_hint_x: .1
                #     #text: 'CERCA'
                #     pos_hint_x: .85
                #     on_release: app.src()
                ScrollView:
                    id: sw
                    pos_hint:{'x': 0, 'y':.2}
                    do_scroll_x: False
                    size_hint: .8,.7
                    MDList:
                        id: tr
    MDNavigationDrawer:
        anchor: 'left'
        id: nav_d
        size_hint_x: .6
        close_on_click: True
        BoxLayout:
            anchor: 'left'
            orientation: 'vertical'
            pos_hint: {'center_x': .5, 'center_y':.5}
            #spacing: '2dp'
            Image:
                #pos_hint: {'x': .1, 'y':0}
                size_hint: 1, None
                size: '120dp', '120dp'
                source: 'NBIT.png'
            MDNavigationDrawerDivider:
            # MDRectangleFlatIconButton:
            #     id: options
            #     text: 'Opzioni'
            #     icon: 'cog'
            #     line_color: 0,0,0,0
            #     size_hint_x: 1
            #   on_press: app.opt()
            MDLabel:
                pos_hint: {'x': 0, 'y': .5}
                font_style: 'Body1'
                id: count  
            MDNavigationDrawerDivider:
            MDRectangleFlatIconButton:
                id: exit
                text: 'Esci'
                icon: 'power'
                font_style: 'H6'
                size_hint_x: 1
                line_color: 0,0,0,0
                on_release: app.on_close()
<pal_dial>
    orientation:'vertical'
    size_hint_y:None
    size_hint_x: .5
    height: '120dp'
    ScrollView:
        do_scroll_x: False
        pos_hint: {'center_x':.5, 'center_y':.5}
        # size_hint_y: 0.5
        #size_hint_x: .5
        MDList:
            id: tr_                                           
    '''
KV_='''
BoxLayout:
    MDBottomAppBar:
        MDTopAppBar:
            title: ''
            icon: 'cog'
    
    FloatLayout:
        MDTextField:
            id: input
            pos_hint:{'x': 0, 'y':.9}
            mode: 'rectangle'
            size_hint: .8, None
            fill_color: 0,0,0,0
            hint_text: 'Cerca'
            #required: True
        MDIconButton:
            id: src
            pos_hint:{'x': .85, 'y':.9}
            icon: 'magnify'
            size_hint_x: .1
            #text: 'CERCA'
            pos_hint_x: .85
            #md_bg_color: app.theme_cls.primary_color
            #theme_icon_color: 'Custom'
            #icon_color: app.theme_cls.secondary_text_color
            on_release: app.src()
        ScrollView:
            id: sw
            pos_hint:{'x': 0, 'y':.2}
            do_scroll_x: False
            size_hint: .8,.7
            MDList:
                theme_text_color: 'Custom'
                id: tr

'''
