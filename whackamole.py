import pygame

# comment 
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            #vertical lines
            for i in range(10):
                pygame.draw.line(screen, "dark green", (i*64, 0), (i*64, 512))
            # horizontal lines
            for i in range (8):
                pygame.draw.line(screen, "dark green", (0, i * 64), (640, i * 64))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
