from settings import *


class Upgrade(pygame.sprite.Sprite):
    def __init__(
        self, name, pos, init_cost, cps_gain, filename, desc_text, game, groups
    ):
        super().__init__(groups)
        self.name = name
        self.pos = pos
        self.game = game
        self.cost = init_cost
        self.init_cost = init_cost
        self.cps_gain = cps_gain
        self.desc_text = desc_text
        self.upgrade_num = 0

        self.og_image = pygame.image.load(join('images', filename)).convert_alpha()
        scaled_image = pygame.transform.scale_by(self.og_image, 0.33)

        self.img_border = 6
        w, h = scaled_image.get_size()
        self.image = pygame.Surface(
            (w + self.img_border + 250, h + self.img_border), pygame.SRCALPHA
        )
        self.image.fill('#FFFFFF')

        self.image.blit(scaled_image, (self.img_border // 2, self.img_border // 2))

        self.rect = self.image.get_frect(center=pos)

        self.desc = self.game.desc_font.render(
            f'{self.name}: {self.upgrade_num}\nCPS: {self.game.format_number(self.cps_gain, abbreviate=True)}\n{self.desc_text}\nCost: {self.game.format_number(self.cost, abbreviate=True)} cookies',
            True,
            UPGRADES_TEXT_COLOR,
        )
        self.desc_rect = self.desc.get_frect(
            topleft=(scaled_image.get_width() + 12, 10)
        )

        self.image.blit(self.desc, self.desc_rect)

    def get_input(self):
        mouse_btns = pygame.mouse.get_just_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if mouse_btns[0] and self.game.cookies >= self.cost:
                self.game.cookies_per_second += self.cps_gain
                self.game.cookies -= self.cost
                self.upgrade_num += 1
                self.cost = round(self.init_cost * (pow(1.15, self.upgrade_num)))
                self.update_description()

    def update_description(self):
        self.image.fill('#FFFFFF')
        scaled_image = pygame.transform.scale_by(self.og_image, 0.33)
        self.image.blit(scaled_image, (self.img_border // 2, self.img_border // 2))

        self.desc = self.game.desc_font.render(
            f'{self.name}: {self.upgrade_num}\nCPS: {self.game.format_number(self.cps_gain, abbreviate=True)}\n{self.desc_text}\nCost: {self.game.format_number(self.cost, abbreviate=True)} cookies',
            True,
            UPGRADES_TEXT_COLOR,
        )
        self.desc_rect = self.desc.get_frect(
            topleft=(scaled_image.get_width() + 12, 10)
        )
        self.image.blit(self.desc, self.desc_rect)

    def update(self):
        self.get_input()
