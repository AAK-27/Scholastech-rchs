import pygame

class Player():
    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.velX = 0
        self.velY = 0

    
    def draw(self, surface):
        pygame.draw.rect(surface, "orange", (self.posX-5, self.posY-20, 10, 20))
    
    def update(self, fps):
        self.velY += 9.8/fps
        self.posY += self.velY
        self.posX += self.velX

pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Platformer!")
clock = pygame.time.Clock()
fps = 30
player = Player(30, 30)

while True:
    pygame.display.set_caption("Platformer   |   " + str(int(clock.get_fps())) + "FPS")
    window.fill('green')
    pygame.draw.rect(window, "blue", (200, 200, 200, 100))
    pygame.draw.circle(window, "red", (250, 250), 25)
    player.draw(window)
    player.update(fps)
    if player.posY > 500:
        player.posY = 500
        player.velY = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                player.velX = -5
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                player.velX = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_LEFT):
                player.velX = 0
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                player.velX = 0
    pygame.display.update()
    clock.tick(fps)