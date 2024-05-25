import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")


class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)


class Ball:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.dx = 5
        self.dy = 5

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Проверка столкновения с верхней и нижней границами
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def draw(self, surface):
        pygame.draw.ellipse(surface, WHITE, self.rect)

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = -self.dx


def main():
    paddle1 = Paddle(30, (HEIGHT - 100) // 2, 10, 100)
    paddle2 = Paddle(WIDTH - 40, (HEIGHT - 100) // 2, 10, 100)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 20)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Движение ракеток
        paddle1.move(pygame.K_w, pygame.K_s)
        paddle2.move(pygame.K_UP, pygame.K_DOWN)

        # Движение мяча
        ball.move()

        # Проверка столкновения мяча с ракетками
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx = -ball.dx

        # Проверка выхода мяча за границы экрана
        if ball.rect.left < 0 or ball.rect.right > WIDTH:
            ball.reset()

        # Обновление экрана
        screen.fill(BLACK)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)
        pygame.display.flip()

        # Задержка для управления FPS
        clock.tick(60)


if __name__ == "__main__":
    main()