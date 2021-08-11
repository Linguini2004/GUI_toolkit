import pygame


def adaptive_image_proportion(width, height, position, dimensions, adjustments, scale, image_to_draw):
    proportion = width / height
    mod_dim = list(dimensions)

    if width > height:
        image_width = dimensions[0]
        image_height = image_width / proportion
    else:
        image_height = dimensions[1]
        image_width = image_height * proportion
    '''
    if adjustments[2] + image_width > dimensions[0]:
        mod_dim[0] -= (adjustments[2] + image_width) - dimensions[0]
        image_width = mod_dim[0]
        image_height = image_width / proportion
    if adjustments[0] + image_height > dimensions[1]:
        mod_dim[1] -= (adjustments[0] + image_height) - dimensions[1]
        image_height = mod_dim[1]
        image_width = image_height * proportion
    if adjustments[2] + image_width > dimensions[0] and adjustments[0] + image_height > dimensions[1]:
        mod_dim[0] -= (adjustments[2] + image_width) - dimensions[0]
        mod_dim[1] -= (adjustments[0] + image_height) - dimensions[1]
    '''
    print("width_over", (adjustments[2] + image_width) - dimensions[0])
    print("height_over", (adjustments[0] + image_height) - dimensions[1])

    if (adjustments[2] + image_width) - dimensions[0] > (adjustments[0] + image_height) - dimensions[1]:
        # print("debug0")
        print("before", mod_dim[0])
        mod_dim[0] -= (adjustments[2] + image_width) - dimensions[0]
        print("after", mod_dim[0])
        image_width = mod_dim[0]
        image_height = image_width / proportion
    else:
        # print("debug1")
        mod_dim[1] -= (adjustments[0] + image_height) - dimensions[1]
        image_height = mod_dim[1]
        image_width = image_height * proportion

    image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    '''
    if dimensions[0] > dimensions[1]:
        image_height = dimensions[1] * scale
        image_width = image_height * proportion
        #print(image_width, image_height)
        if adjustments[2] + image_width > dimensions[0]:
            #print("debug1")

            #print(adjustments[2], dimensions[0])

            #print("before", dimensions[0])
            print("total_width", adjustments[2] + image_width)
            mod_dim[0] -= (adjustments[2] + image_width) - dimensions[0]
            #print("after", dimensions[0])

            print(dimensions)
            print(mod_dim)
            #image_height = mod_dim[1] * scale
            #image_width = image_height * proportion

            image_width = mod_dim[0]
            image_height = image_width / proportion

        if adjustments[0] + image_height > dimensions[1]:
            #print("debug2")

            #print(adjustments[0], dimensions[1])

            mod_dim[1] -= (adjustments[0] + image_height) - dimensions[1]
            image_height = ((mod_dim[1] * scale) / height) * height
            image_width = image_height * proportion

        image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

        # DONT NEED TO DO LINE 16 AND 17 IF NOT LINE 9 OR 10
        #if adjustments[2] + image_width + adjustments[3] > dimensions[0]:
        #    dimensions[0] -= (position[0] + )
        
    
    else: 
        image_width = ((dimensions[0] * scale) / width) * width
        image_height = image_width / proportion
        if adjustments[2] + image_width > dimensions[0]:
            dimensions[0] -= (position[0] + image_width) - dimensions[0]
        if adjustments[0] + image_height > dimensions[1]:
            dimensions[1] -= (position[1] + image_width) - dimensions[1]
        image_width = ((dimensions[0] * scale) / width) * width
        image_height = image_width / proportion

    '''
    return image_to_draw


def image_proportion(width, height, dimensions, image_to_draw):
    image_proportion = width / height
    screen_proportion = dimensions[0] / dimensions[1]
    relationship = image_proportion / screen_proportion

    width_ratio = width / dimensions[0]
    height_ratio = height / dimensions[1]

    print("relationship", image_proportion, screen_proportion)

    print("width", width, dimensions[0], width - dimensions[0])
    print("height", height, dimensions[1], height - dimensions[1])

    # if dimensions[0] > dimensions[1]:
    #    if width > height:

    #if dimensions[0] > dimensions[1]:

    if image_proportion > screen_proportion:
        image_width = dimensions[0]
        image_height = dimensions[0] / image_proportion
    else:
        image_height = dimensions[1]
        image_width = dimensions[1] * image_proportion

    ''''
    else:
        if image_proportion > screen_proportion:
            image_width = dimensions[0]
            image_height = dimensions[0] / image_proportion
        else:
            image_height = dimensions[1]
            image_width = dimensions[1] * image_proportion
            
    '''

    '''
    if image_proportion < screen_proportion:
        if width - dimensions[0] < height - dimensions[1]:
            image_width = dimensions[0]
            image_height = dimensions[0] / image_proportion
        else:
            image_height = dimensions[1]
            image_width = dimensions[1] * image_proportion
    else:
        if width - dimensions[0] > height - dimensions[1]:
            image_width = dimensions[0]
            image_height = dimensions[0] / image_proportion
        else:
            image_height = dimensions[1]
            image_width = dimensions[1] * image_proportion
    '''

    '''
    if dimensions[0] > dimensions[1]:
        if width > height:
            image_width = dimensions[0]
            image_height = image_width / image_proportion
        else:
            image_height = dimensions[1]
            image_width = image_height * image_proportion
    '''
    image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    # image_width = dimensions[0]
    # image_height = image_width / proportion
    # image_to_draw = pygame.transform.scale(image_to_draw, (int(image_width), int(image_height)))

    return image_to_draw
