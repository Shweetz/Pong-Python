
import pygame

# === Variables (w=100, h=100, fr=1 for collision test)
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
FRAMERATE = 1000
CHEAT_MODE = False

fgColor = pygame.Color("white")
bgColor = pygame.Color("black")
wallColor = pygame.Color("orange")
ballColor = pygame.Color("green")
paddleColor = pygame.Color("blue")


# === Classes
class Ball:
    RADIUS = 20

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = ballColor
        self.show(self.color)

    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), Ball.RADIUS)

    def update(self):
        # global fgColor, bgColor
        # Hide previous ball position
        self.show(bgColor)

        # Update and show next ball position
        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx - Ball.RADIUS < BORDER:
            self.vx = -self.vx
        if newy - Ball.RADIUS < BORDER or newy + Ball.RADIUS > HEIGHT - BORDER:
            self.vy = -self.vy
        if newx + Ball.RADIUS > WIDTH - Paddle.WIDTH and abs(newy - paddle.y) < Paddle.HEIGHT//2 + Ball.RADIUS:
            self.vx = -self.vx

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y
        self.color = paddleColor
        self.show(self.color)

    def show(self, color):
        global screen
        rect = pygame.Rect(WIDTH - self.WIDTH, self.y - self.HEIGHT//2, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(screen, color, rect)

    def update(self):
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        if self.y < BORDER + Paddle.HEIGHT//2:
            self.y = BORDER + Paddle.HEIGHT//2
        if self.y > HEIGHT - BORDER - Paddle.HEIGHT//2:
            self.y = HEIGHT - BORDER - Paddle.HEIGHT//2
        self.show(self.color)


# === Draw the scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Walls
pygame.draw.rect(screen, wallColor, pygame.Rect(0, 0, WIDTH, BORDER))
pygame.draw.rect(screen, wallColor, pygame.Rect(0, 0, BORDER, HEIGHT))
pygame.draw.rect(screen, wallColor, pygame.Rect(0, HEIGHT-BORDER, WIDTH, HEIGHT))

# Ball
ball = Ball(WIDTH - Ball.RADIUS - Paddle.WIDTH, HEIGHT//2, -VELOCITY, -VELOCITY)

# Paddle
paddle = Paddle(HEIGHT//2)

# Frame rate
clock = pygame.time.Clock()

# === Game loop
while True:
    if CHEAT_MODE:
        clock.tick(FRAMERATE * (WIDTH - ball.x) / WIDTH)
    else:
        clock.tick(FRAMERATE)

    ball.update()
    paddle.update()
    # Display everything
    pygame.display.flip()

    # === Event queue
    e = pygame.event.poll()

    # Key press
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_UP:
            if FRAMERATE < 10:
                FRAMERATE += 1
            else:
                FRAMERATE *= 1.1
            if FRAMERATE > 1000:
                FRAMERATE = 1000
            print("up", FRAMERATE)
        if e.key == pygame.K_DOWN:
            FRAMERATE //= 1.1
            if FRAMERATE < 1:
                FRAMERATE = 1
            print("down", FRAMERATE)

    # Exit
    if e.type == pygame.QUIT:
        pygame.quit()
