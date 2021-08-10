import pygame

def adaptive_image_proportion(width, height, position, dimensions, adjustments, scale, image_to_draw):
    proportion = width / height
    if dimensions[0] > dimensions[1]:
        image_height = ((dimensions[1] * scale) / height) * height
        image_width = image_height * proportion
        if adjustments[0] + image_width > dimensions[0]:
            dimensions[0] -= (position[0] + image_width) - dimensions[0]
        if adjustments[1] + image_height > dimensions[1]:
            dimensions[1] -= (position[1] + image_width) - dimensions[1]
        image_width = (dimensions[0] / width) * width
        image_height = image_width / proportion
        image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    else:
        image_width = ((dimensions[0] * scale) / width) * width
        image_height = image_width / proportion
        if adjustments[0] + image_width > dimensions[0]:
            dimensions[0] -= (position[0] + image_width) - dimensions[0]
        if adjustments[1] + image_height > dimensions[1]:
            dimensions[1] -= (position[1] + image_width) - dimensions[1]
        image_width = ((dimensions[0] * scale) / width) * width
        image_height = image_width / proportion
        image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw

def image_proportion(width, height, dimensions, image_to_draw):
    proportion = width / height
    if dimensions[0] > dimensions[1]:
        image_height = (dimensions[1] / height) * height
        image_width = image_height * proportion
        image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))
    else:
        image_width = (dimensions[0] / width) * width
        image_height = image_width / proportion
        image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw