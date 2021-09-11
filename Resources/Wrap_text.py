import pygame
from pygame import *
import time

def modifiable_wrap_text(surface, text, color, rect, font, align, cursor=False, aa=True, bkg=None):
    textAlignLeft = 0
    textAlignRight = 1
    textAlignCenter = 2
    textAlignBlock = 3

    full = False

    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for i, image in enumerate(imageList):
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if listOfWords[i] == "¦":
            lineLenList.append(font.render("¦", aa, color).get_width())
            lineList.append([])
        elif len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for line_num, (lineLen, lineImages) in enumerate(zip(lineLenList, lineList)):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages) - 1)
        lastLine += 1

        for i, image in enumerate(lineImages):
            x, y = lineLeft + i * spaceWidth, lineBottom

            if (lineBottom + fontHeight) - rect[1] < rect[3]:
                surface.blit(image, (round(x), y))
                if len(lineImages) == i + 1 and line_num + 1 == len(lineLenList) and time.time() % 1 > 0.5 and cursor and text != "":
                    cursor = font.render("|", aa, color)
                    surface.blit(cursor, (x + image.get_width(), lineBottom))

            lineLeft += image.get_width()
        lineBottom += fontHeight + lineSpacing

    return full

    '''
    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return
    
    '''

def static_wrap_text(text, color, rect, font, align, aa=True, bkg=None):
    textAlignLeft = 0
    textAlignRight = 1
    textAlignCenter = 2
    textAlignBlock = 3

    text_dict = {}

    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for i, image in enumerate(imageList):
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if listOfWords[i] == "¦":
            lineLenList.append(font.render("¦", aa, color).get_width())
            lineList.append([])
        elif len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages) - 1)
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i * spaceWidth, lineBottom
            text_dict[image] = [round(x), y]
            lineLeft += image.get_width()
        lineBottom += fontHeight + lineSpacing

    return text_dict

    '''
    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""
    '''