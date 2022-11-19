import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.button.button import MDFloatingBottomButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import Snackbar
from build import KV
from dictionary import *
conn = sqlite3.connect('dict.db')
langs = sqlite3.connect('langs.db')
l_curs= langs.cursor()
curs = conn.cursor()
y=0
try:
    curs.execute('CREATE TABLE verbi (it text, no text)')
    curs.execute('CREATE TABLE adv (it text, no text)')
    curs.execute('CREATE TABLE adj (it text, no text)')
    curs.execute('CREATE TABLE subs (it, text, no text)')
    curs.execute('CREATE TABLE varie (it text, no text)')
except:
    lista = ['adv', 'adj', 'subs', 'varie', 'verbi']
    present = []
    for i in lista:
        for row in curs.execute(f'SELECT * FROM {i}'):
            y = y+len(row)
dic_list = [adv, adj, pron, conj, subs, art]
db_list = ['avv.', 'agg.', 'sost.', '', 'verbo']#
dic_str_list = ['avv.', 'agg.', 'pron.', 'cong.', 'sost.', 'art.']      # stesse variabili di NBIT_Module
vtemp_list = ['infinito >> ', 'presente: ', 'pass. prossimo: ', 'passato: ', 'futuro: ', 'imperativo: ']
temp_str = '' # stringa temporanea allegata alla lista dic_str_list
temp_list = []
################################### PARTE RELATIVA AL CONTEGGIO DELLE PAROLE TOTALI
l=0
for i in dic_list:
    L=len(i.keys())+len(i.values())
    l=l+L
L= len(verb.keys())+ len(verb.values())
l=l+L
lang='it'
not_found= ''
#######################################################################
class pal_dial(BoxLayout):
    pass

class _mditapp_(MDApp):
    data = {
        0: 'theme-light-dark',
        '': 'palette',
        (): 'translate',
        None: 'power'
    }
    def build(self):
        global theme, palette
        for row in l_curs.execute(f'SELECT it FROM langs WHERE id=\'theme\''):
            theme = row[0]
        for row in l_curs.execute(f'SELECT no FROM langs WHERE id=\'theme\''):
            palette = row[0]
        #self.theme_cls.material_style= 'M3'
        self.theme_cls.theme_style=theme
        self.theme_cls.primary_palette=palette
        self.theme_cls.primary_hue= '900'
        #self.theme_cls.primary_dark = '#0f0000'
        return Builder.load_string(KV)
    def speed_dial_color(self):
        s_d_c = []
        for i in range(0,len(self.theme_cls.primary_color)-1):
            if self.theme_cls.primary_color[i]== 0.0:
                s_d_c.append(self.theme_cls.primary_color[i])
            else:
                s_d_c.append(self.theme_cls.primary_color[i] - .2)
        self.root.ids.speed_dial.bg_color_root_button = s_d_c
    def on_start(self,lang='it'):
        global theme, not_found
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'search\''):
            self.root.ids.input.hint_text = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'dictionary\''):
            dictionary = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'database\''):
            database = row[0]
        # for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'options\''):
        #      options = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'exit\''):
             self.root.ids.exit.text = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'language\''):
            language =  row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'not_found\''):
            not_found= row[0]
        self.icon='icon.ico'
        #self.root.ids.sm.current= 'main_screen'
        #self.root.ids.options.text = options
        self.root.ids.count.text= f'''            
[{l}] {dictionary}

[{y}] {database}

Python 3.10.6 
     - Kivy 2.1.0
     - Kivymd 1.0.2
     - BeautifulSoup4 4.11.1
     
E-MAIL: 
    andrewdm91@gmail.com
    
Ver. 0.18

'''
        #self.root.ids.lang_button.text = language
        self.root.ids.speed_dial.icon='cog'
        self.speed_dial_color()
        # self.root.ids.speed_dial.type= 'large'

    def callback(self, instance):
        icon = instance.icon
        # if you want check button, use
        if isinstance(instance, MDFloatingBottomButton):
            if icon == 'palette':
                self.theme(2)
            elif icon == 'translate':
                self.lang()
            elif icon == 'theme-light-dark':
                self.theme(1)
            elif icon == 'power':
                self.on_close()
    def on_close(self):
        exit()
    def lang(self):
        global lang
        if lang == 'it':
            lang= 'no'
        else:
            lang = 'it'
        self.on_start(lang)
    def theme(self,switch):
        self.root.ids.speed_dial.close_stack()
        global theme, palette
        def pal_cng(palette):
            l_curs.execute(f'UPDATE langs SET no=\'{palette}\' WHERE id= \'theme\'')
            langs.commit()
            self.theme_cls.primary_palette = palette
            self.theme_cls.primary_hue = '900'
            self.speed_dial_color()
        if switch == 1:
            if theme == 'Dark':
                theme = 'Light'
            else:
                theme = 'Dark'
            l_curs.execute(f'UPDATE langs SET it=\'{theme}\' WHERE id= \'theme\'')
            langs.commit()
            self.theme_cls.theme_style=theme
        elif switch == 2:
            _palette_ = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
                       'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
                       'Brown', 'Gray', 'BlueGray']
            theme_list = ['#ff0000', '#ffc0cb', '#800080', '#4d004d', '#4b0082', '#0000ff', '#add8e6',
                          '#00ffff', '#008080', '#008000', '#90ee90', '#00ff00', '#ffff00', '#ff9900', '#ffa500',
                          '#d5760d','#a52a2a', '#808080', '#6b8d94']

            self.PD=MDDialog(
                title='Palette',
                type='custom',
                size_hint_x= '.3',
                content_cls=pal_dial(),
                buttons=[
                    (MDFlatButton(
                    text='OK',
                    on_release=lambda x: self.PD.dismiss()
                ))
                ]
            )
            for i in range(len(_palette_)):
                self.PD.content_cls.ids.tr_.add_widget(MDIconButton(size_hint_x='1',icon='palette', theme_icon_color='Custom', icon_color=theme_list[i], on_release=lambda x, pal=_palette_[i]: pal_cng(pal)))
            self.PD.open()
    def src(self, word):
        global not_found
        #word = str(self.root.ids.input.text)
        if word == '':
            pass
        else:
        #self.root.ids.srcd.text = word
            self.root.ids.tr.clear_widgets()
            samme = []
            dic_str_list_counter = 0
            k_list = list(verb.keys())
            v_list = list(verb.values())
            temp_str = 'verbo'
            if word in verb.keys():
                temp_v_list = list(verb.get(word))
                if type(verb.get(word)) == list:  # se verbo, dà la traduzione + conìugazione
                    for i in range(len(vtemp_list)):
                        #print(vtemp_list[i] + '  ' + temp_v_list[i])
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'{vtemp_list[i]} {temp_v_list[i]}',
                                                                            on_release= lambda x, word=temp_v_list[i]: [Clipboard.copy(word), Snackbar(text=f'\'{word}\' Copiato').open()]))
                        samme.append(i)
                else:
                    print('[>>] \n' + word + ' : ' + verb.get(word) + f' ({temp_str})')
            else:
                for i in range(len(v_list)):
                    # print(f'{v_list[i]} {i} ' + str(type(v_list[i])) )
                    if word == v_list[i]:
                        print('\nIT - NB >> ' + k_list[i] + f' ({temp_str})\n')
                    if type(v_list[i]) == list:  # se la value è una lista (in teoria dovranno essere tutte lista)
                        x = 0  # assegno int per trovare l'index di vtemp_list
                        self.root.ids.tr.text_color='#009f00'
                        for j in v_list[i]:
                            x += 1
                            if word == j:
                                # print(f'{word}  > {j} - {x} ... {vtemp_list[i]}')
                                self.root.ids.tr.add_widget(OneLineListItem(text=f'{word} >> {vtemp_list[x - 1]}  {k_list[i]} ({temp_str})',
                                                                            on_release= lambda x: [Clipboard.copy(word), Snackbar(text=f'\'{word}\' Copiato').open()]))
                                samme.append(word)
                                #print(f' \n{word} >> {vtemp_list[x - 1]}  {k_list[i]} ({temp_str})')
                                # x-1 per quadrare i conti :)
            for i in dic_list:
                temp_str = dic_str_list[dic_str_list_counter]
                k_list = list(i.keys())  # creazione di liste temporanee
                v_list = list(i.values())  # per un handling più semplice
                for w in range(len(i.keys())):
                    if word == k_list[w]:
                        if type(v_list[w]) == list:
                            self.root.ids.tr.add_widget(OneLineListItem(text=', '.join(v_list[w]) +f'({temp_str})',
                                                                            on_release= lambda x, txt=v_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                            samme.append(', '.join(v_list[w]))
                        else:
                            self.root.ids.tr.add_widget(OneLineListItem(text=f'{v_list[w]} ({temp_str})',on_release= lambda x, txt=v_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                            samme.append(v_list[w])

                for w in range(len(i.values())):  # per ogni valore tra le values
                    if word in v_list[w] and (type(v_list[w]) == list) or (word == v_list[w]):
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'{k_list[w]} ({temp_str})', on_release= lambda x , txt=k_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                        samme.append(k_list[w])
                dic_str_list_counter +=1
            n_list = 0
            for i in lista:
                for row in curs.execute(f'SELECT no FROM {i} WHERE it=\'{word}\' '):
                   if str(row[0]).lower() in samme:
                       pass
                   else:
                       self.root.ids.tr.add_widget(OneLineListItem(text=f'{row[0]} [! {db_list[n_list]}]',theme_text_color= 'Custom', text_color='green'))
                       samme.append(row[0])
                for row in curs.execute(f'SELECT it FROM {i} WHERE no=\'{word}\''):
                    if row[0] in samme:
                        pass
                    else:
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'{row[0]} [! {db_list[n_list]}]',theme_text_color= 'Custom', text_color='green'))
                        samme.append(row[0])
                n_list +=1
            if len(samme) == 0:
                self.root.ids.tr.add_widget(OneLineListItem(text=not_found,theme_text_color= 'Custom', text_color='orange'))

_mditapp_().run()