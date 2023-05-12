from pygame import *
game_over = True
win_width = 700
win_height = 500
mw = display.set_mode((win_width, win_height))
clock = time.Clock()
FPS = 60

racket_x1 = 10
racket_y1 = 200 

racket_x2 = 400
racket_y2 = 200

display.set_caption('Пинг-понг')
LIGHT_BLUE = 200, 255, 255
mw.fill(LIGHT_BLUE)
'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_down] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_up] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
'''
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = Rect(x,y,width,height)
        self.fill_color = LIGHT_BLUE
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        self.frame_color = frame_color
        draw.rect(mw, self.frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x, y, width, height)
        self.image = image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label():
    def __init__(self, x, y, width, height, color):
        self.rect = Rect(x,y,width,height)
        self.fill_color = color

    def set_text(self,text,fsize,text_color):
        self.text = text
        self.image = font.Font(None, fsize).render(text, True, text_color)

    def draw(self,shift_x, shift_y):
        draw.rect(mw,self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

ball = Picture('ball.png', 10, 10, 1, 1)
plat1 = Picture('platform.png', racket_x1, racket_y1, 100, 30)
plat2 = Picture('platform.png', racket_x2, racket_y2, 100, 30)

move_up = False
move_down = False
move_w = False
move_s = False

while game_over:
    ball.fill()
    plat1.fill()
    plat2.fill()

    for e in event.get():
        if e.type == QUIT:
           game_over = False
        if e.type == KEYDOWN:
            if e.key == K_UP:
                move_up = True
            if e.key == K_DOWN:
                move_down = True
            if e.key == K_w:
                move_w = True
            if e.key == K_s:
                move_s = True
        elif e.type == KEYUP:
            if e.key == K_UP:
                move_up = False
            if e.key == K_DOWN:
                move_down = False
            if e.key == K_w:
                move_w = False
            if e.key == K_s:
                move_s = False
    if move_up:
        plat1.rect.y -= 3
    if move_down:
        plat1.rect.y += 3

    if move_w:
        plat2.rect.y -= 3
    if move_s:
        plat2.rect.y += 3


    plat2.draw()
    plat1.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)