from settings import *


class Cookie(pygame.sprite.Sprite):
    def __init__(self, pos, game, groups):
        super().__init__(groups)
        self.og_image = pygame.image.load(join('images', 'cookie.png')).convert_alpha()
        self.image = self.og_image
        self.rect = self.image.get_frect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.game = game

        self.scale_factor = 1.0
        self.target_scale = 1.0
        self.scaling = False
        self.scaling_up = False
        self.scale_speed = 0.02
        self.scale_duration = 15
        self.frame_counter = 0

    def get_input(self):
        mouse_btns = pygame.mouse.get_just_pressed()
        mouse_pos = pygame.mouse.get_pos()

        sprite_x = mouse_pos[0] - self.rect.x
        sprite_y = mouse_pos[1] - self.rect.y

        try:
            if self.mask.get_at((sprite_x, sprite_y)):
                if mouse_btns[0] and not self.scaling:
                    self.game.increase_cookie_count()
                    self.target_scale = uniform(1.1, 1.2)
                    self.scaling = True
                    self.scaling_up = True
                    self.frame_counter = 0
        except IndexError:
            pass

    def scale_cookie(self):
        if self.scaling:

            if self.scaling_up:
                if self.scale_factor < self.target_scale:
                    self.scale_factor += self.scale_speed
                    if self.scale_factor >= self.target_scale:
                        self.scale_factor = self.target_scale

                self.frame_counter += 1
                if self.frame_counter > self.scale_duration:
                    self.target_scale = 1.0
                    self.scaling_up = False
            else:
                if self.scale_factor > self.target_scale:
                    self.scale_factor -= self.scale_speed
                    if self.scale_factor <= self.target_scale:
                        self.scale_factor = self.target_scale
                        self.scaling = False
                else:
                    self.scale_factor = self.target_scale
                    self.scaling = False

        self.image = pygame.transform.rotozoom(self.og_image, 0, self.scale_factor)
        self.rect = self.image.get_frect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.get_input()
        self.scale_cookie()
