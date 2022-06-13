import heapq
import json
import operator
import os
import sys
from random import randint
# Zasady
player = input('Podaj swoje imię: ')
title = f'Witaj {player}, grasz w Koło fortuny!'.upper()
print('=' * 30)
print(title)
print('=' * 30)
print('''Zgaduj po jednej literze na raz. Aby kupić samogłoskę, musisz mieć $500.
Jeśli sądzisz, że znasz całe słowo lub zsanie, wpisz \'bingo\' i wciśnij enter, potem podaj słowo lub zdanie.
Otrzymasz wtedy wartość każdej litery a samogłośki za darmo.''')
print('=' * 30)

amounts = [500, 750, 1000, 1250, 1500, 1750, 5000]
total = 0

# Lista liter do zdjęcia z tablicy po poprawnym trafieniu
alphabet = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż', 'A', 'B', 'C',
            'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
# Kategorie, słowa i frazesy z pliko json
with open("kategorie.json", "r") as scan:
    content = json.loads(scan.read())
# Losowy wybór kategorii
categories = content['kategorie']
category = randint(0, len(categories)-1)
# Wypisz kategorię
print('Kategoria:', str(list(categories[category])[0]).upper())
# Losowy wybór słowa lub zdania
word = str(list(categories[category].values())[0]).upper()
wordCount = len(word) - word.count(" ") - word.count("-")
wordRange = wordCount in range(22, 92)
wordLastLetter = int(repr(wordCount)[-1])
wordTeens = wordCount not in range(5, 22)

if wordCount in range(2, 5) or wordLastLetter == 2 and wordTeens \
        or wordLastLetter == 3 and wordTeens \
        or wordLastLetter == 4 and wordTeens:
    print('Na', wordCount, 'litery')
else:
    print('Na', wordCount, 'liter')

# Wypełnienie słowa lub zdania podkreślnikami
Word = []
for char in word:
    if char.isalpha():
        Word.append('_')
    else:
        Word.append(char)


# Funkja drukująca słowo lub zdanie
def printWord(word):
    for char in word:
        print(char, end=' ')
    print()


printWord(Word)

# Lista samogłosek
vowels = ['A', 'E', 'I', 'O', 'U']

# Zgaduj zgadula, do bólu
while True:
    while True:
        # Losowy wybór wygranej za odgadniętą literę
        amount = amounts[randint(0, (len(amounts) - 1))]
        print('Otrzymasz $' + str(amount), 'za poprawną literę')
        print('Zapłacisz $500 za samogłoskę')
        guess = input('Zgaduj, podaj literę: \n').upper()
        # Jeśli gracz che odgadnąć całość od razu
        if guess == 'BINGO':
            while True:
                correct = 0
                guess = input().upper()
                for letter in range(len(guess)):
                    if guess[letter] == word[letter]:
                        correct += 1
                    else:
                        break
                if correct == len(guess):
                    for letter in range(len(guess)):
                        if guess[letter] == word[letter]:
                            if not Word[letter].isalpha():
                                Word[letter] = guess[letter]
                                if guess[letter] not in vowels and guess[letter].isalpha():
                                    total += amount
                else:
                    print('Niestety nie, to nie jest dobra odpowiedź!')
                    printWord(Word)
                    break
                if '_' not in Word:
                    printWord(Word)
                    break
                else:
                    for char in range(len(Word)):
                        if word[char] == guess:
                            Word[char] = guess
                print('$' + str(total))
                printWord(Word)
                if '_' not in Word:
                    break
            break
        # Jeśli gracz poda już wcześniej podaną literę
        elif guess not in alphabet:
            print('Już użyłeś/aś tej litery!')
            print('Posiadasz: $' + str(total))
        # Jeśli samogłoska, zabierz graczowi $500
        elif guess in vowels:
            if total >= 500:
                alphabet.remove(guess)
                for char in range(len(Word)):
                    if word[char] == guess:
                        total -= 500
                        Word[char] = guess
            # Brak środków na zakup samogłoski
            else:
                print('Za mało pieniędzy')
            print('Posiadasz: $' + str(total))
            printWord(Word)
            if '_' not in Word:
                break
        # Jeśli do tej pory wszystko jest False, zdejmij literę z alfabetu i wstaw ją do szukanego hasła
        else:
            alphabet.remove(guess)
            for char in range(len(Word)):
                if word[char] == guess:
                    Word[char] = guess
                    total += amount
            print('Posiadasz: $' + str(total))
            printWord(Word)
            if '_' not in Word:
                break
    # Całe słowo lub zdanie odgadnięte, koniec gry.
    if '_' not in Word:
        with open("wyniki.txt", "a") as w:
            w.write(player + ' ' + str(total) + '\n')
            w.close()
        print('=' * 30)
        print('Brawo!')
        print('Twoja wygrana: $' + str(total))
        print('=' * 30)
        newGame = str(input('Gramy dalej? (t/n): '))
        if newGame == 't':
            print('\nNowa gra:')
            os.execl(sys.executable, sys.executable, *sys.argv)
        if newGame == 'n':
            print("Dziękujemy za grę, do zobaczenia.")
            break
        else:
            print("To nie było śmieszne, żegnam.")
            break
wynik = {}
position = 0
with open("wyniki.txt", "r") as wyniki:
    for line in wyniki:
        (k, v) = line.split()
        wynik[k] = int(v)
sorted_dsc = dict(sorted(wynik.items(), key=operator.itemgetter(1), reverse=True))
top10 = heapq.nlargest(5, wynik, key=wynik.get)
print('\nWyniki 5 najlepszych graczy:')
for i in top10:
    position += 1
    print(position, i, wynik[i])
wyniki.close()
