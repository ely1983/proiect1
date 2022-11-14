# if se cere o conditie daca este True se duce in if daca nu se duce in elif

# elif verifica daca expresia este True daca nu se duce in else

# else este iesire daca if nu e True si nici elif atunci iese prin else


# Ex 2. daca x este nr natural printam acest lucru sau nu;
x = int(input('introduceti un nr'))
if x >= 0:
    print('numar natural')
elif x < 0:
    print('nu este nr natural')


# Ex nr 3. x numar pozitiv, negativ  sau neutru
x = int(input('introduceti un nr'))
if x > 0:
    print('numar pozitiv')
elif x == 0:
    print('numar neutru')
elif x < 0:
    print('numar negativ')


# Ex 4. verifica daca x este intre -2 si 13

x = int(input('introduceti un nr'))
if (x > -2) and (x < 13):
    print('x este in interval')
else:
    print('x nu este in interval')


# Ex 5. verifica si afiseaza daca diferenta dintre x si y este mai mica de 5;
# x-y < 5
x = int(input('introduceti valoarea lui x'))
y = int(input('inc troduceti valoarea lui y'))

if x > y:
    print('x este mai mare')
elif x < y:
    print('x este mai mic')
elif x == y:
    print('este egal')

# Ex 6 .verifica daca x  nu este intre 5 si 27
x = int(input('introduceti un nr'))
if not (5 < x < 27):
    print('x nu este in interval')
else:
    print('x este in interval')

# Ex 7.x și y (int) Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
x = int(input('introduceti valoarea lui x'))
y = int(input('inc troduceti valoarea lui y'))

if x > y:
    print(' x este mai mare')
elif x == y:
    print('este egal')

elif x < y:
    print('x este mai mic')

#  Ex 8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

from math import sqrt as radical
x = int(input('prima latura a triunghiului'))
y = int(input('a doua latura a triunghiului'))
z = int(input('a treia latura a triunghiului'))
if x == y == z:
    print('este echilateral')
elif x == y or y == z or z == x:
    print('este isoscel')
else:
    print('oarecare')

perimetrul = x + y + z
print('perimetru este: ', perimetrul)
p = (x + y + z)/2
aria = radical(p * (p - x) * (p - y) * (p - z))
print('aria este:', aria)
h = 2 * aria / p
print('inaltimea este:', h)

# Ex 9.  Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
# vocala a,e,i,u,( A,E,I,O,U)
ch = input('introduceti caracterul')
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
        or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print(ch, 'este o vocala')
else:
    print(ch, 'nu este o vocala')


# Ex 10. Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = int(input('nota'))
if nota > 9:
    print('nota este A')
elif nota > 8:
    print('nota este B')
elif nota > 7:
    print('nota este C')
elif nota > 6:
    print('nota este D')
elif nota > 4:
    print('nota este E')
elif nota <= 4:
    print('nota este F')
