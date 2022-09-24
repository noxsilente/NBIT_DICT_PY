from termcolor import colored
import os
import platform
from res.dictionary import *
dic_list = [adv, adj, pron, conj, subs, art]
dic_str_list = ['avv.', 'agg.', 'pron.', 'cong.', 'sost.', 'art.']
vtemp_list = ['infinito >> ', 'presente: ', 'pass. prossimo: ', 'passato: ', 'futuro: ', 'imperativo: ']
temp_str = '' # stringa temporanea allegata alla lista dic_str_list
def _verbs_(word):
    '''
    Creazione di un parametro a parte esclusivo per la ricerca dei verbi
    '''
    k_list = list(verb.keys())
    v_list = list(verb.values())
    temp_str = 'verbo'
    if word in verb.keys(): 
            temp_v_list =  list(verb.get(word))
            if type(verb.get(word)) == list: # se verbo dà la traduzione + conuìiugazione
                for i in range(len(vtemp_list)):
                    print(vtemp_list[i]+ '  ' + temp_v_list[i])
                    g_l = (vtemp_list[i]+ '  ' + temp_v_list[i])
            else:
                print('[>>] \n' + word + ' : '+ verb.get(word) + f' ({temp_str})')
    else:
        for i in range(len(v_list)):
            #print(f'{v_list[i]} {i} ' + str(type(v_list[i])) )
            if word == v_list[i]:
                 print('\nIT - NB >> '+ k_list[i] + f' ({temp_str})\n')
            if type(v_list[i])==list: # se la value è una lista (in teoria dovranno essere tutte lista)
                x = 0   # assegno int per trovare l'index di vtemp_list
                for j in v_list[i]:
                    x+= 1
                    if word == j:
                        #print(f'{word}  > {j} - {x} ... {vtemp_list[i]}')
                        print(f' \n{word} >> {vtemp_list[x-1]}  {k_list[i]} ({temp_str})')
                                            # x-1 per quadrare i conti :)

def NB_IT(word):
    '''
    Ritorna la traduzione di una parola ricevuta come input:
    word = input('\nNB - IT >> ')
    '''
    if word == '-E' or word == '-e':
        exit()
    elif word == '-S' or word == '-s':
        print('\nCopia caratteri speciali: \nå Å \næ Æ \nö Ö \nø Ø')
    elif word == 'cls':
        os.system('clear') if (platform.system() == 'Linux') else os.system('cls')
        print(colored ('\n[-S/-s] MENU CARATTERI SPECIALI\n[-h] MENU AIUTO\n[-E/-e] EXIT', 'grey', attrs=['bold']))
    elif word[:2] == '-h' or word[:2] == '-b' or word[:2] == '-B':
        args = word[3::]
        from NBIT_Dict import help_menu
        help_menu(args)
    elif word == '-g':
        os.system('python res/gui.py')
        exit()
    elif word != '':
        _verbs_(word)#primo controllo nella sez verbi
        dic_str_list_counter = 0 # contatore collegato alla lista dic_str_list
        for dic in dic_list:
            temp_str = dic_str_list[dic_str_list_counter]
            k_list = list(dic.keys())       # creazione di liste temporanee 
            v_list = list(dic.values())     # per un handling più semplice
            for w in range(len(dic.keys())): # per ogni valore in un determinato dizionario si cerca la parola,
                if word == k_list[w]:        # se c'è ed è una lista, mostra i valori in lista, altrimenti solo la traduzione 
                    if type(v_list[w]) == list:
                        print(f'{word}\n>>>  ' + ', '.join(v_list[w]) + f' ({temp_str})\n')
                    else:
                        print(f'\n{word}\n>>>> '+ v_list[w] + f' ({temp_str})\n')
            for w in range(len(dic.values())): # per ogni valore tra le values
                if word in v_list[w] and (type(v_list[w]) == list) or (word == v_list[w]):# se è una lista, mostra la chiave corrispondente ... 
                        print(f'\nIT - NB: {word} \n>>>> '+ k_list[w] + f' ({temp_str})\n')
##                else:
##                 	print(colored('\n [X] Parola non presente', 'red'))
##                 	return                  
            dic_str_list_counter += 1
