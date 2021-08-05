# This is one of the widgets
# This widget simply blits text onto the screen
import pygame
from Resources.Wrap_text import wrap_text
from pygame import *

class Text:
    def __init__(self):
        self.text_colour = (255, 255, 255)
        self.text = ""
        self.font = "Rockwell"
        self.font_size = 20
        self.align = 0
        # align must be 0, 1, 2 or 3

        self._type = "text"
        self._dimensions = [0, 0]
        self. _position = [0, 0]

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position

    def draw(self, surface, pos):
        text = self.text
        color = self.text_colour
        rect = [self._position[0], self._position[1], self._dimensions[0], self._position[1]]
        font = pygame.font.SysFont(self.font, self.font_size)
        align = self.align

        wrap_text(surface, text, color, rect, font, align)

        '''
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
        for image in imageList:
            width = image.get_width()
            lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
            if len(lineList[-1]) == 0 or lineLen <= maxLen:
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
                surface.blit(image, (round(x), y))
                lineLeft += image.get_width()
            lineBottom += fontHeight + lineSpacing

        if lastLine < len(lineList):
            drawWords = sum([len(lineList[i]) for i in range(lastLine)])
            remainingText = ""
            for text in listOfWords[drawWords:]: remainingText += text + " "
            return remainingText
        return ""
    
        '''


