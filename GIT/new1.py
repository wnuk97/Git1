#pierwszy  plik
print("CDV")
print(2)

#potegowanie
potega = 2 ** 10
print(potega)

tekst =  "CDV"
print(tekst * 2)

#pobieranie danych z klawiatury
print("Twoje imię: ")
imie = input ()
print("Twoje imię: " + imie)

nazwisko = 'Nowak'
print('Twoje dane: ' + imie + ' ' + nazwisko)

print("Twój wiek: ")
age = input()
print("Twój wiek: " + age)

print('Twoje dane: ' + imie + ' ' + nazwisko + ' ' + age + ' ' + 'lat')
print('Twoje imie: {}, Twój nazwisko: {}, Twoje wiek: {}'.format(imie, nazwisko, age))
# print(f'Twoje imie: {imie}, Twoje nazwisko: {nazwisko}, Twój wiek: {age}')
dlugosc = len(nazwisko)
print(dlugosc)
print(type(dlugosc))
dlugosc = str(dlugosc)
print('Długość nazwiska: ' + dlugosc)

nazwisko = 'Kowalski'
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)
#konwersja
x = '5'
print(type(x))
x = int(x)
print(type(x))
x = float(x)
print(type(x))
print(x)

y = 5
print(type(y))
y = y / 2
print(type(y))

nazwisko = 'Kowalski'
print(nazwisko[0])
print(nazwisko[0:3])
print(nazwisko[-2])
print(nazwisko[-2:])
print(nazwisko[:-2])
print(nazwisko[:-2:2])