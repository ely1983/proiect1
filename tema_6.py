#Ex nr 1.
# Clasa Cerc
# Atribute: raza, culoare

# Constructor pt ambele atribute

# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    pi = 3.14

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print('raza cerc', self.raza, 'si are culoarea', self.culoare)

    def aria(self):
        return float(self.pi) * int(self.raza) ** 2

    def diametru(self):
        return 2 * int(self.raza)

    def circumferinta(self):
        return 2 * float(self.pi) * int(self.raza)


cerc1 = Cerc('8', 'galben')
cerc1.descriere_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())


# Ex nr 2.
# class dreptunghi
# Atribute: lungime, latime, culoare

# Constructor pt toate atributele

# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latimea = latime
        self.culoare = culoare

    def descriere(self):
        print('dreptunghiul are lungimea', self.lungime, ' are latimea', self.latimea, 'si are culoarea', self.culoare)

    def aria(self):
        return int(self.lungime) * int(self.latimea)

    def perimetru(self):
        return 2 * int(self.lungime) * 2 * int(self.latimea)

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua


dreptunghi1 = Dreptunghi('4', '8', 'rosu')
dreptunghi1.descriere()
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoarea('roz')
dreptunghi1.descriere()


# Ex nr 3.
# Clasa Angajat

# Atribute: nume, pre
# nume, salariu

# Constructor pt toate atributele

# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat:
    nume_prenume = 'chiciuc elisabeta'
    salariu_lunar = '1500'
    salariu_anual = '18000'
    marire_salariu = '10%'

    def descriere(self):
        print(f'Ma numesc', self.nume_prenume, 'castig pe luna', self.salariu_lunar,
              ' castig pe an', self.salariu_anual, 'si vreau o marire ', self.marire_salariu)

    def __init__(self, nume_prenume, salariu_lunar, salariu_anual, marire_salariu):
        self.nume_prenume = nume_prenume
        self.salariu_lunar = salariu_lunar
        self.salariu_anual = salariu_anual
        self.marire_salariu = marire_salariu


persoana1 = Angajat('chiciuc elisabeta', '1500', '18000', '10%')
print(persoana1.nume_prenume)
persoana1.descriere()


# Ex nr 4.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma

class Cont_bancar:
    def __init__(self, titular, iban):
        self. titular = titular
        self. iban = iban
        self. sold = 0


    def interogare_sold (self):
        print(f'titular {self. titular}')
        print(f'iban {self. iban}')
        print(f'sold {self. sold}')


    def alimentare_cont (self, suma):
        self. sold += suma
        print(f'ati alimentat {suma}')
        print(f'aveti in cont {self. sold}')

    def debitare_cont (self, suma):
        if suma <= self.sold:
            self.sold -= suma
            print(f'ati cheltuit {suma}')
            print(f'aveti in cont {self. sold}')
        else:
            print('fonduri insuficiente')


cont1 = Cont_bancar ('chiciuc elisabeta',  'RO40INGB000')

cont1.interogare_sold()

cont1.alimentare_cont(1000)

cont1.debitare_cont(1500)
