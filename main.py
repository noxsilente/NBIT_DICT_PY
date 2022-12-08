'''
Alpha version:
0.4 build 18
Requirements for build the app with !buildozer:
# buildozer.spec (all specifications are already inserted, need only to change the version)
# dictionary.py - handmade dictionary using python dicties
# main.py - main script with all the defs
# build.kv - part with kv script (for app layout)
# dict.db - downloaded words translated using 'translator_alpha.py'
# langs.db - language references
# NBIT.png - Splash Screen image
# innb.jpg - App background
# icon-png - icon for the app
'''
########        IMPORTING LIBRARIES
import sqlite3
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import Snackbar
from dictionary import *
############################################ MODIFICATION  ########
conn = sqlite3.connect('res/dict.db') # COMMENT BEFORE BUILD APP  #
# conn = sqlite3.connect('dict.db')  # UNCOMMENT BEFORE BUILD APP #
langs = sqlite3.connect('langs.db')                               #
###################################################################
# Inizializing the database
l_curs= langs.cursor()
curs = conn.cursor()
#######################################################
# Trying to create all the tables
# If already exist, I get all the words in them appending in a list
# then I count its length
try:
    curs.execute('CREATE TABLE verbi (it text, no text)')
    curs.execute('CREATE TABLE adv (it text, no text)')
    curs.execute('CREATE TABLE adj (it text, no text)')
    curs.execute('CREATE TABLE subs (it, text, no text)')
    curs.execute('CREATE TABLE varie (it text, no text)')
except:
    y = 0
    lista = ['adv', 'adj', 'subs', 'varie', 'verbi']
    present = []
    for i in lista:
        for row in curs.execute(f'SELECT * FROM {i}'):
            y = y+len(row)
# Declaring lists
dic_list = [adv, adj, pron, conj, subs, art]
db_list = ['avv.', 'agg.', 'sost.', '', 'verbo']
dic_str_list = ['avv.', 'agg.', 'pron.', 'cong.', 'sost.', 'art.']
vtemp_list = ['infinito >> ', 'presente: ', 'pass. prossimo: ', 'passato: ', 'futuro: ', 'imperativo: ']
temp_str = '' # temporary string for  dic_str_list
temp_list = []
# Counting the total number of the words in dictionary.py
l=0
for i in dic_list:
    L=len(i.keys())+len(i.values())
    l=l+L
L= len(verb.keys())+ len(verb.values())
l=l+L
############################################ other variables
lang='it'
not_found= ''
#######################################################################
class pal_dial(BoxLayout):
    '''
    Class for the palette dialog box
    '''
    pass

class _mditapp_(MDApp):
    '''
    Main class
    '''
    def build(self):
        '''
        Building app.
        Configuration of theme and palette getting variables from the database
        '''
        global theme, palette
        for row in l_curs.execute(f'SELECT it FROM langs WHERE id=\'theme\''):
            theme = row[0]
        for row in l_curs.execute(f'SELECT no FROM langs WHERE id=\'theme\''):
            palette = row[0]
        self.theme_cls.theme_style=theme
        self.theme_cls.primary_palette=palette
        self.theme_cls.primary_hue= '900'
        self.load_kv('build.kv')

    def on_start(self,lang=lang):
        '''
        Getting other variables from the database.
        Actually, standard language is IT but, everytime the language is changed
        it returns here with selected language from the database.
        Example:
            The user choose 'NO' language.
            It returns here (on_start) with parameter lang=no
            All the texts are replaced getting the specific id from the specific table
        '''
        global theme, not_found, dictionary, database
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'search\''):
            self.root.ids.input.hint_text = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'dictionary\''):
            dictionary = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'database\''):
            database = row[0]
        for row in l_curs.execute(f'SELECT {lang} FROM langs WHERE id=\'not_found\''):
            not_found= row[0]
        self.icon='icon.ico'
    def on_close(self):
        exit()
    def lang(self):
        '''
        Simple function for change the app language.
        > It's possible to add it directly in the function 'on_start'
        '''
        global lang
        if lang == 'it':
            lang= 'no'
        else:
            lang = 'it'
        self.on_start(lang)

    def dialog_open(self):
        '''
        Function called for open the info dialog box
        {l}: total words in 'dictionary.py'
        {y}: total words in 'dict.db'
        '''
        global dictionary, database
        self.dialog = MDDialog(
            title='info',
            type='simple',
            text=f'''            
        [{l}] {dictionary}

        [{y}] {database}

        Python 3.10.6 
             - Kivy 2.1.0
             - Kivymd 1.0.2
             - sqlite3

        E-MAIL: 
            andrewdm91@gmail.com

        Ver. 0.4
        '''
        )
        self.dialog.open()
    def theme(self,switch):
        '''
        This function have two inner parts.
        From the 'build.kv' the function is called by a button with a relative 'switch'
        Cause of an error occurred in the app (need to build it with a recent version of Python,
        where exists the switch-case statement)

        if the id is called from the button 'theme-light-dark':
            if there's a theme, it changes in the other one and commit the parameter in the database
        if the id is called from the button 'palette':
            it opens the palette dialog where the user can choose the primary_palette color.
            Commit the variable in the database and close the dialog after pressing button 'OK'
        '''
        global theme, palette, lang
        def pal_cng(palette):
            '''
            variable 'palette' is taken from the button created during the dialog construction
            '''
            l_curs.execute(f'UPDATE langs SET no=\'{palette}\' WHERE id= \'theme\'')
            langs.commit()
            self.theme_cls.primary_palette = palette
            self.theme_cls.primary_hue = '900' # Darkest hue.. it goes from '50' to '900' and from 'A50' to 'A700'
        if switch == 1:
            if theme == 'Dark':
                theme = 'Light'
            else:
                theme = 'Dark'
            l_curs.execute(f'UPDATE langs SET it=\'{theme}\' WHERE id= \'theme\'')
            langs.commit()
            self.theme_cls.theme_style=theme
        elif switch == 2:
            # Creating two lists:
            #   '_palette_' for the palette to choose
            #   'theme_list' for colouring the dialog icons
            _palette_ = ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue',
                       'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
                       'Brown', 'Gray', 'BlueGray']
            theme_list = ['#ff0000', '#ffc0cb', '#800080', '#4d004d', '#4b0082', '#0000ff', '#add8e6',
                          '#00ffff', '#008080', '#008000', '#90ee90', '#00ff00', '#ffff00', '#ff9900', '#ffa500',
                          '#d5760d','#a52a2a', '#808080', '#6b8d94']
            # Issues with size_hint_x
            self.PD=MDDialog(
                title='Palette',
                type='custom',
                size_hint_x= '.3',
                overlay_color= [0,0,0,.5],
                content_cls=pal_dial(),
                buttons=[
                    (MDFlatButton(
                    text='OK',
                    on_release=lambda x: self.PD.dismiss()
                ))
                ]
            )
            # every button is created getting the index of the previous lists
            for i in range(len(_palette_)):
                self.PD.content_cls.ids.tr_.add_widget(MDIconButton(size_hint_x='1',icon='palette', theme_icon_color='Custom', icon_color=theme_list[i], on_release=lambda x, pal=_palette_[i]: pal_cng(pal)))
            self.PD.open()
    def src(self, word):
        '''
        This function permits the user to fin the word to translate.
        With 'on_text: app.src(self.text)' in the TextField (MDTextField in 'build.kv')
        the user can search in real time the word, without the needing of a button (so, no other objects to handle)

        While a word is digitized in the app we have different steps before to give a/some result/s
            if word is not an empty string:
                First, the widgets in the list (MDList with id 'tr'), are cleared.
                    This allows to search everytime a new word without add useless items in the list
                A list 'samme' is created. Then a list containing all the keys
                and another containing all the values taken from dictionaries in 'dictionary.py'

                    If the word is in the key list the corresponding value is added to the list 'samme' and a OneLineListItem is created and added to the list
                        If the value is a list, all elements of the list are added to a different list item
                    Same if the word is in the value list, getting the corresponding key and adding it to the list
                    With all the words, in the OneLineListItem text is added also the class (noun, pronoun, adverb ecc...)
        ('samme' list serves to avoid a duplication of the translation)

                If the word is not found in the dicties, is the time to scanning the database.
                    If the word has a correspondence, the relative value is added (for it>>no or no>>it)
                    To the OneLineListItem is added also the table relative to the word class (noun, pronoun, adverb ecc...)
        '''
        global not_found
        #word = str(self.root.ids.input.text)
        if word == '':
            self.root.ids.tr.clear_widgets()
        else:
        #self.root.ids.srcd.text = word
            self.root.ids.tr.clear_widgets()
            samme = []
            dic_str_list_counter = 0
            k_list = list(verb.keys())
            v_list = list(verb.values())
            temp_str = 'verbo'
            if word in verb.keys():
                # First, the word is searched in the verb dictionary
                temp_v_list = list(verb.get(word))
                if type(verb.get(word)) == list:  # if it is a verb, it returns translation + conjugation
                    for i in range(len(vtemp_list)):
                        #print(vtemp_list[i] + '  ' + temp_v_list[i])
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'{vtemp_list[i]} {temp_v_list[i]}',
                                                                            on_release= lambda x, word=temp_v_list[i]: [Clipboard.copy(word), Snackbar(text=f'\'{word}\' Copiato').open()]))
                        samme.append(i)
                else: # This particular case is if the verb doesn't have a conjugation
                    print('[>>] \n' + word + ' : ' + verb.get(word) + f' ({temp_str})')
            else:
                for i in range(len(v_list)):
                    # print(f'{v_list[i]} {i} ' + str(type(v_list[i])) ) # debug
                    if word == v_list[i]:
                        print('\nIT - NB >> ' + k_list[i] + f' ({temp_str})\n')
                    if type(v_list[i]) == list:
                        x = 0  # for find the index of vtemp_list
                        for j in v_list[i]:
                            if word == j:
                                # if the word is in the conjugation list it returns the conjugation + translation
                                # It doesn't work for conjugate italian verbs bacause i haven't added them
                                # print(f'{word}  > {j} - {x} ... {vtemp_list[i]}') #debug
                                self.root.ids.tr.add_widget(OneLineListItem(text=f'{word} >> {vtemp_list[x]}  {k_list[i]} ({temp_str})',
                                                                            on_release= lambda x: [Clipboard.copy(word), Snackbar(text=f'\'{word}\' Copiato').open()]))
                                samme.append(word)
                                #print(f' \n{word} >> {vtemp_list[x - 1]}  {k_list[i]} ({temp_str})') # debug
                            x += 1
            for i in dic_list:
                # if the word is not in the verb dictionary it is searched in the other dicts
                temp_str = dic_str_list[dic_str_list_counter]
                k_list = list(i.keys())  # temporary lists
                v_list = list(i.values())  # for an easy handling
                for w in range(len(i.keys())):
                    if word == k_list[w]:
                        if type(v_list[w]) == list:
                            # if the word is in a list it is added to the OneLineListItem using a ',' separating the words
                            self.root.ids.tr.add_widget(OneLineListItem(text=', '.join(v_list[w]) +f'({temp_str})',
                                                                            on_release= lambda x, txt=v_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                            samme.append(', '.join(v_list[w]))
                            # same as above
                        else:
                            self.root.ids.tr.add_widget(OneLineListItem(text=f'{v_list[w]} ({temp_str})',on_release= lambda x, txt=v_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                            samme.append(v_list[w])

                for w in range(len(i.values())):
                    if word in v_list[w] and (type(v_list[w]) == list) or (word == v_list[w]):
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'{k_list[w]} ({temp_str})', on_release= lambda x , txt=k_list[w]: [Clipboard.copy(txt), Snackbar(text=f'\'{txt}\' Copiato').open()]))
                        samme.append(k_list[w])
                dic_str_list_counter +=1
            n_list = 0
            for i in lista:
                for row in curs.execute(f'SELECT no FROM {i} WHERE it=\'{word}\' '):
                   if str(row[0]).lower() in samme:
                       pass # if the word already exists in 'samme' list, it pass not showing a duplication of translation
                   else:
                       self.root.ids.tr.add_widget(OneLineListItem(text=f'[IT-NO] {row[0]} (! {db_list[n_list]})',theme_text_color= 'Custom', text_color='orange'))
                       samme.append(row[0]) # if the word is founded it is appended to the list for other purposes
                for row in curs.execute(f'SELECT it FROM {i} WHERE no=\'{word}\''):
                    if row[0] in samme:
                        pass
                    else:
                        self.root.ids.tr.add_widget(OneLineListItem(text=f'[NO-IT] {row[0]} (! {db_list[n_list]})',theme_text_color= 'Custom', text_color='orange'))
                        samme.append(row[0])
                n_list +=1
            if len(samme) == 0:
                #if no word is founded, no word is added to samme list, so the length of the list will be 0 and the message below is showed
                self.root.ids.tr.add_widget(OneLineListItem(text=not_found,theme_text_color= 'Custom', text_color='red'))

_mditapp_().run()