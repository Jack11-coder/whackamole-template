import pygame
import random
def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_position=(0,0)
        screen.fill("light blue")
        for xPos in range(32, 640, 32):
            pygame.draw.line(screen, "dark green", (xPos, 0), (xPos, 512))
        for yPos in range(32, 512, 32):
            pygame.draw.line(screen, "dark green", (0, yPos), (640, yPos))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if mole_image.get_rect(topleft=mole_position).collidepoint(event.pos):
                        # checks if mouse click is within the mole image rectangle
                        randX=random.randrange(0,640//32) * 32
                        randY=random.randrange(0,512//32) * 32
                        mole_position=(randX, randY)
                        screen.fill("light blue")
                        for xPos in range(32, 640, 32):
                            pygame.draw.line(screen, "dark green", (xPos, 0), (xPos, 512))
                        for yPos in range(32, 512, 32):
                            pygame.draw.line(screen, "dark green", (0, yPos), (640, yPos))
                        screen.blit(mole_image, mole_image.get_rect(topleft=mole_position))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
