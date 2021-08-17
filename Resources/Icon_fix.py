import pygame
import os

pygame.init()
pygame.display.init()

icon_paths = "Icons"
icon_paths = os.path.abspath(icon_paths).replace(os.sep, "/")
for e, icon in enumerate(os.listdir(icon_paths)):
    icon_id = 42 + e
    fake_name = f"0{icon_id}-test{e}.png"
    icon_path = os.path.join(icon_paths, icon).replace(os.sep, "/")
    icon_to_draw = pygame.image.load(icon_path)

    alphas = pygame.surfarray.pixels_alpha(icon_to_draw)
    for y in range(icon_to_draw.get_height()):
        for x in range(icon_to_draw.get_width()):
            print(x, y, alphas[x, y])
            if 150 < alphas[x, y]:
                alphas[x, y] = 255
            elif alphas[x, y] <= 150:
                alphas[x, y] = 0

    del alphas
    pygame.image.save(icon_to_draw, os.path.join(icon_paths, fake_name).replace(os.sep, "/"))

