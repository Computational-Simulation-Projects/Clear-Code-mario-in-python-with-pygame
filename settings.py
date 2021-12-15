level_map = [
    '                            ',
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX                         ',
    ' XXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64  # size of each tile

# screen size
screen_width = 1200
# height is determined by the number of rows in the map
screen_height = len(level_map) * tile_size
