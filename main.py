import pygame

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
inputBoxText = 'text input box content to check position etc.'
INPUT_BOX_TEXT_POSITION = (60, 620) # X, Y

def setBackground():
    WINDOW.fill(BG_COLOR)

def setGameNameLogo():
    welcomeText = MAIN_FONT.render('Witamy w grze "Koło NIEfortuny"', 1, MAIN_FONT_COLOR)
    WINDOW.blit(welcomeText, GAME_NAME_LOGO_POSITION)

def setGameDescription():
    description1 = DESCRIPTION_FONT.render('Zgaduj po jednej literze na raz. Aby kupić samogłoskę, musisz mieć $500.', 1, DESCRIPTION_FONT_COLOR)
    description2 = DESCRIPTION_FONT.render('Jeśli sądzisz, że znasz całe słowo lub zdanie, wpisz \'bingo\' i wciśnij enter.', 1, DESCRIPTION_FONT_COLOR)
    description3 = DESCRIPTION_FONT.render('Następnie podaj słowo lub zdanie. Otrzymasz wtedy wartość każdej spółgłoski', 1, DESCRIPTION_FONT_COLOR)
    WINDOW.blit(description1, DESCRIPTION1_POSITION)
    WINDOW.blit(description2, DESCRIPTION2_POSITION)
    WINDOW.blit(description3, DESCRIPTION3_POSITION)

def setTextBox():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, INPUT_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, INPUT_BOX_FILL)
    textBoxContent = INPUT_BOX_FONT.render(inputBoxText, 1, INPUT_BOX_FONT_COLOR)
    WINDOW.blit(textBoxContent, INPUT_BOX_TEXT_POSITION)

def main():
    pygame.display.set_caption("Koło NIEfortuny")
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
        setBackground()
        setGameNameLogo()
        setGameDescription()
        setTextBox()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()    