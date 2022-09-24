#import tkinter
from tkinter import *
import tkinter as tk
import platform
#from res.dictionary import d_ver
from functools import partial
from res.dictionary import *
dic_list = [adv, adj, pron, conj, subs, art]
dic_str_list = ['avv.', 'agg.', 'pron.', 'cong.', 'sost.', 'art.']
vtemp_list = ['infinito >> ', 'presente: ', 'pass. prossimo: ', 'passato: ', 'futuro: ', 'imperativo: ']
temp_str = '' # stringa temporanea allegata alla lista dic_str_list
ver = '1.1741'
main_label = f'''
    NB_IT GUI ver. : {ver}\nDictionary ver.:  {d_ver}
    \nPiattaforma: {platform.system()}\n
    '''
def ex_():
    window.destroy
    return exit()
def _verbs_(word):
    '''
    Creazione di un parametro a parte esclusivo per la ricerca dei verbi
    '''
    k_list = list(verb.keys())
    v_list = list(verb.values())
    temp_list = []
    temp_str = 'verbo'
    if word in verb.keys():
            temp_v_list =  list(verb.get(word))
            if type(verb.get(word)) == list: # se verbo, dà la traduzione + coniugazione
                for i in range(len(vtemp_list)):
                    temp_list.append('\n'+ vtemp_list[i]+ '  ' + temp_v_list[i])
                g_ver(temp_list)
            else:
                g_ver('[>>] \n' + verb.get(word) + f' ({temp_str})')
    else:
        for i in range(len(v_list)):
            if word == v_list[i]:
                 g_ver('\nIT - NB >> '+ k_list[i] + f' ({temp_str})\n')
            if type(v_list[i])==list: # se la value è una lista (in teoria dovranno essere tutte lista)
                x = 0   # assegno int per trovare l'index di vtemp_list
                for j in v_list[i]:
                    x+= 1
                    if word == j:
                        g_ver(f' \n>> {vtemp_list[x-1]}  {k_list[i]} ({temp_str})')
                                            # x-1 per quadrare i conti :)

def NB_IT(word):
    _verbs_(word)#primo controllo nella sez verbi
    dic_str_list_counter = 0 # contatore collegato alla lista dic_str_list
    for dic in dic_list:
        temp_str = dic_str_list[dic_str_list_counter]
        k_list = list(dic.keys())       # creazione di liste temporanee
        v_list = list(dic.values())     # per un handling più semplice
        for w in range(len(dic.keys())): # per ogni valore in un determinato dizionario si cerca la parola,
            if word == k_list[w]:        # se c'è ed è una lista, mostra i valori in lista, altrimenti solo la traduzione
                if type(v_list[w]) == list:
                    g_ver('\n>>>  ' + ', '.join(v_list[w]) + f' ({temp_str})\n')
                else:
                    g_ver('\n>>>> '+ v_list[w] + f' ({temp_str})\n')
        for w in range(len(dic.values())): # per ogni valore tra le values
            if word in v_list[w] and (type(v_list[w]) == list) or (word == v_list[w]):# se è una lista, mostra la chiave corrispondente ...
                    g_ver(f'\nIT - NB: {word} \n>>>> '+ k_list[w] + f' ({temp_str})\n')
##                else:
##                 	print(colored('\n [X] Parola non presente', 'red'))
##                 	return
        dic_str_list_counter += 1

def next(w):
    word = (w.get())
    if word[:1] == '-':
        NB_IT(word)
    else:
        for i in (word.split(', ')):
            NB_IT(i)

def g_ver(g_l):
    found_word.place(x=0, y=430)
    found_word.config(text="")
    found_word.config(text=g_l, justify='left')

window = tk.Tk()
window.geometry('400x600+100+200')
window.title("NB - IT Dictionary")
text = tk.StringVar()
bg = PhotoImage(file="res/NBIT.png")
background = Label(window, image=bg).place(x=100, y=0)
word_i = tk.Entry(window, textvariable=text).place(x=30, y=400)
exit_button = tk.Button(text="Esci", command=ex_).place(x=350, y=450)
ver_label = tk.Label(window, text=main_label).place(x=0, y=250)
useless_label = tk.Label(window, text=">>").place(x=0, y=400)
found_word = tk.Label(window, text='')#.place(x=0, y=430,bordermode='inside')
found_word.pack()
next = partial(next, text)
search_button = tk.Button(text="Cerca", command=next).place(x=150, y=400)
window.mainloop()


