tekst = 'Anna, paweł, TomEK'

tab = tekst.split(',')
print(tekst)
print(tab)
imie = tab[0]
print(imie)
print(type(tab))

imieDuze = imie.upper()
print(imieDuze)

imieMale = imie.lower()
print(imieMale)

#sprawdzanie zawartości
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)
print(type(zawartosc))

imie = 'Julia'
print('\nDane użytkownika:\nMasz na imię: ' + imie)

text1 = 'Jan\n'
text2 = 'Nowak'
print(text1 + text2)

text1 = text1.rstrip()
print(text1 + text2)
print(text1 + ' ' + text2)

#wyświetlanie łańcuchów znaków

#wszystkie wersje Pythona
text = '%s, Java i %s'%('PHP', 'Python')
print(text)

#nowsze wersje Pythona 2.6
text = '{0},  Java i {1}'.format('PHP', 'Python')
print(text)

# help(text.replace)
new = text.replace('PHP', 'C#')
print(new)

#wypisanie danych
rok = '2019'
miesiac = 'marzec'
dzien = '23'

print('Data: ', end='')
print(dzien, miesiac, rok)

print('Data: ', end='')
print(dzien, miesiac, rok, sep='-')

print('Data: ', end='')
print(dzien, miesiac, rok, sep='.')