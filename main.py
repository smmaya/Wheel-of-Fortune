import json
import pygame
from random import choices, randint
from time import sleep

pygame.init()

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

BG_COLOR = (44, 62, 80) # R, G, B

MAIN_FONT = pygame.font.SysFont('Lato', 40) # FontFamily, FontSize
MAIN_FONT_COLOR = (241, 196, 15) # R, G, B
DESCRIPTION_FONT = pygame.font.SysFont('Lato', 30) # FontFamily, FontSize
DESCRIPTION_FONT_COLOR = (52, 152, 219) # R, G, B

GAME_NAME_LOGO_POSITION = (342, 10) # X, Y      342 because width of welcomeText is 596 -> (1280 - 596) / 2 = 342. This is done on purpose of center the welcomeText
DESCRIPTION1_POSITION = (158, 60) # X, Y        158 because width of description1 is 964
DESCRIPTION2_POSITION = (161, 100) # X, Y       161 because width of description1 is 958
DESCRIPTION3_POSITION = (119, 140) # X, Y       119 because width of description1 is 1041

INPUT_BOX = pygame.Rect(50, 610, 1180, 60) # X, Y, WIDTH, HEIGHT 
INPUT_BOX_COLOR = (243, 156, 18) # R, G, B
INPUT_BOX_FILL = pygame.Rect(53, 613, 1174, 54) # X, Y, WIDTH, HEIGHT 
INPUT_BOX_FONT = pygame.font.SysFont('Lato', 30) # FontFamily, FontSize
INPUT_BOX_FONT_COLOR = (41, 128, 185) # R, G, B
inputBoxText = ''
INPUT_BOX_TEXT_POSITION = (60, 620) # X, Y

CATEGORY_TEXT_Y_POSITION = 220
NUMBER_OF_LETTERS_Y_POSITION = 260
category: str
word: str
numberOfLetters: int
wordLastLetter: int
wordTeens: bool

MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW = 23 # Because 1180 (1280 - 50 - 50 = 1180 | 50 is margin on each side) : 50 = 23.6 ~ 23
SINGLE_LETTER_BOX_WIDTH = 40
SINGLE_LETTER_BOX_HEIGHT = 60
SINGLE_LETTER_BOX_FILL_WIDTH = 34
SINGLE_LETTER_BOX_FILL_HEIGHT = 54
SPACE_BETWEEN_LETTERS = 10
FIRST_ROW_BOX_Y_POS = 310
FIRST_ROW_BOX_FILL_Y_POS = 313
SECOND_ROW_BOX_Y_POS = 380
SECOND_ROW_BOX_FILL_Y_POS = 383
THIRD_ROW_BOX_Y_POS = 450
THIRD_ROW_BOX_FILL_Y_POS = 453
COMMA_FONT = pygame.font.SysFont('Lato', 60) # FontFamily, FontSize

amount: int
PRICE_FOR_LETTER_TEXT_POSITION = (50, 540)

balance = 0
BALANCE_DESCRIPTION_TEXT_POSITION = (850, 540)
CURRENT_BALANCE_BOX = pygame.Rect(1000, 530, 230, 60)
CURRENT_BALANCE_BOX_FILL = pygame.Rect(1003, 533, 224, 54)
CURRENT_BALANCE_TEXT_POSITION = (1010, 540)

alphabet = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ł', 'ł', 'Ń', 'ń', 'Ó', 'ó', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

vowels = ['A', 'E', 'I', 'O', 'U']

guessedLetters = []

error_message_type = int(0)
ERROR_MESSAGE_FONT = DESCRIPTION_FONT
ERROR_MESSAGE_FONT_COLOR = (192, 57, 43)
ERROR_MESSAGE_Y_POS = 620

bingo = False

WIN_MESSAGE_FONT = DESCRIPTION_FONT
WIN_MESSAGE_FONT_COLOR = (39, 174, 96)
WIN_MESSAGE_Y_POS = ERROR_MESSAGE_Y_POS

win = False

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
    guessedLetters = []
    error_message_type = int(0)
    bingo = False
    win = False

def setBackground():
    WINDOW.fill(BG_COLOR)

def setGameNameLogo():
    welcomeText = MAIN_FONT.render('Witamy w grze "NIEKoło NIEfortuny"', 1, MAIN_FONT_COLOR)
    WINDOW.blit(welcomeText, GAME_NAME_LOGO_POSITION)

def setGameDescription():
    description1 = DESCRIPTION_FONT.render('Zgaduj po jednej literze na raz. Aby kupić samogłoskę, musisz mieć $500.', 1, DESCRIPTION_FONT_COLOR)
    description2 = DESCRIPTION_FONT.render('Jeśli sądzisz, że znasz całe słowo lub zdanie, wpisz \'bingo\' i wciśnij enter.', 1, DESCRIPTION_FONT_COLOR)
    description3 = DESCRIPTION_FONT.render('Następnie podaj słowo lub zdanie. Otrzymasz wtedy wartość każdej spółgłoski', 1, DESCRIPTION_FONT_COLOR)
    WINDOW.blit(description1, DESCRIPTION1_POSITION)
    WINDOW.blit(description2, DESCRIPTION2_POSITION)
    WINDOW.blit(description3, DESCRIPTION3_POSITION)

def setCategory():
    global category, word, numberOfLetters, wordLastLetter, wordTeens
    categoryID = randint(0, (len(CATEGORIES) - 1))
    category = list(CATEGORIES[categoryID])[0]
    word = list(CATEGORIES[categoryID].values())[0].upper()
    numberOfLetters = len(word) - word.count(" ") - word.count("-")
    wordLastLetter = int(repr(numberOfLetters)[-1])
    wordTeens = numberOfLetters not in range(5, 22)

def setCategoryText():
    categoryText = DESCRIPTION_FONT.render(f'Kategoria: {category}', 1, DESCRIPTION_FONT_COLOR)
    category_text_x_position = (WIDTH - categoryText.get_size()[0]) / 2
    numberOfLettersText: pygame.Surface
    if(numberOfLetters in range(2, 5) or wordLastLetter == 2 and wordTeens \
        or wordLastLetter == 3 and wordTeens \
        or wordLastLetter == 4 and wordTeens):
        numberOfLettersText = DESCRIPTION_FONT.render(f'Na {numberOfLetters} litery', 1, DESCRIPTION_FONT_COLOR)
    else:
        numberOfLettersText = DESCRIPTION_FONT.render(f'Na {numberOfLetters} liter', 1, DESCRIPTION_FONT_COLOR)
    numberOfLetters_text_x_position = (WIDTH - numberOfLettersText.get_size()[0]) /2    
    WINDOW.blit(categoryText, (category_text_x_position, CATEGORY_TEXT_Y_POSITION))
    WINDOW.blit(numberOfLettersText, (numberOfLetters_text_x_position, NUMBER_OF_LETTERS_Y_POSITION))

def setWordPuzzle():
    global word
    words = word.split()
    isFirstFull, isSecondFull = False, False
    firstRowLetterSize, secondRowLetterSize, thirdRowLetterSize = int(0), int(0), int(0)
    firstRow, secondRow, thirdRow = list[str](), list[str](), list[str]()
    for singleWord in words:
        if(isFirstFull == False):
            if(firstRowLetterSize + len(singleWord) + 1 > MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW):
                isFirstFull = True
        elif(isSecondFull == False):
            if(secondRowLetterSize + len(singleWord) + 1 > MAX_NUMBER_OF_LETTER_IN_SINGLE_ROW):
                isSecondFull = True
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
    X_pos = int((WIDTH - size) / 2)
    for singleWord in firstRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(X_pos, FIRST_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(X_pos + 3, FIRST_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, FIRST_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                if(char == 'M'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 6, FIRST_ROW_BOX_Y_POS + 10))
                elif(char == 'I'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 15, FIRST_ROW_BOX_Y_POS + 10))
                else:
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, FIRST_ROW_BOX_Y_POS + 10))
            X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
    size = secondRowLetterSize * SINGLE_LETTER_BOX_WIDTH + (secondRowLetterSize - 1) * SPACE_BETWEEN_LETTERS 
    X_pos = int((WIDTH - size) / 2)
    for singleWord in secondRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(X_pos, SECOND_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(X_pos + 3, SECOND_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, SECOND_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                if(char == 'M'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 6, SECOND_ROW_BOX_Y_POS + 10))
                elif(char == 'I'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 15, SECOND_ROW_BOX_Y_POS + 10))
                else:
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, SECOND_ROW_BOX_Y_POS + 10))
            X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
    size = thirdRowLetterSize * SINGLE_LETTER_BOX_WIDTH + (thirdRowLetterSize - 1) * SPACE_BETWEEN_LETTERS 
    X_pos = int((WIDTH - size) / 2)
    for singleWord in thirdRow:
        for char in singleWord:
            pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, pygame.Rect(X_pos, THIRD_ROW_BOX_Y_POS, SINGLE_LETTER_BOX_WIDTH, SINGLE_LETTER_BOX_HEIGHT))
            pygame.draw.rect(WINDOW, BG_COLOR, pygame.Rect(X_pos + 3, THIRD_ROW_BOX_FILL_Y_POS, SINGLE_LETTER_BOX_FILL_WIDTH, SINGLE_LETTER_BOX_FILL_HEIGHT))
            if(char == ','):
                WINDOW.blit(COMMA_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, THIRD_ROW_BOX_Y_POS - 15))
            if(char in guessedLetters):
                if(char == 'M'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 6, THIRD_ROW_BOX_Y_POS + 10))
                elif(char == 'I'):
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 15, THIRD_ROW_BOX_Y_POS + 10))
                else:
                    WINDOW.blit(INPUT_BOX_FONT.render(char, 1, INPUT_BOX_FONT_COLOR), (X_pos + 10, THIRD_ROW_BOX_Y_POS + 10))
            X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS
        X_pos += SINGLE_LETTER_BOX_WIDTH + SPACE_BETWEEN_LETTERS

def setPriceForLetter():
    global amount
    amount = int(str(choices(AMOUNTS, weights=(70, 60, 50, 40, 30, 20, 10), k=1))[1:-1])

def setPriceForLetterText():
    priceForLetterText = DESCRIPTION_FONT.render(f'Otrzymasz ${str(amount)} za poprawną literę', 1, DESCRIPTION_FONT_COLOR)
    WINDOW.blit(priceForLetterText, PRICE_FOR_LETTER_TEXT_POSITION)  

def setCurrentBalance():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, CURRENT_BALANCE_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, CURRENT_BALANCE_BOX_FILL)
    balanceDescriptionText = DESCRIPTION_FONT.render('Posiadasz', 1, DESCRIPTION_FONT_COLOR)
    currentBalanceText = INPUT_BOX_FONT.render(f'${balance}', 1, INPUT_BOX_FONT_COLOR)
    WINDOW.blit(balanceDescriptionText, BALANCE_DESCRIPTION_TEXT_POSITION)
    WINDOW.blit(currentBalanceText, CURRENT_BALANCE_TEXT_POSITION)

def setTextBox():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, INPUT_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, INPUT_BOX_FILL)
    textBoxContent = INPUT_BOX_FONT.render(inputBoxText, 1, INPUT_BOX_FONT_COLOR)
    WINDOW.blit(textBoxContent, INPUT_BOX_TEXT_POSITION)

def setErrorMessageBox():
    if(error_message_type == 0):
        return
    elif(error_message_type == 1):
        errorMessage = ERROR_MESSAGE_FONT.render('Już użyłeś/aś tej litery!', 1, ERROR_MESSAGE_FONT_COLOR)
        errorMessage_X_Pos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessage_X_Pos, ERROR_MESSAGE_Y_POS))
    elif(error_message_type == 2):
        errorMessage = ERROR_MESSAGE_FONT.render('Za mało pieniędzy!', 1, ERROR_MESSAGE_FONT_COLOR)
        errorMessage_X_Pos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessage_X_Pos, ERROR_MESSAGE_Y_POS))
    elif(error_message_type == 3):
        errorMessage = ERROR_MESSAGE_FONT.render('Niestety nie, to nie jest dobra odpowiedź!', 1, ERROR_MESSAGE_FONT_COLOR)
        errorMessage_X_Pos = (WIDTH - errorMessage.get_size()[0]) /2
        WINDOW.blit(errorMessage, (errorMessage_X_Pos, ERROR_MESSAGE_Y_POS))

def setWinMessage():
    if(win):
        winMessage = WIN_MESSAGE_FONT.render(f'Brawo! Twoja wygrana: ${str(balance)}', 1, WIN_MESSAGE_FONT_COLOR)
        winMessage_X_Pos = (WIDTH - winMessage.get_size()[0]) /2
        WINDOW.blit(winMessage, (winMessage_X_Pos, WIN_MESSAGE_Y_POS))

def playAgainMessage():
    playAgain = WIN_MESSAGE_FONT.render(f'Aby zagrać ponownie, wpisz "TAK"', 1, WIN_MESSAGE_FONT_COLOR)
    playAgain_X_Pos = (WIDTH - playAgain.get_size()[0]) /2
    WINDOW.blit(playAgain, (playAgain_X_Pos, WIN_MESSAGE_Y_POS))

def main():
    global inputBoxText, alphabet, error_message_type, balance, bingo, win
    setNotConstantVariables()
    setCategory()
    setPriceForLetter()
    pygame.display.set_caption("NIEKoło NIEfortuny")
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.KEYDOWN):
                error_message_type = '0'
                if(event.key == pygame.K_BACKSPACE):
                    inputBoxText = inputBoxText[:-1]
                elif(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                    inputBoxText = inputBoxText.upper()
                    if(bingo):
                        if(inputBoxText == word):
                            win = True
                            inputBoxText = ''
                            break
                        else:
                            bingo = False
                            error_message_type = 3
                    elif(inputBoxText == 'BINGO'):
                        bingo = True
                    elif(inputBoxText not in alphabet):
                        error_message_type = 1
                        setPriceForLetter()
                    elif(inputBoxText in vowels):
                        if(balance >= 500):
                            alphabet.remove(inputBoxText)
                            balance -= 500
                        else:
                            error_message_type = 2
                        setPriceForLetter()
                    else:
                        alphabet.remove(inputBoxText)
                        guessedLetters.append(inputBoxText)
                        for char in range(len(word)):
                            if word[char] == inputBoxText:
                                balance += amount
                        setPriceForLetter()
                    inputBoxText = ''
                else:
                    inputBoxText += event.unicode    
        setBackground()
        setGameNameLogo()
        setGameDescription()
        setCategoryText()
        setWordPuzzle()
        setPriceForLetterText()
        setCurrentBalance()
        setTextBox()
        setErrorMessageBox()
        setWinMessage()
        pygame.display.update()
        if(win):
            sleep(10)
            break
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
                    inputBoxText = inputBoxText.upper()
                    if(inputBoxText == "TAK"):
                        return True
                    else:
                        return False
                else:
                    inputBoxText += event.unicode
        setBackground()
        setGameNameLogo()
        setGameDescription()
        setCategoryText()
        setWordPuzzle()
        setPriceForLetterText()
        setCurrentBalance()
        setTextBox()
        playAgainMessage()    
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    run = True
    while(run):
        run = main()
    pygame.quit()
        
