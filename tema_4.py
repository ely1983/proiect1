# ex nr 1
# Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
# Faceti acelasi lucru cu un for each
# Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin',
          'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in masini:
    print('1. masina mea preferata este' + x)
for x in range(0,len(masini)):
    print('[for] masina mea preferata este' + masini[x])
x = 0
while x >= len(masini) - 1:
    print('[while] masina mea preferata este'+ masini [x])
x+= 1

# Ex nr 2
# Aceeasi lista
# Folositi un for
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
print(masini)

# Ex 3.
# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'Opel']
for i in masini:
    if i == "MERCEDES":
        print('am gasit masina dorita')
        break
    else:
        print(f'am gasit masina dorita{i}. mai cautam')


# Ex 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

for masina in masini:
    if masina == 'TRABANT' or masina == 'LASTUN':
        continue
    else:
        print(f'sar putea sa va placa masina {masina}')



# Ex nr 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'TRABANT' or masini[i] == 'LASTUN':
         masini_vechi.append(masini[i])
         masini[i] = 'TESLA'
print(f'modele vechi: {masini_vechi}')
print(f'modele noi:{masini}')


# ex 6.
#Avand dict

# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100, 'Audi': 19000,'BMW': 23000}
buget = int(input('ce buget aveti pentru masina'))
for masina in pret_masini:
    if buget >= pret_masini[masina]:
        print(f'pentru un buget de {pret_masini[masina]}euro puteti alege masina {masina}')


# Ex 7.
# Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
total=0
for numar in numere:
    if numar == 3:
        total += 1
print(f'numarul 3 apare de {total} ori.')

# Ex nr 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

suma = 0
for numar in numere:
    suma += numar
print(f'suma tuturor elementelor este {suma}.')


# Ex 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

nr_max = 0
for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'cel mai mare numar din lista mea este {nr_max}')


# Ex 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
print(f'noua lista este: {numere}')
