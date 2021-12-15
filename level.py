import pygame
from player import Player

from tiles import Tile
from settings import tile_size
from player import Player


class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout_data):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout_data):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

                elif col == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def run(self):
      # level tiles
        self.tiles.update(self.world_shift)  # update the tiles horizontally
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()  # update the player
        self.player.draw(self.display_surface)
