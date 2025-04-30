from settings import *
from cookie import Cookie
from upgrade import Upgrade


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Cookie Clicker')
        self.running = True
        self.clock = pygame.time.Clock()

        self.game_font = pygame.font.Font(join('fonts', 'Chewy.ttf'), 70)
        self.cps_font = pygame.font.Font(join('fonts', 'Chewy.ttf'), 40)
        self.desc_font = pygame.font.Font(join('fonts', 'Chewy.ttf'), 20)

        self.cookies = 583
        self.cookies_per_second = 0

        self.add_cps_event = pygame.event.custom_type()
        pygame.time.set_timer(self.add_cps_event, 1000)

        self.all_sprites = pygame.sprite.Group()

        self.cookie = Cookie(
            (WINDOW_WIDTH - 1600, WINDOW_HEIGHT // 2), self, self.all_sprites
        )

        self.cursor_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 1100)
        self.cursor_init_cost = 15
        self.cursor_cps_gain = 0.1
        self.cursor_desc = 'Click faster with autoclicks.'
        self.cursor = Upgrade(
            'Cursor',
            self.cursor_pos,
            self.cursor_init_cost,
            self.cursor_cps_gain,
            'cursor.png',
            self.cursor_desc,
            self,
            self.all_sprites,
        )

        self.grandma_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 1100)
        self.grandma_init_cost = 80
        self.grandma_cps_gain = 1
        self.grandma_desc = 'Grandma bakes cookies. A lot.'
        self.grandma = Upgrade(
            'Grandma',
            self.grandma_pos,
            self.grandma_init_cost,
            self.grandma_cps_gain,
            'grandma.png',
            self.grandma_desc,
            self,
            self.all_sprites,
        )

        self.farm_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 1100)
        self.farm_init_cost = 400
        self.farm_cps_gain = 8
        self.farm_desc = 'Farming cookies. Great idea!'
        self.farm = Upgrade(
            'Farm',
            self.farm_pos,
            self.farm_init_cost,
            self.farm_cps_gain,
            'farm.png',
            self.farm_desc,
            self,
            self.all_sprites,
        )

        self.mine_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 950)
        self.mine_init_cost = 2500
        self.mine_cps_gain = 47
        self.mine_desc = 'Digging deep for more cookies.'
        self.mine = Upgrade(
            'Mine',
            self.mine_pos,
            self.mine_init_cost,
            self.mine_cps_gain,
            'mine.png',
            self.mine_desc,
            self,
            self.all_sprites,
        )

        self.factory_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 950)
        self.factory_init_cost = 15000
        self.factory_cps_gain = 260
        self.factory_desc = 'Factory workers love cookies.'
        self.factory = Upgrade(
            'Factory',
            self.factory_pos,
            self.factory_init_cost,
            self.factory_cps_gain,
            'factory.png',
            self.factory_desc,
            self,
            self.all_sprites,
        )

        self.bank_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 950)
        self.bank_init_cost = 100000
        self.bank_cps_gain = 1400
        self.bank_desc = 'Cookies while you nap.'
        self.bank = Upgrade(
            'Bank',
            self.bank_pos,
            self.bank_init_cost,
            self.bank_cps_gain,
            'bank.png',
            self.bank_desc,
            self,
            self.all_sprites,
        )

        self.temple_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 800)
        self.temple_init_cost = 750000
        self.temple_cps_gain = 7800
        self.temple_desc = 'Divine powers bake cookies.'
        self.temple = Upgrade(
            'Temple',
            self.temple_pos,
            self.temple_init_cost,
            self.temple_cps_gain,
            'temple.png',
            self.temple_desc,
            self,
            self.all_sprites,
        )

        self.wizard_tower_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 800)
        self.wizard_tower_init_cost = 5000000
        self.wizard_tower_cps_gain = 44000
        self.wizard_tower_desc = 'Wizards + cookies = magic.'
        self.wizard = Upgrade(
            'Wizard Tower',
            self.wizard_tower_pos,
            self.wizard_tower_init_cost,
            self.wizard_tower_cps_gain,
            'wizard_tower.png',
            self.wizard_tower_desc,
            self,
            self.all_sprites,
        )

        self.shipment_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 800)
        self.shipment_init_cost = 30000000
        self.shipment_cps_gain = 260000
        self.shipment_desc = 'Ship cookies across the world.'
        self.shipment = Upgrade(
            'Shipment',
            self.shipment_pos,
            self.shipment_init_cost,
            self.shipment_cps_gain,
            'shipment.png',
            self.shipment_desc,
            self,
            self.all_sprites,
        )

        self.alchemy_lab_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 650)
        self.alchemy_lab_init_cost = 200000000
        self.alchemy_lab_cps_gain = 1600000
        self.alchemy_lab_desc = 'Turn stuff into cookies. Magic.'
        self.alchemy_lab = Upgrade(
            'Alchemy Lab',
            self.alchemy_lab_pos,
            self.alchemy_lab_init_cost,
            self.alchemy_lab_cps_gain,
            'alchemy_lab.png',
            self.alchemy_lab_desc,
            self,
            self.all_sprites,
        )

        self.portal_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 650)
        self.portal_init_cost = 1000000000
        self.portal_cps_gain = 10000000
        self.portal_desc = 'Portals = infinite cookies.'
        self.portal = Upgrade(
            'Portal',
            self.portal_pos,
            self.portal_init_cost,
            self.portal_cps_gain,
            'portal.png',
            self.portal_desc,
            self,
            self.all_sprites,
        )

        self.time_machine_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 650)
        self.time_machine_init_cost = 6000000000
        self.time_machine_cps_gain = 65000000
        self.time_machine_desc = 'Time travel = cookies now.'
        self.time_machine = Upgrade(
            'Time Machine',
            self.time_machine_pos,
            self.time_machine_init_cost,
            self.time_machine_cps_gain,
            'time_machine.png',
            self.time_machine_desc,
            self,
            self.all_sprites,
        )

        self.antimatter_condenser_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 650)
        self.antimatter_condenser_init_cost = 25000000000
        self.antimatter_condenser_cps_gain = 430000000
        self.antimatter_condenser_desc = 'Harness antimatter for cookies.'
        self.antimatter_condenser = Upgrade(
            'Antimatter Condenser',
            self.antimatter_condenser_pos,
            self.antimatter_condenser_init_cost,
            self.antimatter_condenser_cps_gain,
            'antimatter_condenser.png',
            self.antimatter_condenser_desc,
            self,
            self.all_sprites,
        )

        self.prism_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 500)
        self.prism_init_cost = 100000000000
        self.prism_cps_gain = 2900000000
        self.prism_desc = 'Bend light, bake cookies faster.'
        self.prism = Upgrade(
            'Prism',
            self.prism_pos,
            self.prism_init_cost,
            self.prism_cps_gain,
            'prism.png',
            self.prism_desc,
            self,
            self.all_sprites,
        )

        self.chancemaker_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 500)
        self.chancemaker_init_cost = 450000000000
        self.chancemaker_cps_gain = 21000000000
        self.chancemaker_desc = 'Chance = more cookies per sec.'
        self.chancemaker = Upgrade(
            'Chancemaker',
            self.chancemaker_pos,
            self.chancemaker_init_cost,
            self.chancemaker_cps_gain,
            'chancemaker.png',
            self.chancemaker_desc,
            self,
            self.all_sprites,
        )

        self.fractal_engine_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 500)
        self.fractal_engine_init_cost = 2000000000000
        self.fractal_engine_cps_gain = 150000000000
        self.fractal_engine_desc = 'Fractals help cookies grow.'
        self.fractal_engine = Upgrade(
            'Fractal Engine',
            self.fractal_engine_pos,
            self.fractal_engine_init_cost,
            self.fractal_engine_cps_gain,
            'fractal_engine.png',
            self.fractal_engine_desc,
            self,
            self.all_sprites,
        )

        self.js_console_pos = (WINDOW_WIDTH - 1000, WINDOW_HEIGHT - 350)
        self.js_console_init_cost = 9000000000000
        self.js_console_cps_gain = 1100000000000
        self.js_console_desc = 'Code cookies into existence.'
        self.js_console = Upgrade(
            'Javascript Console',
            self.js_console_pos,
            self.js_console_init_cost,
            self.js_console_cps_gain,
            'js_console.png',
            self.js_console_desc,
            self,
            self.all_sprites,
        )

        self.idleverse_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 350)
        self.idleverse_init_cost = 40000000000000
        self.idleverse_cps_gain = 8300000000000
        self.idleverse_desc = 'The idleverse bakes cookies.'
        self.idleverse = Upgrade(
            'Idleverse',
            self.idleverse_pos,
            self.idleverse_init_cost,
            self.idleverse_cps_gain,
            'idleverse.png',
            self.idleverse_desc,
            self,
            self.all_sprites,
        )

        self.cortex_baker_pos = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 350)
        self.cortex_baker_init_cost = 150000000000000
        self.cortex_baker_cps_gain = 64000000000000
        self.cortex_baker_desc = 'AI bakes cookies with brains.'
        self.cortex_baker = Upgrade(
            'Cortex Baker',
            self.cortex_baker_pos,
            self.cortex_baker_init_cost,
            self.cortex_baker_cps_gain,
            'cortex_baker.png',
            self.cortex_baker_desc,
            self,
            self.all_sprites,
        )

        self.you_pos = (WINDOW_WIDTH - 600, WINDOW_HEIGHT - 200)
        self.you_init_cost = 600000000000000
        self.you_cps_gain = 510000000000000
        self.you_desc = 'Clone yourself for cookies.'
        self.you = Upgrade(
            'You',
            self.you_pos,
            self.you_init_cost,
            self.you_cps_gain,
            'you.png',
            self.you_desc,
            self,
            self.all_sprites,
        )

    def run(self):
        self.clock.tick()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.add_cps_event:
                    self.add_cps_to_cookies()

            self.display_surface.fill(BG_COLOR)
            self.all_sprites.update()
            self.all_sprites.draw(self.display_surface)
            self.display_cookie_count()
            self.display_cps()
            pygame.display.flip()

    def format_number(self, num, decimals=3, abbreviate=False):
        suffix = ''
        og_num = num

        suffixes = [
            '',
            '',
            ' million',
            ' billion',
            ' trillion',
            ' quadrillion',
            ' quintillion',
            ' sextillion',
            ' septillion',
            ' octillion',
            ' nonillion',
            ' decillion',
            ' undecillion',
            ' duodecillion',
            ' tredecillion',
            ' quattuordecillion',
            ' quindecillion',
            ' sexdecillion',
            ' septendecillion',
            ' octodecillion',
            ' novemdecillion',
            ' vigintillion',
            ' unvigintillion',
            ' duovigintillion',
            ' trevigintillion',
            ' quattuorvigintillion',
            ' quinvigintillion',
            ' sexvigintillion',
            ' septenvigintillion',
            ' octovigintillion',
            ' novemvigintillion',
            ' trigintillion',
            ' untrigintillion',
            ' duotrigintillion',
            ' googol',
        ]

        abbreviated_suffixes = [
            '',
            '',
            'M',
            'B',
            'T',
            'Qa',
            'Qi',
            'Sx',
            'Sp',
            'Oc',
            'No',
            'Dc',
            'Ud',
            'Dd',
            'Td',
            'Qad',
            'Qid',
            'Sxd',
            'Spd',
            'Ocd',
            'Nod',
            'Vg',
            'UVg',
            'DVg',
            'TVg',
            'QaVg',
            'QiVg',
            'SxVg',
            'SpVg',
            'OcVg',
            'NoVg',
            'Tg',
            'UTg',
            'DTg',
            'Gg',
        ]

        if abbreviate:
            suffixes = abbreviated_suffixes

        if num < 1_000_000:
            formatted_num = f'{num:,.{decimals}f}'.rstrip('0').rstrip('.')
            return formatted_num

        index = 0

        while num >= 1000 and index < len(suffixes) - 1:
            num /= 1000.0
            index += 1

        if 10**100 <= og_num < 10**103:
            num /= 10
            formatted_num = f'{num:,.{decimals}f}'.rstrip('0').rstrip('.')
            return f'{formatted_num}{suffixes[index]}'

        if index >= len(suffixes):
            return f'{num:.{decimals}e}'

        suffix = suffixes[index - 1]
        formatted_num = f'{num:,.{decimals}f}'.rstrip('0').rstrip('.')
        return f'{formatted_num}{suffixes[index]}'

    def increase_cookie_count(self):
        self.cookies += 1.0

    def add_cps_to_cookies(self):
        self.cookies += self.cookies_per_second

    def display_cookie_count(self):
        formatted_cookies = self.format_number(int(self.cookies))
        cookie_count_text = self.game_font.render(
            f'{formatted_cookies} {'cookie' if int(self.cookies) == 1 else 'cookies'}',
            True,
            SCORE_COLOR,
        )
        cookie_count_rect = cookie_count_text.get_frect(
            center=(WINDOW_WIDTH - 1600, WINDOW_HEIGHT - 1000)
        )
        self.display_surface.blit(cookie_count_text, cookie_count_rect)

    def display_cps(self):
        formatted_cps = self.format_number(self.cookies_per_second, decimals=1)
        cps_text = self.cps_font.render(
            f'per second: {formatted_cps}', True, SCORE_COLOR
        )
        cps_rect = cps_text.get_frect(center=(WINDOW_WIDTH - 1600, WINDOW_HEIGHT - 900))
        self.display_surface.blit(cps_text, cps_rect)


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
