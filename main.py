import json
from typing import Tuple
import pygame
from random import choices, randint
from time import sleep

pygame.init()

WIDTH, HEIGHT = int(1280), int(720)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = int(60)

BG_COLOR = (int(30), int(39), int(46)) # R, G, B

GAME_NAME_FONT = pygame.font.SysFont('Lato', 40) # FontFamily, FontSize
GAME_NAME_FONT_COLOR = (int(255), int(192), int(72)) # R, G, B
DESCRIPTION_FONT = pygame.font.SysFont('Lato', 30) # FontFamily, FontSize
DESCRIPTION_FONT_COLOR = (int(52), int(231), int(228)) # R, G, B

GAME_NAME_LOGO_Y_POS = int(10)
DESCRIPTION1_Y_POS = int(150)
DESCRIPTION2_Y_POS = int(190)
DESCRIPTION3_Y_POS = int(230)

INPUT_BOX = pygame.Rect(50, 520, 1180, 60) # X, Y, WIDTH, HEIGHT 
INPUT_BOX_COLOR = (int(255), int(168), int(1)) # R, G, B
INPUT_BOX_FILL = pygame.Rect(53, 523, 1174, 54) # X, Y, WIDTH, HEIGHT 
INPUT_BOX_FONT = pygame.font.SysFont('Lato', 30) # FontFamily, FontSize
INPUT_BOX_FONT_COLOR = (int(0), int(216), int(214)) # R, G, B
inputBoxText = str('')
INPUT_BOX_TEXT_POS = (int(60), int(530)) # X, Y

CATEGORY_TEXT_Y_POS = int(150)
NUMBER_OF_LETTERS_Y_POS = int(190)
category = str()
word = str()
numberOfLetters = int()
wordLastLetter = int()
wordTeens = bool()

MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW = int(23) # Because 1180 (1280 - 50 - 50 = 1180 | 50 is margin on each side) : 50 = 23.6 ~ 23
SINGLE_LETTER_BOX_WIDTH = int(40)
SINGLE_LETTER_BOX_HEIGHT = int(60)
SINGLE_LETTER_BOX_FILL_WIDTH = int(34)
SINGLE_LETTER_BOX_FILL_HEIGHT = int(54)
SPACE_BETWEEN_LETTERS = int(10)
FIRST_ROW_BOX_Y_POS = int(240)
FIRST_ROW_BOX_FILL_Y_POS = int(243)
SECOND_ROW_BOX_Y_POS = int(310)
SECOND_ROW_BOX_FILL_Y_POS = int(313)
THIRD_ROW_BOX_Y_POS = int(380)
THIRD_ROW_BOX_FILL_Y_POS = int(383)
COMMA_FONT = pygame.font.SysFont('Lato', 60) # FontFamily, FontSize

amount = int()
PRICE_FOR_LETTER_TEXT_POS = (int(50), int(460))

balance = int(0)
BALANCE_DESCRIPTION_TEXT_POS = (int(850), int(460))
CURRENT_BALANCE_BOX = pygame.Rect(1000, 450, 230, 60)
CURRENT_BALANCE_BOX_FILL = pygame.Rect(1003, 453, 224, 54)
CURRENT_BALANCE_TEXT_POS = (int(1010), int(460))

alphabet = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

guessedLetters = list[str]()

error_message_type = int(0)
ERROR_MESSAGE_FONT = DESCRIPTION_FONT
ERROR_MESSAGE_FONT_COLOR = (int(245), int(59), int(87))
ERROR_MESSAGE_Y_POS = int(530)

bingo = False

WIN_MESSAGE_FONT = DESCRIPTION_FONT
WIN_MESSAGE_FONT_COLOR = (int(11), int(232), int(129))
WIN_MESSAGE_Y_POS = ERROR_MESSAGE_Y_POS

win = bool(False)

MAIN_MENU_PLAY_BUTTON = pygame.Rect(490, 100, 300, 60)      # X, Y, WIDTH, HEIGHT
MAIN_MENU_INFO_BUTTON = pygame.Rect(490, 200, 300, 60)      # X, Y, WIDTH, HEIGHT 
MAIN_MENU_SCORE_BUTTON = pygame.Rect(490, 300, 300, 60)     # X, Y, WIDTH, HEIGHT 
MAIN_MENU_BUTTON_COLOR = INPUT_BOX_COLOR
MAIN_MENU_BUTTON_HOVER_COLOR = (int(255), int(63), int(52))
MAIN_MENU_BUTTON_HOVER_BG_COLOR = (int(72), int(84), int(96))
MAIN_MENU_BUTTON_FONT = INPUT_BOX_FONT
MAIN_MENU_BUTTON_FONT_COLOR = INPUT_BOX_FONT_COLOR
MAIN_MENU_BUTTON_HOVER_FONT_COLOR = (int(60), int(64), int(198)) #rgb(60, 64, 198)
MAIN_MENU_PLAY_TEXT_Y_POS = int(110)
MAIN_MENU_INFO_TEXT_Y_POS = int(210)
MAIN_MENU_SCORE_TEXT_Y_POS = int(310)

BACK_TO_MAIN_MENU_BUTTON = pygame.Rect(490, 610, 300, 60)   # X, Y, WIDTH, HEIGHT
BACK_TO_MAIN_MENU_TEXT_Y_POS = int(620)

with open('kategorie.json', 'r', encoding='utf-8') as file:
    content = json.loads(file.read())
CATEGORIES = content['kategorie']

AMOUNTS = [500, 750, 1000, 1250, 1500, 1750, 5000]

def setNotConstantVariables():
    global inputBoxText, category, word, numberOfLetters, wordLastLetter, wordTeens, amount, balance, alphabet, vowels, guessedLetters, error_message_type, bingo, win
    inputBoxText = str()
    category = str()
    word = str()
    numberOfLetters = int()
    wordLastLetter = int()
    wordTeens = bool()
    amount = int()
    balance = int(0)
    alphabet = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']
    guessedLetters = list[str]()
    error_message_type = int(0)
    bingo = bool(False)
    win = bool(False)

def setBackground():
    WINDOW.fill(BG_COLOR)

def setGameNameLogo():
    welcomeText = GAME_NAME_FONT.render('NIEkoło NIEfortuny', True, GAME_NAME_FONT_COLOR)
    welcomeTextXPos = (WIDTH - welcomeText.get_size()[0]) / 2
    WINDOW.blit(welcomeText, (welcomeTextXPos, GAME_NAME_LOGO_Y_POS))

def setGameDescription():
    description1 = DESCRIPTION_FONT.render('Zgaduj po jednej literze na raz. Aby kupić samogłoskę, musisz mieć $500.', True, DESCRIPTION_FONT_COLOR)
    description2 = DESCRIPTION_FONT.render('Jeśli sądzisz, że znasz całe słowo lub zdanie, wpisz \'bingo\' i wciśnij enter.', True, DESCRIPTION_FONT_COLOR)
    description3 = DESCRIPTION_FONT.render('Następnie podaj słowo lub zdanie.', True, DESCRIPTION_FONT_COLOR)
    description1XPos = (WIDTH - description1.get_size()[0]) / 2
    description2XPos = (WIDTH - description2.get_size()[0]) / 2
    description3XPos = (WIDTH - description3.get_size()[0]) / 2
    WINDOW.blit(description1, (description1XPos, DESCRIPTION1_Y_POS))
    WINDOW.blit(description2, (description2XPos, DESCRIPTION2_Y_POS))
    WINDOW.blit(description3, (description3XPos, DESCRIPTION3_Y_POS))

def setCategory():
    global category, word, numberOfLetters, wordLastLetter, wordTeens
    categoryID = randint(0, (len(CATEGORIES) - 1))
    category = list(CATEGORIES[categoryID])[0]
    word = list(CATEGORIES[categoryID].values())[0].upper()
    numberOfLetters = len(word) - word.count(" ") - word.count("-")
    wordLastLetter = int(repr(numberOfLetters)[-1])
    wordTeens = numberOfLetters not in range(5, 22)

def setCategoryText():
    categoryText = DESCRIPTION_FONT.render(f'Kategoria: {category}', True, DESCRIPTION_FONT_COLOR)
    categoryTextXPos = (WIDTH - categoryText.get_size()[0]) / 2
    numberOfLettersText: pygame.Surface
    if(numberOfLetters in range(2, 5) or wordLastLetter == 2 and wordTeens \
        or wordLastLetter == 3 and wordTeens \
        or wordLastLetter == 4 and wordTeens):
        numberOfLettersText = DESCRIPTION_FONT.render(f'Na {numberOfLetters} litery', True, DESCRIPTION_FONT_COLOR)
    else:
        numberOfLettersText = DESCRIPTION_FONT.render(f'Na {numberOfLetters} liter', True, DESCRIPTION_FONT_COLOR)
    numberOfLettersTextXPos = (WIDTH - numberOfLettersText.get_size()[0]) /2    
    WINDOW.blit(categoryText, (categoryTextXPos, CATEGORY_TEXT_Y_POS))
    WINDOW.blit(numberOfLettersText, (numberOfLettersTextXPos, NUMBER_OF_LETTERS_Y_POS))

def setWordPuzzle():
    global word, win
    words = word.split()
    isFirstFull, isSecondFull = bool(False), bool(False)
    firstRowLetterSize, secondRowLetterSize, thirdRowLetterSize = int(0), int(0), int(0)
    firstRow, secondRow, thirdRow = list[str](), list[str](), list[str]()
    wholeWordGuessed = bool(True)
    for singleWord in words:
        if(isFirstFull == False):
            if(firstRowLetterSize + len(singleWord) + 1 > MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW):
                isFirstFull = bool(True)
        elif(isSecondFull == False):
            if(secondRowLetterSize + len(singleWord) + 1 > MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW):
                isSecondFull = bool(True)
        if(isFirstFull == False):
            if(firstRowLetterSize == 0):
                firstRowLetterSize += len(singleWord)
            else:
                firstRowLetterSize += len(singleWord) + 1   
            firstRow.append(singleWord)
        elif(isSecondFull == False):
            if(secondRowLetterSize == 0):
                secondRowLetterSize += len(singleWord)
            else:
                secondRowLetterSize += len(singleWord) + 1
            secondRow.append(singleWord)
        else:
            if(thirdRowLetterSize == 0):
                thirdRowLetterSize += len(singleWord)
            else:
                thirdRowLetterSize += len(singleWord) + 1
            thirdRow.append(singleWord)
    size = firstRowLetterSize * SINGLE_LETTER_BOX_WIDTH + (firstRowLetterSize - 1) * SPACE_BETWEEN_LETTERS
    XPos = int((WIDTH - size) / 2)
    for singleWord in firstRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(XPos, FIRST_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(XPos + 3, FIRST_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, True, INPUT_BOX_FONT_COLOR), (XPos + 10, FIRST_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                letter = INPUT_BOX_FONT.render(char, True, INPUT_BOX_FONT_COLOR)
                letterXPos = int(XPos + (((34 - letter.get_size()[0]) / 2) + 3))
                WINDOW.blit(letter, (letterXPos, FIRST_ROW_BOX_Y_POS + 10))
            else:
                wholeWordGuessed = bool(False)
            XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
    size = secondRowLetterSize * SINGLE_LETTER_BOX_WIDTH + (secondRowLetterSize - 1) * SPACE_BETWEEN_LETTERS 
    XPos = int((WIDTH - size) / 2)
    for singleWord in secondRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(XPos, SECOND_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(XPos + 3, SECOND_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, True, INPUT_BOX_FONT_COLOR), (XPos + 10, SECOND_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                letter = INPUT_BOX_FONT.render(char, True, INPUT_BOX_FONT_COLOR)
                letterXPos = int(XPos + (((34 - letter.get_size()[0]) / 2) + 3))
                WINDOW.blit(letter, (letterXPos, SECOND_ROW_BOX_Y_POS + 10))
            else:
                wholeWordGuessed = bool(False)
            XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
    size = thirdRowLetterSize * SINGLE_LETTER_BOX_WIDTH + (thirdRowLetterSize - 1) * SPACE_BETWEEN_LETTERS 
    XPos = int((WIDTH - size) / 2)
    for singleWord in thirdRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(XPos, THIRD_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(XPos + 3, THIRD_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, True, INPUT_BOX_FONT_COLOR), (XPos + 10, THIRD_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                letter = INPUT_BOX_FONT.render(char, True, INPUT_BOX_FONT_COLOR)
                letterXPos = int(XPos + (((34 - letter.get_size()[0]) / 2) + 3))
                WINDOW.blit(letter, (letterXPos, THIRD_ROW_BOX_Y_POS + 10))
            else:
                wholeWordGuessed = bool(False)
            XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        XPos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
    if(wholeWordGuessed):
        win = bool(True)

def setPriceForLetter():
    global amount
    amount = int(str(choices(AMOUNTS, weights=(70, 60, 50, 40, 30, 20, 10), k=1))[1:-1])

def setPriceForLetterText():
    priceForLetterText = DESCRIPTION_FONT.render(f'Otrzymasz ${str(amount)} za poprawną literę', True, DESCRIPTION_FONT_COLOR)
    WINDOW.blit(priceForLetterText, PRICE_FOR_LETTER_TEXT_POS)  

def setCurrentBalance():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, CURRENT_BALANCE_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, CURRENT_BALANCE_BOX_FILL)
    balanceDescriptionText = DESCRIPTION_FONT.render('Posiadasz', True, DESCRIPTION_FONT_COLOR)
    currentBalanceText = INPUT_BOX_FONT.render(f'${balance}', True, INPUT_BOX_FONT_COLOR)
    WINDOW.blit(balanceDescriptionText, BALANCE_DESCRIPTION_TEXT_POS)
    WINDOW.blit(currentBalanceText, CURRENT_BALANCE_TEXT_POS)

def setTextBox():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, INPUT_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, INPUT_BOX_FILL)
    textBoxContent = INPUT_BOX_FONT.render(inputBoxText, True, INPUT_BOX_FONT_COLOR)
    WINDOW.blit(textBoxContent, INPUT_BOX_TEXT_POS)

def setErrorMessageBox():
    if(error_message_type == 0):
        return
    elif(error_message_type == 1):
        errorMessage = ERROR_MESSAGE_FONT.render('Już użyłeś/aś tej litery!', True, ERROR_MESSAGE_FONT_COLOR)
        errorMessageXPos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessageXPos, ERROR_MESSAGE_Y_POS))
    elif(error_message_type == 2):
        errorMessage = ERROR_MESSAGE_FONT.render('Za mało pieniędzy!', True, ERROR_MESSAGE_FONT_COLOR)
        errorMessageXPos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessageXPos, ERROR_MESSAGE_Y_POS))
    elif(error_message_type == 3):
        errorMessage = ERROR_MESSAGE_FONT.render('Niestety nie, to nie jest dobra odpowiedź!', True, ERROR_MESSAGE_FONT_COLOR)
        errorMessageXPos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessageXPos, ERROR_MESSAGE_Y_POS))

def setWinMessage():
    if(win):
        winMessage = WIN_MESSAGE_FONT.render(f'Brawo! Twoja wygrana: ${str(balance)}', True, WIN_MESSAGE_FONT_COLOR)
        winMessageXPos = (WIDTH - winMessage.get_size()[0]) /2
        WINDOW.blit(winMessage, (winMessageXPos, WIN_MESSAGE_Y_POS))

def setPlayAgainMessage():
    playAgain = WIN_MESSAGE_FONT.render(f'Aby zagrać ponownie, wpisz "TAK"', True, WIN_MESSAGE_FONT_COLOR)
    playAgainXPos = (WIDTH - playAgain.get_size()[0]) /2
    WINDOW.blit(playAgain, (playAgainXPos, WIN_MESSAGE_Y_POS))

def setMainMenuButtons(mousePos: Tuple[int, int]):
    if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 100 and mousePos[1] <= 160):
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_HOVER_COLOR, MAIN_MENU_PLAY_BUTTON, 3, 10)
        playText = MAIN_MENU_BUTTON_FONT.render('Graj', True, MAIN_MENU_BUTTON_HOVER_FONT_COLOR)
    else:
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_COLOR, MAIN_MENU_PLAY_BUTTON, 3, 10)
        playText = MAIN_MENU_BUTTON_FONT.render('Graj', True, MAIN_MENU_BUTTON_FONT_COLOR)
    if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 200 and mousePos[1] <= 260):
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_HOVER_COLOR, MAIN_MENU_INFO_BUTTON, 3, 10)
        gameInfoText = MAIN_MENU_BUTTON_FONT.render('Jak grać?', True, MAIN_MENU_BUTTON_HOVER_FONT_COLOR)
    else:
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_COLOR, MAIN_MENU_INFO_BUTTON, 3, 10)
        gameInfoText = MAIN_MENU_BUTTON_FONT.render('Jak grać?', True, MAIN_MENU_BUTTON_FONT_COLOR)
    if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 300 and mousePos[1] <= 360):
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_HOVER_COLOR, MAIN_MENU_SCORE_BUTTON, 3, 10)
        scoreText = MAIN_MENU_BUTTON_FONT.render('Wyniki', True, MAIN_MENU_BUTTON_HOVER_FONT_COLOR)
    else:
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_COLOR, MAIN_MENU_SCORE_BUTTON, 3, 10)
        scoreText = MAIN_MENU_BUTTON_FONT.render('Wyniki', True, MAIN_MENU_BUTTON_FONT_COLOR)
    playTextXPos = (WIDTH - playText.get_size()[0]) / 2
    gameInfoTextXPos = (WIDTH - gameInfoText.get_size()[0]) / 2
    scoreTextXPos = (WIDTH - scoreText.get_size()[0]) / 2
    WINDOW.blit(playText, (playTextXPos, MAIN_MENU_PLAY_TEXT_Y_POS))
    WINDOW.blit(gameInfoText, (gameInfoTextXPos, MAIN_MENU_INFO_TEXT_Y_POS))
    WINDOW.blit(scoreText, (scoreTextXPos, MAIN_MENU_SCORE_TEXT_Y_POS))

def setBackToMainMenuButton(mousePos: Tuple[int, int]):
    if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 610 and mousePos[1] <= 670):
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_HOVER_COLOR, BACK_TO_MAIN_MENU_BUTTON, 3, 10)
        backToMainMenuText = MAIN_MENU_BUTTON_FONT.render('Powrót do menu', True, MAIN_MENU_BUTTON_HOVER_FONT_COLOR)
    else:
        pygame.draw.rect(WINDOW, MAIN_MENU_BUTTON_COLOR, BACK_TO_MAIN_MENU_BUTTON, 3, 10)
        backToMainMenuText = MAIN_MENU_BUTTON_FONT.render('Powrót do menu', True, MAIN_MENU_BUTTON_FONT_COLOR)
    backToMainMenuTextXPos = (WIDTH - backToMainMenuText.get_size()[0]) / 2
    WINDOW.blit(backToMainMenuText, (backToMainMenuTextXPos, BACK_TO_MAIN_MENU_TEXT_Y_POS))

def setGameWindow():
    global inputBoxText, alphabet, error_message_type, balance, bingo, win
    setNotConstantVariables()
    setCategory()
    setPriceForLetter()
    buttonClicked = bool(False)
    run = bool(True)
    while(run):
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = bool(False)
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 610 and mousePos[1] <= 670):
                    buttonClicked = bool(True)
            if(event.type == pygame.KEYDOWN):
                error_message_type = int(0)
                if(event.key == pygame.K_BACKSPACE):
                    inputBoxText = inputBoxText[:-1]
                elif(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                    inputBoxText = str(inputBoxText.upper())
                    if(bingo):
                        if(inputBoxText == word):
                            for letter in inputBoxText:
                                if(letter not in guessedLetters):
                                    guessedLetters.append(letter)
                            win = bool(True)
                            inputBoxText = str('')
                            break
                        else:
                            bingo = bool(False)
                            error_message_type = int(3)
                    elif(inputBoxText == 'BINGO'):
                        bingo = bool(True)
                    elif(inputBoxText not in alphabet):
                        error_message_type = int(1)
                        setPriceForLetter()
                    elif(inputBoxText in vowels):
                        if(balance >= 500):
                            alphabet.remove(inputBoxText)                            
                            guessedLetters.append(inputBoxText)
                            balance -= 500
                        else:
                            error_message_type = int(2)
                        setPriceForLetter()
                    else:
                        alphabet.remove(inputBoxText)
                        guessedLetters.append(inputBoxText)
                        for char in range(len(word)):
                            if word[char] == inputBoxText:
                                balance += amount
                        setPriceForLetter()
                    inputBoxText = str('')
                else:
                    inputBoxText += str(event.unicode)
        mousePos = pygame.mouse.get_pos()
        setBackground()
        setGameNameLogo()
        setCategoryText()
        setWordPuzzle()
        setPriceForLetterText()
        setCurrentBalance()
        setTextBox()
        setErrorMessageBox()
        setWinMessage()
        setBackToMainMenuButton(mousePos)
        pygame.display.update()
        if(buttonClicked):
            break
        if(win):
            sleep(10)
            break
    if(buttonClicked):
        return False
    while(run):
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = bool(False)
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 610 and mousePos[1] <= 670):
                    buttonClicked = bool(True)
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                    inputBoxText = str(inputBoxText.upper())
                    if(inputBoxText == "TAK"):
                        return True
                    else:
                        return False
                else:
                    inputBoxText += str(event.unicode)
        setBackground()
        setGameNameLogo()
        setCategoryText()
        setWordPuzzle()
        setPriceForLetterText()
        setCurrentBalance()
        setTextBox()
        setPlayAgainMessage() 
        setBackToMainMenuButton()   
        pygame.display.update()
        if(buttonClicked):
            break
    if(buttonClicked):
        return False

def setGameInfoWindow():
    buttonClicked = bool(False)
    run = bool(True)
    while(run):
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = bool(False)
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(mousePos[0] >= 490 and mousePos[0] <= 790 and mousePos[1] >= 610 and mousePos[1] <= 670):
                    buttonClicked = bool(True)
        mousePos = pygame.mouse.get_pos()
        setBackground()
        setGameNameLogo()
        setGameDescription()
        setBackToMainMenuButton(mousePos)
        pygame.display.update()
        if(buttonClicked):
            break
    if(buttonClicked):
        return False

def setMainMenuWindow():
    buttonType = int(0)
    run = bool(True)
    while(run):
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = bool(False)
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(mousePos[0] >= 490 and mousePos[0] <= 790):
                    if(mousePos[1] >= 100 and mousePos[1] <= 160):
                        buttonType = int(1)
                    elif(mousePos[1] >= 200 and mousePos[1] <= 260):
                        buttonType = int(2)
                    elif(mousePos[1] >= 300 and mousePos[1] <= 360):
                        buttonType = int(3)
        mousePos = pygame.mouse.get_pos()
        setBackground()
        setGameNameLogo()
        setMainMenuButtons(mousePos)
        pygame.display.update()
        if(buttonType != 0):
            break
    return buttonType

def main():    
    pygame.display.set_caption("NIEkoło NIEfortuny")
    run = bool(True)
    while(run):
        buttonType = setMainMenuWindow()
        runTab = bool(True)
        if(buttonType == 0):
            break
        elif(buttonType == 1):
            while(runTab):
                runTab = setGameWindow()
        elif(buttonType == 2):
            while(runTab):
                runTab = setGameInfoWindow()
        if(runTab is None):
            break
    pygame.quit()

if __name__ == "__main__":
    main()
