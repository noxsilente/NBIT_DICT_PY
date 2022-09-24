from termcolor import colored
import platform
import os
from res import dictionary
from res.dictionary import *  # file .py contenente le dict
ver = '22.3824.2'  # aa.settimanagiorno
s_o = platform.system()
# conteggio elementi in lista
L = list(verb.keys()) + list(adj.keys()) + list(adv.keys()) + list(pron.keys()) + list(conj.keys()) + list(
    subs.keys()) + list(art.keys())
dict_count = str(len(L))
log = '''
**********************************************************************
\t ###########
\t # NB - IT #
\t ###########

##ver. del 24/09/2022
\tAggiunta la modalità grafica

##ver. del 21/09/2022
\tModifiche codice (aggiunta sez. articoli) + pulizia con aggiunta di un modulo supplementare.

##ver. del 20/09/2022
\tCreazione changelog, ri-dimensionamento {ver},  pulizia del codice ed altre aggiunte.

##ver. del 19/09/2022
\tAggiunta possibilità di cercare più parole contemporaneamente.

##ver. del 18/09/2022
\tModifiche codice e creazione della sequenza versione.

'''
# creazione banners
banner_W = long_string = f'''
    ####################################
    # ##   ### ####       ###  ####### #
    #  #  # #   #  #       #      #    #
    #  # #  #   ###   ###  #      #    #
    #  ##   #   #  #       #      #    #
    # ###   ## ####       ###    ###   #
    ####################################
    #NB/IT Dictionary\t\t\tPy3
    Ver. 1 - {ver}\t\t\tS.O.: {s_o}
    Dict. Ver. {d_ver}\t\t\t{dict_count} parole
    \n\n[-S] MENU CARATTERI SPECIALI\n[-h] AIUTO\n[-E] ESCI\n\n
    '''


def banner_L():  # banner and menu per terminale linux (o PS) #righe
    print('####################################')  # 1
    print('# ', end='')  # 2
    print(colored('##   ', 'red'), end='')
    print(colored('##', 'blue'), end='')
    print(colored('# ####   ', 'red'), end='')
    print(colored('    ##', 'green'), end='')
    print('#  ###', end='')
    print(colored('#### ', 'red'), end='')
    print('#')
    print('# ', end='')  # 3
    print(colored(' #  # ', 'red'), end='')
    print(colored('# ', 'blue'), end='')
    print(colored('  #  #  ', 'red'), end='')
    print(colored('     #', 'green'), end='')
    print('      ', end='')
    print(colored('#    ', 'red'), end='')
    print('#')
    print('# ', end='')  # 4
    print(colored(' # #  #   ###   ', 'blue'), end='')
    print('###', end='')
    print(colored('  #', 'green'), end='')
    print('      ', end='')
    print(colored('#    ', 'red'), end='')
    print('#')
    print('# ', end='')  # 5
    print(colored(' ##  ', 'red'), end='')
    print(colored(' #  ', 'blue'), end='')
    print(colored(' #  #  ', 'red'), end='')
    print(colored('     #', 'green'), end='')
    print('      ', end='')
    print(colored('#    ', 'red'), end='')
    print('#')
    print('# ', end='')  # 6
    print(colored('###  ', 'red'), end='')
    print(colored(' #', 'blue'), end='')
    print(colored('# ####   ', 'red'), end='')
    print(colored('    ##', 'green'), end='')
    print('#    #', end='')
    print(colored('##   ', 'red'), end='')
    print('#')
    print('####################################\nNB/IT Dictionary\t\tPy3')  # 7-8
    print(colored(f'Ver. 1 - {ver}\nDict. Ver. {d_ver}', 'white', attrs=['underline', 'bold']))
    print(colored(f'\n{s_o} System', 'white', attrs=['underline']), end='')
    print(colored(f'\t {dict_count} parole\n', 'yellow', attrs=['bold', 'blink']))
    print(colored('\n[-S/-s] MENU CARATTERI SPECIALI\n[-h] MENU AIUTO\n[-E/-e] ESCI', 'green', attrs=['bold']))


# menu per l'aiuto
def help_menu(args=''):
    os.system('clear') if (platform.system() == 'Linux') else os.system('cls')
    if args == '--complete':
        from res.NBIT_Module import _verbs_
        print(help(NB_IT))
        print(help(_verbs_))
    if args == '--linux':
        banner_L()
        return
    if args == '--win':
        print(banner_W)
        return ''
    if args == '--log':
        os.system('clear') if (platform.system() == 'Linux') else os.system('cls')
        print(log)
        print(dictionary.log())
        input('\nPremi invio per continuare...')
        os.system('clear') if (platform.system() == 'Linux') else os.system('cls')
        return

    print('''Inserire la parola da tradurre. \nVerrà tradotto in automatico da Norvegese ad Italiano e da Italiano a Norvegese.
Se sono più parole, è necessario dividerle con ', '
Guida ai verbi:\nPer cercare un verbo, bisogna inserire il verbo nella forma infinita (senza å).

\nLista comandi disponibili:

-g:\tVersione grafica.
-e/-E:\tEsci dall\'applicazione.
-s/-S:\tMostra i caratteri speciali. \n\tSu Android è possibile usare i caratteri già presenti nella tastiera.
-h:\tMostra il menù dei comandi:
\t--complete: Mostra le definizioni nel codice
\t--log: mostra i changelog
\n-b/-B:\tMostra il banner:
\t--linux: Banner colorato (funziona anche su PowerShell ma non su Prompt CMD)
\t--win: Banner semplice
\ncls:\tPulisci lo schermo
\nPer Windows è possibile vedere i colori facendo partire lo script su PowerShell.
Molte funzionalità non sono disponibili se si fa partire lo script tramite IDLE Python\n
''')


from res.NBIT_Module import NB_IT


# check the system
if s_o == 'Windows':
    print(banner_W)
    #g_ver(g_l)
    #exec('gui')
elif s_o == 'Linux':
    banner_L()

while True:
    dic_str_list_counter = 0  # reset del contatore per la dic_str_list
    word = input('\n[NB - IT] >> ')
    if word[:1] == '-':
        NB_IT(word)
    else:
        for i in (word.split(', ')):
            NB_IT(i)
