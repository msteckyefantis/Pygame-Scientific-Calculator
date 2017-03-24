#FILE 2

import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *


# RESET TO ORIGINAL OptionsMenuHeight = 25
OptionsMenuHeight = 0




# Input Box Button Parameters
InputBoxButtonx = 15
InputBoxButtony = OptionsMenuHeight + 10
InputBoxButtonw = 253
InputBoxButtonh = int(WINDOWHEIGHT*.15)
InputBoxButtonTextDisplay = "Calculator"
InputBoxButtonFont = BOLDFONT
InputBoxButtonTextColor = WHITE
InputBoxButtonFontSize = 20
InputBoxButtonFontSizeAdjustment = 0
InputBoxButtontextcoordmode = TXTCOORDMODEcenter
InputBoxButtonTextSpread = 20
InputBoxButtonTextX = InputBoxButtonx + (InputBoxButtonw/2)
InputBoxButtonTextY = InputBoxButtony + (InputBoxButtonh/2) - InputBoxButtonTextSpread 
InputBoxButtonTextXAdjustment = 0
InputBoxButtonTextYAdjustment = 0
InputBoxButtonBorderColor = DARKGRAY
InputBoxButtonBorderMARGIN = 5


# Creating Input Box Button
CalcModeInputBoxButton = Button(InputBoxButtonx, InputBoxButtony, InputBoxButtonw  , InputBoxButtonh,
                 WHITE,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 None,
                 True,
                 InputBoxButtonBorderColor,
                 InputBoxButtonBorderMARGIN,
                 None,
                 None,
                 (CalcMode))




# inputboxbutton text

InputBoxButtonText_MSE = MyText(\
             InputBoxButtonTextX,#x
             InputBoxButtonTextY,#y
             InputBoxButtonFont,#font
             InputBoxButtonFontSize,#font size
             "Michael Stecky-Efantis'",#text
             InputBoxButtonTextColor,#text color
             InputBoxButtontextcoordmode,#text coord mode
             True)# static bool


InputBoxButtonText_Calculator = MyText(\
             InputBoxButtonTextX,#x
             InputBoxButtonTextY + (2 * InputBoxButtonTextSpread),#y
             InputBoxButtonFont,#font
             InputBoxButtonFontSize,#font size
             "Calculator",#text
             InputBoxButtonTextColor,#text color
             InputBoxButtontextcoordmode,#text coord mode
             True)# static bool




### Caculator Status
# CalcModeStatus = CMS
CMSx = InputBoxButtonx + int(InputBoxButtonw/2)
CMSy = InputBoxButtony + 30
CMSFontsize = 20

CalcModeStatusTextSlot = MyText(\
             CMSx, #x
             CMSy, #y
             BOLDFONT, #Font
             CMSFontsize, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False) #staticbool





# input box button text border

InputBoxButtonTextBorder = MyRect(\
             InputBoxButtonx + InputBoxButtonBorderMARGIN +\
             KPBMargin, # x
             InputBoxButtony + InputBoxButtonBorderMARGIN + KPBMargin, # y
             InputBoxButtonw - (2*KPBMargin) - (2 *InputBoxButtonBorderMARGIN), # w
             InputBoxButtonh - (2*KPBMargin) - (2 *InputBoxButtonBorderMARGIN) ,# h
             BLUE,# color
             thickness = 0)# thickness

InputBoxButtonMiddleTextDividor = MyRect(\
             InputBoxButtonx + InputBoxButtonBorderMARGIN, # x
             InputBoxButtony + (InputBoxButtonh/2) + 4, # y
             InputBoxButtonw - (2*InputBoxButtonBorderMARGIN), # w
             KPBMargin,# h
             WHITE,# color
             thickness = 0)# thickness

InputBoxButtonMiddleVertialTextDividor = MyRect(\
             InputBoxButtonx + (InputBoxButtonw/2)- 19, # x
             InputBoxButtony + InputBoxButtonBorderMARGIN, # y
             KPBMargin, # w
             InputBoxButtonh -(2*InputBoxButtonBorderMARGIN),# h
             WHITE,# color
             thickness = 0)# thickness


def drawInputBoxButtonTextBorders():
    InputBoxButtonTextBorder.draw()
    InputBoxButtonMiddleTextDividor.draw()
    InputBoxButtonMiddleVertialTextDividor.draw()

# Input Box  Parameters
InputBoxx = 15 + 253 + 15 # *See Keypad container KBC for values
InputBoxy = InputBoxButtony
InputBoxw = WINDOWWIDTH - (253 + (6 * 15 )) # *
InputBoxh = int(WINDOWHEIGHT*.15)
InputBoxText = ""
InputBoxFont = BOLDFONT
InputBoxTextColor = WHITE
InputBoxFontSize = FONTSIZE + 12
InputBoxFontSizeAdjustment = 0
InputBoxTextX =  InputBoxx
InputBoxTextY =  InputBoxy
InputBoxTextXAdjustment = 13
InputBoxTextYAdjustment = 21
InputBoxBorderColor = WHITE
InputBoxBorderMARGIN = 5

# Creating Input Box
CalcModeInputBox = Button(InputBoxx, InputBoxy, InputBoxw  , InputBoxh,
                 BLUE,
                 InputBoxText,
                 None,
                 InputBoxFont,
                 InputBoxTextColor,
                 InputBoxFontSize,
                 InputBoxFontSizeAdjustment,
                 TXTCOORDMODEtopleft,
                 InputBoxTextX,
                 InputBoxTextY,
                 InputBoxTextXAdjustment,
                 InputBoxTextYAdjustment,
                 False,
                 InputBoxBorderColor,
                 InputBoxBorderMARGIN,
                 None,
                 None,
                 (CalcMode),
                 textstaticbool = False)


# Dealing with inputting a lot of numbers and functions
InputBoxTextSizeSmallMode = [False]
def isInputTextTooBig(Button, TextSize, SizeLimit):
    fontobj = pygame.font.Font(Button.textfont, TextSize)
    #color is arbitrary for this function
    TextSurf = fontobj.render(Button.buttontext, True, BLACK) 
    TextRect = TextSurf.get_rect()
    if TextRect[2] > SizeLimit:
        return True
    else:
        return False


# shrink InputBoxText if too large
def FormatInputBoxTextSize(Button, SizeLimit,\
                           NormalTextSize, ModifiedTextSize,
                           NormalTextY,
                           ModifiedTextY):
    if isInputTextTooBig(Button, NormalTextSize, SizeLimit):
        Button.textsize = ModifiedTextSize
        InputBoxTextSizeSmallMode[0] = True
        if Button.textYposition != ModifiedTextY:
            Button.textYposition = ModifiedTextY    
    else:
        Button.textsize = NormalTextSize
        InputBoxTextSizeSmallMode[0] = False
        if Button.textYposition != NormalTextY:
            Button.textYposition = NormalTextY 

def InputBoxTextSizeHitLimit():
    if InputBoxTextSizeSmallMode[0]:
        if isInputTextTooBig(CalcModeInputBox,
                             CalcModeInputBox.textsize,
                             CalcModeInputBox.w - ( 2 * InputBoxTextXAdjustment)):
            return True
        else:
            return False


# inputBox border

InputBoxLeftBorder =  MyRect(\
             InputBoxx, # x
             InputBoxy, # y
             KPBMargin, # w
             InputBoxh,# h
             WHITE,# color
             thickness = 0)# thickness

InputBoxTopBorder =  MyRect(\
             InputBoxx, # x
             InputBoxy, # y
             InputBoxw, # w
             KPBMargin,# h
             WHITE,# color
             thickness = 0)# thickness

InputBoxBottomBorder =  MyRect(\
             InputBoxx, # x
             InputBoxy + InputBoxh - KPBMargin, # y
             InputBoxw, # w
             KPBMargin,# h
             WHITE,# color
             thickness = 0)# thickness


InputBoxRightBorder =  MyRect(\
             InputBoxx + InputBoxw - KPBMargin, # x
             InputBoxy, # y
             KPBMargin, # w
             InputBoxh,# h
             WHITE,# color
             thickness = 0)# thickness




def DrawInputBoxBorder():
    InputBoxLeftBorder.draw()
    InputBoxRightBorder.draw()
    InputBoxTopBorder.draw()
    InputBoxBottomBorder.draw()

