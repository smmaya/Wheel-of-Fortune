import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

BG_COLOR = (44, 62, 80)

MAIN_FONT = pygame.font.SysFont('Lato', 40)
MAIN_FONT_COLOR = (241, 196, 15)

INPUT_BOX = pygame.Rect(100, 100, 240, 60)
INPUT_BOX_COLOR = (243, 156, 18)
INPUT_BOX_FILL = pygame.Rect(103, 103, 234, 54)

def setBackground():
    WINDOW.fill(BG_COLOR)

def setGameNameLogo():
    welcomeText = MAIN_FONT.render('Witamy w grze "Koło NIEfortuny"', 1, MAIN_FONT_COLOR)
    WINDOW.blit(welcomeText, (10, 10))

def setTextBox():
    pygame.draw.rect(WINDOW, INPUT_BOX_COLOR, INPUT_BOX)
    pygame.draw.rect(WINDOW, BG_COLOR, INPUT_BOX_FILL)

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
        setTextBox()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()    