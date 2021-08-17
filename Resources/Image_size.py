import pygame


def adaptive_image_proportion(width, height, position, dimensions, adjustments, image_to_draw, scale=1):
    image_proportion = width / height
    screen_proportion = dimensions[0] / dimensions[1]

    """This function uses the code from the image_proportion function to set the maximum image width
    and height based on the dimensions of the widget. This is then multiplied by the scale"""#

    if image_proportion > screen_proportion:
        image_width = dimensions[0] * scale
        image_height = (dimensions[0] * scale) / image_proportion
    else:
        image_height = dimensions[1] * scale
        image_width = (dimensions[1] * scale) * image_proportion

    """Given the adjustments (padding) these if statements check whether the adjustments would cause the
    image to go out of the widget and so adjust the dimensions of the image accordingly"""

    if adjustments[2] + image_width > dimensions[0]:
        image_width -= (adjustments[2] + image_width) - dimensions[0]
        image_height = image_width / image_proportion
    if adjustments[0] + image_height > dimensions[1]:
        image_height -= (adjustments[0] + image_height) - dimensions[1]
        image_width = image_height * image_proportion

    if adjustments[2] + image_width + adjustments[3] > dimensions[0]:
        image_width -= (adjustments[2] + image_width + adjustments[3]) - dimensions[0]
        image_height = image_width / image_proportion
    if adjustments[0] + image_height + adjustments[1] > dimensions[1]:
        image_height -= (adjustments[0] + image_height + adjustments[1]) - dimensions[1]
        image_width = image_height * image_proportion


    image_to_draw = pygame.transform.smoothscale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw


def image_proportion(width, height, dimensions, image_to_draw, scale=1):
    image_proportion = width / height
    screen_proportion = dimensions[0] / dimensions[1]

    """This function uses the image size and screen size to determine what the maximum size of the image
    can be for it to still fit in the widget. This is then multiplied by the scale in order to shrink the image"""

    if image_proportion > screen_proportion:
        image_width = dimensions[0] * scale
        image_height = (dimensions[0] * scale) / image_proportion
    else:
        image_height = dimensions[1] * scale
        image_width = (dimensions[1] * scale) * image_proportion

    image_to_draw = pygame.transform.smoothscale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw
