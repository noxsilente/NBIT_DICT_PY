        ###################################
        ## å = ALT + 134 | ø = ALT + 155 ##
        ## Å = ALT + 143 | Ø = ALT + 157 ##
        ## æ = ALT + 145 | ö = ALT + 148 ##
        ## Æ = ALT + 146 | Ö = ALT + 153 ##
        ###################################

d_ver = '22.3823' # aa.settimanagiorno
def log():
	print( '''	
**********************************************************************
\t##############
\t# Dictionary #
\t##############

##ver. del 22/09/2022
\tAggiunta altri vocaboli.

##ver. del 22/09/2022
\tAggiunta altri vocaboli.

##ver. del 21/09/2022
\tAggiunta della 'dict' articoli ed altri vocaboli.

## ver. del 20/09/2022            
\tModifica codice versione e creazione changelog.

##ver. del 19/09/2022
\tAggiunta parole + ordine alfabetico.
**********************************************************************
'''
)

verb = {
    'arbeide' : ['lavorare', 'arbeider', 'har arbeidet', 'arbeidet', 'vil arbeide', 'arbeid'],
    'bære' : ['portare', 'bærer', 'har båret', 'bar', 'vil bære', 'bær'],
    'begynne' : ['iniziare', 'begynner', 'har begynt', 'begynt', 'vil begynne', 'begyn'],
    'bestille' : ['ordinare', 'bestiller', 'har bestilt', 'bestilte', 'vil bestille', 'bestill'],
    'bety' : ['significare', 'betyr', 'har betydd', 'betydde/betød', 'vil bety', 'bety'],
    'bo' : ['vivere', 'bor', 'har bodd', 'bodde', 'vil bo', 'bo'],
    'burde' : ['dovere', 'bør', 'har burdet', 'burde', 'vil burde', 'burd'],
    'dra' : ['andare', 'drar', 'har dratt/dradd', 'dro', 'vil dra', 'dra'],
    'drikke' : ['bere', 'drikker', 'har drukket', 'drakk', 'vil drikke', 'drikk'],
    'få' : ['ricevere', 'får', 'har fått', 'fikk','vil få', 'få'],
    'finne' :['trovare', 'finner','har funnet', 'fant', 'vil finne', 'finn'],
    'fly' : ['volare', 'flyr', 'har flydd', 'flydde', 'vil fly', 'fly'],
    'foretrekker' : ['preferire', 'foretrekker', 'har foretrukket', 'foretrakk', 'vil foretrekke', 'foretrekk'],
    'forstå' : ['capire', 'forstår', 'har forstått', 'forstod', 'vil forstå', 'forstå'],
    'fortelle' : ['raccontare', 'forteller', 'har fortalt', 'fortalte', 'vil fortelle', 'fortell'],
    'gå' : ['andare', 'går', 'har gått', 'gikk', 'vil gå', 'gå'],
    'ha' : ['avere', 'har', 'har hatt', 'hadde', 'vil ha', 'ha'],
    'være' : ['essere', 'er', 'har vært', 'var', 'vil være', 'vær'] 
    }

adj = {
    'dårlig' : 'cattivo',
    'fattig' : 'povero',
    'feil' : ['errore', 'sbaglio', 'sbagliato'],
    'fort' : ['rapido', 'forte'],
    'første' : 'primo',
    'frisk' : 'sano',
    'gammel' : 'vecchio',
    'glad': ['allegro', 'felice'],
    'god' : 'buono',
    'høy' : 'alto',
    'hurtig' : 'veloce',
    'lang' : 'lungo',
    'langsom' : 'lento',
    'lav' : 'basso',
    'liten' : 'piccolo',
    'lykkelig' : 'felice',
    'ny' : 'nuovo',
    'rik' : 'ricco',
    'syk' : 'malato',
    'sist' : 'ultimo',
    'stor' : 'grande',
    'kort' : 'corto',
    'ung' : 'giovane'
    }

adv = {
    'aldri' : 'mai',
    'altfor': 'troppo',
    'av og til' : 'a volte',
    'bare' : 'solo',
    'bak' : 'dietro',
    'bra' : 'bene',
    'der' : 'lì',
    'dit' : 'lì',
    'etterpå' : 'dopo',
    'for' : 'troppo',
    'foran' : 'davanti',
    'fort' : ['rapidamente', 'velocemente'], 
    'fortid' : 'passato',
    'fremtid' : 'futuro',
    'her' : 'qui',
    'hit' : 'qui',
    'høyre' : 'destra',
    'hvor' : 'dove',
    'inne' : ['dentro', 'nel'],
    'igjen' : 'ancora',
    'ingen' : ['niente', 'nessuno'],
    'ingeting' : 'niente',
    'ja' : 'sì',
    'langsomt' : 'lentamente',
    'langt' : 'lontano',
    'nå' : ['ora', 'adesso'],
    'nåtiden' : 'presente',
    'nær' : ['vicino', 'accanto'],
    'nei' : 'no',
    'midnatt' : 'mezzanotte',
    'midt' : ['mezzo', 'centro'],
    'noen ganger' : 'a volte',
    'ofte' : 'spesso',
    'over' : 'sopra',
    'overalt' : 'ovunque',
    'sammen' : 'insieme',
    'senere' : ['più tardi', 'dopo'],
    'sjelden' : 'raramente',
    'veldig' : ['veramente', 'davvero'],
    'venstre' : 'sinistra'
    }
pron = {
    'de' : ['essi', 'loro', 'quelli', 'quelle'],
    'den' : ['quei', 'quelle'],
    'denne' : ['questo', 'questa'],
    'dere' : 'voi',
    'deres' : 'loro',  
    'det' : [ 'esso', 'essa', 'quei', 'quelle', '(n)'],
    'dette' : ['questo', 'questa', '(n)'],
    'disse' : ['questi', 'queste'],
    'du' : 'tu',
    'han' : 'lui',
    'hans': 'il suo',
    'hennes' : 'la sua',
    'hun' : 'lei',
    'hva' : 'cosa',
    'hvem' : 'chi',
    'jeg' : 'io',
    'mi' : 'mia',
    'min' : 'mio',
    'mine' : 'mie',
    'mitt' : ['mio', 'mia', '(n)'],
    'seg' : 'si',
    'som' : ['che', 'il quale'],
    'vår' : ['nostro', 'nostra'],
    'vårt' : ['nostro', 'nostra', '(n)'],
    'våre' : 'nostre',
    'vi' : 'noi'
    }
conj = {
    'at' : 'che',
    'eller' : ['oppure', 'o'],
    'for' : 'per',
    'ikke' : 'non',
    'men' : 'ma',
    'og' : 'e',
    'så' : 'così'
    }
subs = {
    'arm' : 'braccio',
    'armen' : 'il braccio',
    'baby' : ['bambino', 'bambina'],
    'babyen' : ['il bambino', 'la bambina'],
    'barn' : ['ragazzino', 'ragazzina'],
    'barnet' : ['il ragazzino', 'la ragazzina'],
    'barna' : ['i ragazzi', 'le ragazze'],
    'bein' : 'gamba',
    'beina' : 'le gambe',
    'bil' : ['auto', 'macchina'],
    'bilen' : 'l\'auto',
    'biler' : 'auto',
    'bilene' : 'le auto',
    'bok' : 'libro',
    'boka': 'il libro',
    'boken' : 'il libro',
    'bøkene' : 'i libri',
    'bøker' : 'libri',
    'bro' : 'ponte',
    'broen' : 'il ponte',
    'hest' : 'cavallo',
    'hesten' : 'il cavallo',
    'hestene' : 'i cavalli',
    'hester' : 'cavalli',
    'hjert' : 'cuore',
    'hjertet' : 'il cuore',
    'hund' : 'cane',
    'hunden' : 'il cane',
    'hundene' : 'i cani',
    'hunder': 'cani',
    'gutt' : 'ragazzo',
    'gutten' : 'il ragazzo',
    'guttene' : 'i ragazzi',
    'gutter' : 'ragazzi',
    'jenta' : 'la ragazza',
    'jente' : 'ragazza',
    'jentene' : 'le ragazze',
    'jenter' : 'ragazze',
    'kropp' : 'corpo',
    'ku' : 'mucca',
    'kvinne' : 'donna',
    'kvinnen' : 'la donna',
    'kvinnene' : 'le donne',
    'kvinner' : 'donne',
    'kyr': 'mucche',
    'mann' : 'uomo',
    'mannen' : 'l\'uomo',
    'menn' : 'uomini',
    'mennene' : 'gli uomini',
    'maskine' : 'macchina',
    'maskinen' : 'la macchina',
    'sand' : 'sabbia',
    'strand' : 'spiaggia',
    'stranda' : 'la spiaggia',
    'strendene' : 'le spiaggie',
    'vann' : 'acqua',
    'vannet' : 'l\'acqua'
    }
art = {
	'av' : 'di',
	'ei' : 'una',
	'en' : ['un', 'uno', 'una'],
	'et' : ['un', 'uno', 'una', '(n)'],
	'i' : ['in', 'nel'],
	'med' : 'con',
	'mellom' : 'tra',
	'på' : ['su', 'sopra']
	}
