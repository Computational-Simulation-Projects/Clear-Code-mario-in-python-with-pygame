import pygame
from os import walk

# import all files in a folder and return a list of their names


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            if image.endswith('.png'):  # only import png files
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
    return surface_list
