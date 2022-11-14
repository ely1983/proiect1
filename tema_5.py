import math
# Ex nr 1.
# Functie care sa calculeze si sa returneze suma a 2 numere
def func_cu_2_params(a, b):
    print(f'suma este {a+b}')


func_cu_2_params("5", "6")
func_cu_2_params(5, 6)

# Ex nr 2.
# Functie care sa returneze TRUE daca un numar este par, FALSE pt impar


def verificare_numere(par):
    if par % 2 == 0:
        return True
    else:
        return False


print(verificare_numere(6))

# Ex 3.
# Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

def print_Greeting_By_Name(nume,prenume):

    print(f'numele meu este {nume} {prenume}')
    print_Greeting_By_Name('Chiciuc', 'Elisabeta')


print(len('Chiciuc''Elisabeta'))

# Ex.4
# Functie care returneaza aria dreptunghiului

def aria_triunghiului(lungime,latime):

    aria_triunghiului = lungime * latime
    return aria_triunghiului


a = aria_triunghiului(4, 5)
print(a)

# Ex 5.
# Functie care returneaza aria cercului


def aria_cerc(r):
    aria = math.pi * r ** 2
    return aria


x = aria_cerc(8)
print(x)

# Ex 6.
# Functie care returneaza True daca un caracter x se gaseste intr-un string dat.
# Fasle daca nu

def my_function(a,string):

    for i in range(len(string)):
        if a == string[i]:
            return True
        else:
            return False


x = my_function("a", "alfabet")
print(x)

# Ex 7.
# Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y


def string_test(caractere):
    x = {'upper_chase': 0, 'lower_case': 0}
    for y in caractere:

         if y.isupper():
             x['upper_chase'] += 1

         elif y.islower():
             x['lower_case'] += 1

         else:
             pass

    print(f'original string', caractere)
    print('number of upper case alfabets:', x['upper_chase'])
    print('numberof lower case alfabets:', x['lower_case'])


string_test('masina CASA masa APARTAMENT')


# Ex nr 8:
# Functie care primeste o LISTA de numere si returneaza o LISTA
# doar cu numerele pozitive:


list1 = [-1, 5, -8, 4, 9, 3, -2, -8]
def pozitiv_negativ(my_list):
    pozitv_list = []
    negativ_list = []
    for numere in my_list:
        if numere > 0:
            pozitv_list.append(numere)
        else:
            negativ_list.append(numere)
    print('pozitiv_list=', pozitv_list)
    print('negativ_list=', negativ_list)


pozitiv_negativ(list1)


# Ex 9.
# Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.


def cu_2_parametri(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x


verificare = cu_2_parametri(5, 3)
print(verificare)

# Ex 10.
# Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

def add_to_set(x,y):
    if x not in y:
        y.add(x)
        print('am adaugat numarul', x, 'in setul', y)
        return True
    else:
         print('nu am adaugat numarul', x, 'in setul', y, 'acesta exista deja')
         return False

z = add_to_set(5, {8,9,4,3})
print('valoarea afirmatiei este', z)

