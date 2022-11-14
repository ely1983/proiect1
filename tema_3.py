# Ex 1.
note_muzicale = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO']
# afisam lista
print(note_muzicale)

# Inverseaza ordinea folosind slicing si suprascrie aceasta lista

print(note_muzicale[::-1])

note_muzicale[:] = note_muzicale[::-1]
print(note_muzicale)

note_muzicale[::-1] = note_muzicale[::]
print(note_muzicale)

# Ex 2.
# De cate ori apare ‘do’?
print(note_muzicale.count('DO'))

# Ex 3.
# Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista

lista_1 = ['3','1','0','2']
lista_2= ['6','5','4',]

list_1 = lista_1 + lista_2
print(list_1)

lista_1.extend(lista_2)
print(lista_1)


# Ex 4.
# Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

lista_1.sort()
print(lista_1)
lista_1.pop(0)
print(lista_1)

# Ex 5.
# Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala

lista_1 = ['3', '1', '0', '2', '6', '5', '4']
lista_goala = []
if lista_1 == lista_goala:
    print('lista este goala')
else:
    print('lista nu este goala')


# Ex 6.
# Folositi o functie care sa stearga lista de la ex3.

lista_1.clear()
print(lista_1)


# Ex 7.
# Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala

if lista_1 == lista_goala:
    print('lista este goala')
else:
    print('lista nu este goala')

# Ex 8.
# Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

note_elevi = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(note_elevi.keys())

# Ex. 9
# Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

print(note_elevi['Ana'])
print(note_elevi['Gigel'])
print(note_elevi['Dorel'])


# Ex 10.
# Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

note_elevi['Dorel'] = 6
print(note_elevi['Dorel'])

# Ex 11.
# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

note_elevi.pop('Gigel' )
print(note_elevi)

note_elevi['Ionica'] = 9
print(note_elevi)

# Ex 12.
# zile_sapt =  , 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt = {'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

# Ex 13.
# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt


if weekend == zile_sapt:
    print(f'{weekend} este un subset al zilelor din sapt')
else:
    print(f'{weekend} nu este un subset al zilelor din sapt')


