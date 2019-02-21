import pygame
import random

background = (115, 255, 220)

screen_width = 700
screen_height = 500


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0


def make_ball():
    ball = Ball()
    ball.radius = random.randrange(15, 60)
    ball.x = random.randrange(ball.radius, screen_width - ball.radius)
    ball.y = random.randrange(ball.radius, screen_height - ball.radius)
    ball.dx = random.randrange(1, 7)
    ball.dy = random.randrange(1, 7)
    ball.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    return ball


def main():
    pygame.init()
    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Flying Balls")
    done = False
    clock = pygame.time.Clock()
    ball_list = []

    for _ in range(10):
        ball = make_ball()
        ball_list.append(ball)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        for ball in ball_list:
            ball.x += ball.dx
            ball.y += ball.dy

            if ball.y > screen_height - ball.radius or ball.y < ball.radius:
                ball.dy = - ball.dy
            if ball.x > screen_width - ball.radius or ball.x < ball.radius:
                ball.dx = - ball.dx

        screen.fill(background)

        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.radius)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
