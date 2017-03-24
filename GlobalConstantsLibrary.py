#FILE 1

import pygame, math, sys, copy
from pygame.locals import *
#### GLOBAL CONSTANTS

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = int(1152 * 1) # size of window's width in pixels
WINDOWHEIGHT = int( WINDOWWIDTH*(9/16) )# size of windows' height in pixels
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


#Font data
BASICFONT = "C:\\Windows\\Fonts\\segoeuil.ttf"
BOLDFONT = "C:\\Windows\\Fonts\\segoeuib.ttf"
FONTSIZE = int( WINDOWWIDTH * 0.024 )


# Colours     R    G    B

LIGHTGRAY= (222, 222, 222)
DARKGRAY = (100, 100, 100)
GRAY     = (200, 200, 200)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
PINK     = (255, 105, 180)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
LIGHTBLUE= (127, 203, 255)
ALMOSTLIGHTGRAY= (215, 215, 215)
HIGHLIGHTEDBLUE= (  55,  55, 255)
LIGHTBLUETWOth = (78, 78, 255)
DARKLIGHTBLUE   =    (LIGHTBLUE[0] - 15,\
                  LIGHTBLUE[1] - 15,\
                  LIGHTBLUE[2])
DARKBLUE     = (  0,   0, 200)
DARKERBLUE     = (  0,   0, 175)

LIGHTBLACK = (75,75,75)

YELLOWTREE = (128,255,0)
YELLOWTWO = (153,255,153)
#Program Modes
CalcMode = "Calcmode"

# button modes
keypad = "keypad mode"
INVkeypad = "INVkeypad mode"

# radian/degree modes
RadianMode = "Radian Mode"
DegreeMode = "Degree Mode"

AngleMode = [RadianMode]
Memory = [None]

# Screen mode, default is None
SpecialFunctionsScreenMode = "SFSMode"
ScreenMode = [None]

# Special functions screen and constants view index
# [view index for functions, view index for consants]
SFSViewIndex = [0, 0]

# How many signiciant figures calculator rounds to
SignificantFigures = [30]

# Number of Times the enter button is pressed
NumberOfTimesEnterPressed = [0]

#####Initial Settings
# Mode list of form:
# ModesList = [ProgramMode, KeypadMode]
ModesList = [CalcMode, keypad]


# HoverStatus Bar Data

HoverStatusBarData = [None]

CommaMode = [False]


ButtonPressed = None
ButtonHover = None


# keyboardbutton pressed this round # 4 FXzz

KeyboardButtonPressedStatus = [()]

for i in range(323):
    KeyboardButtonPressedStatus[0] += (0,) 

def KeyboardButtonPressedStatusReset():
    KeyboardButtonPressedStatus[0] = pygame.key.get_pressed()
        

# Scroll Wheel Variable
ScrollWheelVariable = [None,0,0,0,0]


# Button Color Modes
HIGHLIGHT = "highlight"
PRESSED = "pressed"


#Text coordinate modes
TXTCOORDMODEcenter = "center"
TXTCOORDMODEtopleft = "topleft"
TXTCOORDMODEbottomleft = "bottomleft"
TXTCOORDMODEmidleft = "midleft"
TXTCOORDMODEmidright = "midright"

#KeypadConstant (used in inputbox)
KPBMargin = 3


class Button:
    def __init__(self,
                 x,# x
                 y,# y
                 w,# w
                 h,# h
                 bgcolor, # bgcolor
                 buttontext, # buttontext
                 inputboxtext, # inputboxtext
                 textfont, # textfont
                 textcolor, # textcolor
                 textsize, # textsize
                 textsizeadjustment, # textsizeadjustment
                 textcoordmode, # textcoordmode
                 textXposition, # textXposition
                 textYposition, # textYposition
                 textXpositionadjustment, # textXpositionadjustment
                 textYpositionadjustment, # textYpositionadjustment
                 borderbool, #borderbool
                 bordercolor, # bordercolor
                 bordermargin, # bordermargin
                 highlightcolor, #highlightcolor
                 pressedcolor, # pressedcolor
                 modetuple, #modetuple
                 textstaticbool = True): # textstaticbool
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bgcolor = bgcolor
        self.buttontext = buttontext
        self.inputboxtext = inputboxtext
        self.textfont = textfont
        self.textcolor = textcolor
        self.textsize = textsize
        self.textsizeadjustment = textsizeadjustment
        self.textcoordmode = textcoordmode
        self.textXposition = textXposition
        self.textYposition = textYposition
        self.textXpositionadjustment = textXpositionadjustment
        self.textYpositionadjustment = textYpositionadjustment
        self.modetuple = modetuple
        self.borderbool = borderbool
        self.bordercolor = bordercolor
        self.bordermargin = bordermargin
        self.highlightcolor = highlightcolor
        self.pressedcolor = pressedcolor
        self.textstaticbool = textstaticbool

        
        if borderbool:
            self.rectparam = (x + bordermargin,y + bordermargin,
                              w - (2 * bordermargin) ,h  - (2 * bordermargin))
            self.rectboundary = (self.rectparam[0],
                                 self.rectparam[0] + self.rectparam[2],
                                 self.rectparam[1],
                                 self.rectparam[1] + self.rectparam[3])

            self.borderrectparam = (x, y, w, h)
            self.borderrectboundary =  (x, x + w,
                                    y, y+ h)
        else:
            self.rectparam = (x, y, w, h)
            self.rectboundary = (x, x+w, y, y+h)

        # if text is static, will create the text one time only
        if (self.buttontext != None) and self.textstaticbool:
            self.fontObj = pygame.font.Font(self.textfont,
                                       self.textsize + self.textsizeadjustment)
            self.textSurf = self.fontObj.render(self.buttontext,
                                      True, self.textcolor)
            self.textRect = self.textSurf.get_rect()
            # Text coordinate relative to center or top left of button
            if self.textcoordmode == TXTCOORDMODEtopleft:
                self.textRect.topleft = (self.textXposition + self.textXpositionadjustment ,
                                self.textYposition + self.textYpositionadjustment)
            elif self.textcoordmode == TXTCOORDMODEcenter:
                self.textRect.center = (self.textXposition + self.textXpositionadjustment ,
                                self.textYposition + self.textYpositionadjustment)
            
            
    def __repr__(self):
        if self.buttontext != None:
            return str(self.buttontext)
        elif self.borderbool:
            return str(self.borderrectparam)
        else:
            return str(self.rectparam)

    def __str__(self):
        if self.buttontext != None:
            return str(self.buttontext)
        elif self.borderbool:
            return str(self.borderrectparam)
        else:
            return str(self.rectparam)


    #def __dir__(self):
    #    return ["__str__","__init__","__repr__", "__dir__"]

    def draw(self, RectColor = None):
        """ Insert Rectangle Color as argument to draw it a different color"""
        # drawing border if the button has one
        if self.borderbool:
            pygame.draw.rect(DISPLAYSURF, self.bordercolor, self.borderrectparam)
        #drawing button a different color if selected
        if RectColor == None:
            pygame.draw.rect(DISPLAYSURF, self.bgcolor, self.rectparam)
        else:
            pygame.draw.rect(DISPLAYSURF, RectColor, self.rectparam)
        #drawing button text
        if (self.buttontext != None):
            if self.textstaticbool:
                DISPLAYSURF.blit(self.textSurf, self.textRect)
            # if not static, text will be updated
            elif not self.textstaticbool:
                fontObj = pygame.font.Font(self.textfont,
                                           self.textsize + self.textsizeadjustment)
                textSurf = fontObj.render(self.buttontext,
                                          True, self.textcolor)                  
                textRect = textSurf.get_rect()
                # Text coordinate relative to center or top left of button
                if self.textcoordmode == TXTCOORDMODEtopleft:
                    textRect.topleft = (self.textXposition + self.textXpositionadjustment ,
                                    self.textYposition + self.textYpositionadjustment)
                elif self.textcoordmode == TXTCOORDMODEcenter:
                    textRect.center = (self.textXposition + self.textXpositionadjustment ,
                                    self.textYposition + self.textYpositionadjustment)
                DISPLAYSURF.blit(textSurf, textRect)

    def draw2(self, RectColor = None): # less "static"
        # drawing border
        if self.borderbool: 
            pygame.draw.rect(DISPLAYSURF, self.bordercolor,\
                             (self.x, self.y, self.w, self.h))
        if RectColor == None:
            pygame.draw.rect(DISPLAYSURF, self.bgcolor,\
                             (self.x + self.bordermargin,
                              self.y + self.bordermargin,
                              self.w - (2 * self.bordermargin),
                              self.h - (2* self.bordermargin)))
        else:
            pygame.draw.rect(DISPLAYSURF, RectColor,\
                             (self.x + self.bordermargin,
                              self.y + self.bordermargin,
                              self.w - (2 * self.bordermargin),
                              self.h - (2* self.bordermargin)))

    def Move_Draw(self,
                  x, # x
                  y, # y
                  w, # w
                  h, # h
                  bordercolor, # bordercolor
                  insidecolor, # insidecolor
                  bordersize): # bordresize
        pygame.draw.rect(DISPLAYSURF, bordercolor,\
                         (x,y,w,h))
        pygame.draw.rect(DISPLAYSURF, insidecolor,\
                             (x + bordersize,
                              y + bordersize,
                              w - (2 * bordersize),
                              h - (2 * bordersize)))
############ EXTRAZ

            
# draw(self, colorsetting = None, ButtonHighlight = False, BorderHighlight = False):
        # Drawing if Highlighted
        # CONSIDER OMITING THIS PART, JUST MAKE MOUSE
        # CHANGE THE OBJECT COLOR PARAMETER
        #elif colorsetting == HIGHLIGHT:
            # drawing (possibliy highlighted) border if the button has one
        #    if self.borderbool and BorderHighlight:
        #        pygame.draw.rect(DISPLAYSURF, YELLOW, self.borderrectparam)
         #   elif self.borderbool and (not BorderHighlight):
         #       pygame.draw.rect(DISPLAYSURF, self.bordercolor, self.borderrectparam)
            # drawing (possibliy highlighted) rectangle
         #   if ButtonHighlight:
          #      pygame.draw.rect(DISPLAYSURF, YELLOW, self.rectparam)
           # else:
            #    pygame.draw.rect(DISPLAYSURF, self.bgcolor, self.rectparam)

#     
#def drawKeypad():
#    #draws Keypad Button Container
#    KBC.draw()
#    #Draw A type buttons
#    buttonListDrawer(ATypeButtons)
#    if KeypadMode == keypad:
#        buttonListDrawer(BTypeButtons)
#    elif KeypadMode == INVkeypad:
#        buttonListDrawer(INVBTypeButtons)
#    buttonListDrawer(CTypeButtons)
#    INVButton.draw()
#    DeleteButton.draw()
#    EnterButton.draw()   TXTCOORDMODEmidleft 


class MyText:
    def __init__(self,
             x, #x
             y, #y
             Font, #Font
             Fontsize, #Fontsize
             text, #text
             textcolor, #textcolor
             textcoordmode, #textcoordmode
             staticbool): #staticbool
        self.x = x
        self.y = y
        self.Font = Font
        self.Fontsize = Fontsize
        self.text = text
        self.textcolor = textcolor
        self.textcoordmode = textcoordmode 
        self.staticbool = staticbool

        if self.staticbool:
            self.FontObj = pygame.font.Font(self.Font,
                                   self.Fontsize)
            self.TextSurf = self.FontObj.render(self.text,
                                      True, self.textcolor)
            self.TextRect = self.TextSurf.get_rect()
            if self.textcoordmode ==  TXTCOORDMODEmidleft:
                self.TextRect.midleft = (self.x,
                                         self.y)
            elif self.textcoordmode ==  TXTCOORDMODEmidright:
                self.TextRect.midright = (self.x,
                                         self.y)
            elif self.textcoordmode == TXTCOORDMODEtopleft:
                self.TextRect.topleft = (self.x,
                                         self.y)
            elif self.textcoordmode == TXTCOORDMODEcenter:
                self.TextRect.center = (self.x,
                                        self.y)
                
    
    
    def __repr__(self):
        return str([self.text,"x = ",self.x,"y = ",self.y])
                 

    def __str__(self):
        return self.text

    def write(self):
        if self.staticbool:
            DISPLAYSURF.blit(self.TextSurf, self.TextRect)
        else:      
            FontObj = pygame.font.Font(self.Font,
                                       self.Fontsize)
            TextSurf = FontObj.render(self.text,
                                          True, self.textcolor)
            TextRect = TextSurf.get_rect()
            if self.textcoordmode ==  TXTCOORDMODEmidleft:
                TextRect.midleft = (self.x,
                                    self.y)
            elif self.textcoordmode ==  TXTCOORDMODEmidright:
                TextRect.midright = (self.x, self.y)
            elif self.textcoordmode ==  TXTCOORDMODEtopleft:
                TextRect.topleft = (self.x, self.y)
            DISPLAYSURF.blit(TextSurf, TextRect)
    def write2(self, Text):
        FontObj = pygame.font.Font(self.Font,
                                   self.Fontsize)
        TextSurf = FontObj.render(Text,
                                      True, self.textcolor)
        TextRect = TextSurf.get_rect()
        if self.textcoordmode ==  TXTCOORDMODEmidleft:
            TextRect.midleft = (self.x,
                                self.y)
        elif self.textcoordmode ==  TXTCOORDMODEmidright:
            TextRect.midright = (self.x, self.y)
        elif self.textcoordmode ==  TXTCOORDMODEtopleft:
            TextRect.topleft = (self.x, self.y)
        elif self.textcoordmode ==  TXTCOORDMODEcenter:
            TextRect.center = (self.x, self.y)
        DISPLAYSURF.blit(TextSurf, TextRect)
            
    def write3(self, Text, Textsize, Textx, Texty):
        FontObj = pygame.font.Font(self.Font,
                                   Textsize)
        TextSurf = FontObj.render(Text,
                                      True, self.textcolor)
        TextRect = TextSurf.get_rect()
        if self.textcoordmode ==  TXTCOORDMODEmidleft:
            TextRect.midleft = ( Textx, Texty)
        elif self.textcoordmode ==  TXTCOORDMODEmidright:
            TextRect.midright = ( Textx, Texty)
        elif self.textcoordmode ==  TXTCOORDMODEtopleft:
            TextRect.topleft = ( Textx, Texty)
        elif self.textcoordmode ==  TXTCOORDMODEcenter:
            TextRect.center = ( Textx, Texty)
        DISPLAYSURF.blit(TextSurf, TextRect)

    def writeColor(self,Color):  
        FontObj = pygame.font.Font(self.Font,
                                       self.Fontsize)
        TextSurf = FontObj.render(self.text,
                                          True, Color)
        TextRect = TextSurf.get_rect()
        if self.textcoordmode ==  TXTCOORDMODEmidleft:
            TextRect.midleft = (self.x, self.y)
        elif self.textcoordmode ==  TXTCOORDMODEmidright:
            TextRect.midright = (self.x, self.y)
        elif self.textcoordmode ==  TXTCOORDMODEtopleft:
            TextRect.topleft = (self.x, self.y)
        DISPLAYSURF.blit(TextSurf, TextRect)
        
        
class MyRect: #that doesn't sound right lol
    def __init__(self,
             x, # x
             y, # y
             w, # w
             h, # h
             color, # color
             thickness = 0): #thickness
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rectparam = (x,y,w,h)
        self.thickness = thickness
        

    def __repr__(self):
        return str(["x = ",self.x,"y = ",self.y])
                 

    def __str__(self):
        return  "x = "+ str(self.x)+ " y = " + str(self.y)

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, self.rectparam, self.thickness)

    def draw2(self, Color = None):
        if Color == None:
            pygame.draw.rect(DISPLAYSURF, self.color,
                         (self.x,self.y,self.w,self.h),
                         self.thickness)
        else:
            pygame.draw.rect(DISPLAYSURF, Color,
                         (self.x,self.y,self.w,self.h),
                         self.thickness)



class MyEquiTri: #draws equilateral triangle
    def __init__(self,
             leftx, #Left x
             y, # y value of highest point
             w, # w
             h, # h
             PointingUpbool,# pointing up or down
             color, # color
             thickness = 0): #thickness
        self.leftx = leftx
        self.y = y
        self.w = w
        self.h = h
        self.PointingUp = PointingUpbool
        self.color = color
        self.thickness = thickness

     
        if self.PointingUp:
            self.P1 = (self.leftx, \
                      self.y + self.h - 1)
            self.P2 = (self.leftx + self.w- 1, \
                      self.y + self.h - 1)
            self.P3 = (self.leftx + (self.w/2), \
                      self.y)
        else:
            self.P1 = (self.leftx, self.y)
            self.P2 = (self.leftx + self.w - 1, \
                      self.y)
            self.P3 = (self.leftx + (self.w/2), \
                      self.y+ self.h- 1)

        self.Plist = (self.P1, self.P2, self.P3)
    





    def __repr__(self):
        return "Leftmost x = " + str(self.leftx) + ", h = "  + str(self.h) 

    def __str__(self):
        return  "Leftmost x = " + str(self.leftx) + ", h = "  + str(self.h) 




    def draw(self,color = None):
        if color == None:
            pygame.draw.polygon(DISPLAYSURF, self.color,
                            self.Plist, self.thickness)
        else:
            pygame.draw.polygon(DISPLAYSURF, color,
                            self.Plist, self.thickness)
    

