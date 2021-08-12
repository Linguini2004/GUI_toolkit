import pygame


def adaptive_image_proportion(width, height, position, dimensions, adjustments, image_to_draw, scale=1):
    image_proportion = width / height
    screen_proportion = dimensions[0] / dimensions[1]

    if image_proportion > screen_proportion:
        image_width = dimensions[0] * scale
        image_height = (dimensions[0] * scale) / image_proportion
    else:
        image_height = dimensions[1] * scale
        image_width = (dimensions[1] * scale) * image_proportion

    if adjustments[2] + image_width > dimensions[0]:
        image_width -= (adjustments[2] + image_width) - dimensions[0]
        image_height = image_width / image_proportion
    if adjustments[0] + image_height > dimensions[1]:
        image_height -= (adjustments[0] + image_height) - dimensions[1]
        image_width = image_height * image_proportion

    image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw


def image_proportion(width, height, dimensions, image_to_draw, scale=1):
    image_proportion = width / height
    screen_proportion = dimensions[0] / dimensions[1]

    if image_proportion > screen_proportion:
        image_width = dimensions[0] * scale
        image_height = (dimensions[0] * scale) / image_proportion
    else:
        image_height = dimensions[1] * scale
        image_width = (dimensions[1] * scale) * image_proportion

    image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw
