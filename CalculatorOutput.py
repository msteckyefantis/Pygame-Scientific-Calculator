#File 6
import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from KeypadLibrary import *
from MouseLibrary import *
from TextFormatingLibrary import *


## Creating Calculator Output Box

#def __init__(self,
 #                x, y, w ,h,
  #               bgcolor,
   #              buttontext,
    #             CalcBoxtext,
     #            textfont,
      #           textcolor,
       #          textsize,
        #         textsizeadjustment,
         #        textcoordmode,
          #       textXposition,
            #     textYposition,
           #      textXpositionadjustment,
             #    textYpositionadjustment,
              #   borderbool,
               #  bordercolor,
                # bordermargin,
                 #highlightcolor,
               #  pressedcolor,
               #  modetuple):
# Input Box  Parameters
CalcBoxx = KBCx + KBCw + KBCSideMargin
CalcBoxy = InputBoxButtony + InputBoxButtonh + KBCSideMargin
CalcBoxw = WINDOWWIDTH - (KBCw + (6 * KBCSideMargin ))
CalcBoxh = WINDOWHEIGHT - CalcBoxy - KBCSideMargin
CalcBoxText = None
CalcBoxFont = None
CalcBoxTextColor = None
CalcBoxFontSize = None
CalcBoxFontSizeAdjustment = None
CalcBoxTextX =  None
CalcBoxTextY =  None
CalcBoxTextXAdjustment = None
CalcBoxTextYAdjustment = None
CalcBoxBorderColor = WHITE #DARKGRAY
CalcBoxBorderMARGIN = KPBMargin


CalcBox = Button(CalcBoxx, CalcBoxy, CalcBoxw  , CalcBoxh,
                 BLUE, # LIGHTGRAY
                 CalcBoxText,
                 None,
                 CalcBoxFont,
                 CalcBoxTextColor,
                 CalcBoxFontSize,
                 CalcBoxFontSizeAdjustment,
                 None,
                 CalcBoxTextX,
                 CalcBoxTextY,
                 CalcBoxTextXAdjustment,
                 CalcBoxTextYAdjustment,
                 True,
                 CalcBoxBorderColor,
                 CalcBoxBorderMARGIN,
                 None,
                 None,
                 (CalcMode))


# Drawing the Lines
# Getting Line parameters
NumberOfCalcBoxSections = 5
NumberOfCalcBoxLines = NumberOfCalcBoxSections - 1
CalcBoxLineColor = WHITE # DARKGRAY
CalcBoxLineWidth = KPBMargin

YDistanceBetweenLines = int(CalcBox.rectparam[3]/float(NumberOfCalcBoxSections))


# x value of lines same for all
CalcBoxLineX1 = CalcBox.rectparam[0]
CalcBoxLineX2 = CalcBox.rectparam[0] + (CalcBox.rectparam[2] - 1)

# getting y values of lines
CalcBoxLineY = []

def getCalcBoxLineYValues():
    for i in range(1,NumberOfCalcBoxLines + 1):
        YValue = CalcBox.rectparam[1] + (i * YDistanceBetweenLines)
        CalcBoxLineY.append(YValue)

getCalcBoxLineYValues()

# function that draws lines

def drawCalcBoxLines():
    for i in range(NumberOfCalcBoxLines):
        pygame.draw.line(DISPLAYSURF, CalcBoxLineColor,
                         (CalcBoxLineX1, CalcBoxLineY[i]),
                         (CalcBoxLineX2, CalcBoxLineY[i]),
                          CalcBoxLineWidth)




###############################################

#Scroll Button

CalcBoxDisplayStartIndex = [0]
ScrollButtonPressedY = [None]


# [Scroll Button Pressed Y, 0
# Calc Box display Start index] 1

#CalcOutputHistory = [("TEST", "FUCK"), ("DUCK", "TRUCK"), ("MUCK", "LUCK")]
CalcOutputHistory = []



ScrollButton = Button(RRBBx + InputBoxButtonBorderMARGIN,# x
                 CalcBoxy,# y
                 RRBBw - (2*InputBoxButtonBorderMARGIN),# w
                 CalcBoxh,# h
                 BLUE, # bgcolor
                 None, # buttontext
                 None, # inputboxtext
                 None, # textfont
                 None, # textcolor
                 0, # textsize
                 0, # textsizeadjustment
                 None, # textcoordmode
                 0, # textXposition
                 0, # textYposition
                 0, # textXpositionadjustment
                 0, # textYpositionadjustment
                 True, #borderbool
                 WHITE, # bordercolor
                 KPBMargin, # bordermargin
                 None, #highlightcolor
                 None, # pressedcolor
                 None, #modetuple
                 True)




ScrollButtonBackGroundRectangle = MyRect(ScrollButton.x,
                                         CalcBoxy,
                                         ScrollButton.w,
                                         CalcBoxh,
                                         DARKGRAY,
                                         0)


SFSPseudoScrollButton = Button(RRBBx + InputBoxButtonBorderMARGIN,# x
                 CalcBoxy,# y
                 RRBBw - (2*InputBoxButtonBorderMARGIN),# w
                 CalcBoxh,# h
                 BLUE, # bgcolor
                 None, # buttontext
                 None, # inputboxtext
                 None, # textfont
                 None, # textcolor
                 0, # textsize
                 0, # textsizeadjustment
                 None, # textcoordmode
                 0, # textXposition
                 0, # textYposition
                 0, # textXpositionadjustment
                 0, # textYpositionadjustment
                 True, #borderbool
                 WHITE, # bordercolor
                 KPBMargin, # bordermargin
                 None, #highlightcolor
                 None, # pressedcolor
                 None, #modetuple
                 True)


def UpdateScrollButtonHeight():
    if len(CalcOutputHistory) > NumberOfCalcBoxSections:
        ScrollButton.h =\
        int( \
        (NumberOfCalcBoxSections/len(CalcOutputHistory)) *(CalcBoxh)\
        )


def drawScrollButton():
    ScrollButtonBackGroundRectangle.draw()
    ScrollButton.Move_Draw(ScrollButton.x, # x
                  ScrollButton.y, # y
                  ScrollButton.w, # w
                  ScrollButton.h,#h
                  WHITE, # bordercolor
                  BLUE, # insidecolor
                  KPBMargin)

# Scroll Button Zone Y Partition stuff


ScrollButtonYPartitionZones = [(0,CalcBoxy +CalcBoxh)]

def getScrollButtonYPartitionZones():
    if len(CalcOutputHistory) <= NumberOfCalcBoxSections:
        return [(0,CalcBoxy +CalcBoxh)]
    else:
        NumberOfElements = len(CalcOutputHistory)
        NumberOfPartitions = NumberOfElements \
                             - NumberOfCalcBoxSections + 1
        TopY = CalcBoxy
        BottomY = CalcBoxy + CalcBoxh - ScrollButton.h
        TotalDistanceRange = BottomY - TopY
        PartitionHeight = int(TotalDistanceRange/NumberOfPartitions)
        PartitionZones = []
        for i in range(NumberOfPartitions):
            PartitionZones.append(\
                                   (TopY + (PartitionHeight * i),\
                                    TopY + (PartitionHeight * (i + 1))\
                                            - 0.00000000001) \
                                 )
        # making sure last partition zone is has "good" range
        PartitionZones[-1] = (PartitionZones[-1][0], CalcBoxy+ CalcBoxh)
        return PartitionZones



def UpdateCalcOutputTextDisplay():
    Zones = getScrollButtonYPartitionZones()
    for i in range(len(Zones)):
        if (Zones[i][0] <= ScrollButton.y) and\
           (Zones[i][1] >= ScrollButton.y):
            CalcBoxDisplayStartIndex[0] = i
            


    
######## Text Slots

CalcOutputTextSlot = MyText(0, #x
             0, #y
             BOLDFONT, #Font
             0, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False) #staticbool



def drawCalcOutputText():
    XDistanceFromSide = 5
    TopYDistanceFromLine = 10
    BottomYDistanceFromLine = 42
    X = CalcBoxx + XDistanceFromSide
    YTop = [CalcBoxy + KPBMargin + TopYDistanceFromLine]
    YBottom = [CalcBoxy + KPBMargin + BottomYDistanceFromLine]

    for i in range(len(CalcBoxLineY)):
        YTop.append(CalcBoxLineY[i] + KPBMargin + TopYDistanceFromLine)
        YBottom.append(CalcBoxLineY[i] + KPBMargin + BottomYDistanceFromLine)

    for i in range(NumberOfCalcBoxSections):
        Errored = False
        try:
            TopText = CalcOutputHistory[CalcBoxDisplayStartIndex[0] + i][0]
            BottomText = CalcOutputHistory[CalcBoxDisplayStartIndex[0] + i][1]
        except IndexError:
            Errored = True
        if not Errored:
            CalcOutputTextSlot.write3(TopText,
                              19,
                              X,
                              YTop[i])
            CalcOutputTextSlot.write3(BottomText,
                              40,
                              X,
                              YBottom[i])

    
def drawCalcBox():
    UpdateCalcOutputTextDisplay()
    CalcBox.draw()
    drawCalcBoxLines()
    drawCalcOutputText()

