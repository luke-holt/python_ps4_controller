import pygame
from pygame import key, joystick
import json, os
from game_math import Point2D, Hitbox


class PlayerSquare:
    def __init__(self, width, height, pos, color=(255, 255, 255)):
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color

    def center_origin(self):
        self.pos = Point2D(self.pos.x - self.width / 2, self.pos.y - self.height / 2)

    def get_hitbox(self):
        return (
            Point2D(self.pos.x, self.pos.y),
            Point2D(self.pos.x, self.pos.y + self.height),
            Point2D(self.pos.x + self.pos.x, self.pos.y),
            Point2D(self.pos.x + self.pos.x, self.pos.y + self.height),
        )

    def get_details(self):
        return (
            self.pos.x,
            self.pos.y,
            self.width,
            self.height,
        )


# Load up window and initialize joysticks
pygame.init()
SIZE = WIDTH, HEIGHT = (600, 400)
FPS = 60
frame = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("PS4 Controller Test")
clock = pygame.time.Clock()

# Initialize controller(s)
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

# Load json file with button mappings
with open(os.path.join("mapping.json"), "r+") as file:
    ds_buttons = json.load(file)
# Dict for analog interactions
ds_joysticks = {
    0: 0,  # Left joystick horizontal
    1: 0,  # Left joystick vertical
    2: 0,  # Right joystick horizontal
    3: 0,  # Right joystick vertical
    4: -1,  # Left trigger
    5: -1,  # Right trigger
}

# Player square sprite
width = 15
height = 15
x = (WIDTH - width) / 2
y = (HEIGHT - height) / 2
speed = 5

player = PlayerSquare(15, 15, Point2D(WIDTH / 2, HEIGHT / 2))
player.center_origin()

rh = 0
rv = 0

while True:
    s = speed
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.JOYBUTTONDOWN:
            if ds_buttons["X"] == event.button:
                print("JUMP")
                pass
        if event.type == pygame.JOYAXISMOTION:
            # Updates when there is a change in joystick states
            ds_joysticks[event.axis] = event.value if abs(event.value) > 0.1 else 0

            if event.axis == 2:
                rh = ds_joysticks[event.axis]
            if event.axis == 3:
                rv = ds_joysticks[event.axis]

    player.pos += Point2D(s * rh, s * rv)
    # player.pos.x += s * rh
    # player.pos.y += s * rv

    # keys = pygame.key.get_pressed()

    # if keys[pygame.K_LEFT]:
    #     x -= s
    # if keys[pygame.K_RIGHT]:
    #     x += s
    # if keys[pygame.K_UP]:
    #     y -= s
    # if keys[pygame.K_DOWN]:
    #     y += s

    if x < 0:
        x = 0
    elif x > (WIDTH - width):
        x = WIDTH - width
    if y < 0:
        y = 0
    elif y > (HEIGHT - height):
        y = HEIGHT - height

    frame.fill(pygame.Color("black"))
    pygame.draw.rect(frame, player.color, player.get_details())
    pygame.display.update()


# if __name__ == "__main__":
#     main()
