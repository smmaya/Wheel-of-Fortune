import pygame

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG_COLOR = (44, 62, 80)
FPS = 60

pygame.display.set_caption("Koło NIEfortuny")

def setBackground():
    WIN.fill(BG_COLOR)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
        setBackground()
    pygame.quit()

if __name__ == "__main__":
    main()    