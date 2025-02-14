import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boy Running on the Road")

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
GREEN = (34, 139, 34)

road = pygame.Rect(0, HEIGHT // 2, WIDTH, 100)  
boy_image = pygame.image.load("boy_running.png")  
boy_image = pygame.transform.scale(boy_image, (80, 100))  

boy_x = 50
boy_y = HEIGHT // 2 - 10
boy_speed = 5

clock = pygame.time.Clock()

def main():
    global boy_x

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GREEN)

        pygame.draw.rect(screen, GRAY, road)

        screen.blit(boy_image, (boy_x, boy_y))

        boy_x += boy_speed
        if boy_x > WIDTH:  
            boy_x = -80

        pygame.display.flip()

        clock.tick(30)


if __name__ == "__main__":
    main()
