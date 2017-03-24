import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from InputBoxLibrary import *
from KeypadLibrary import *
from CalculatorOutput import *

########### Special Functions Button SFB ###################

SFBx = KBCx
SFBy =  int(RSBBy + RSBBh +  KBCSideMargin)
SFBw =  KBCw
SFBh =  WINDOWHEIGHT - SFBy - (WINDOWHEIGHT - CalcBoxy - CalcBoxh)
SFBColor = WHITE
SFBBorderColor = WHITE
SFBBorderMargin = CalcBoxBorderMARGIN
SFBText = "FUNCTIONS"
SFBTextColor = WHITE
SFBTextx = SFBx + (SFBw/2)
SFBTextySpread = 30
SFBTextySpreadb = 20 # for SFS mode
SFBTexty = SFBy + (SFBh/2) - SFBTextySpread 
SFBTextCoordmode = TXTCOORDMODEcenter
SFBfont = BOLDFONT
SFBfontsize = 24
SFBhighlightcolor = YELLOW
SFBpressedcolor = ORANGE


SpecialFunctionsButton = Button(\
                 SFBx, SFBy, SFBw ,SFBh,
                 SFBColor, #bg color
                 None,#Button Text
                 None,# inputbox text
                 None,# text font
                 None,# text color
                 None, # text size
                 None,# text size adjustment
                 None,# text coord mode
                 None ,# text x
                 None,# text y
                 None, # text x adj
                 None,# text y adj
                 True, # border bool
                 SFBBorderColor,# border color
                 SFBBorderMargin , # border margin 
                 SFBhighlightcolor, #highlight Color
                 SFBpressedcolor, # pressed color
                 None, # mode tuple
                 textstaticbool = True)

# Special functions button Text Border

SFBTextBorder = MyRect(\
             TopLeftKPBPixelCoords[0][0][0], # x
             SFBy +  KPBMargin, # y
             (KPBAW * 5) +  (KPBMargin * 4) , # w
             SFBh  - (KPBMargin *2) ,# h
             BLUE,# color
             thickness = 0)# thickness


# special functions SP text 

SFBTextSwitch = MyText(\
             SFBTextx,#x
             SFBy + (SFBh/2) - SFBTextySpread,#y
             SFBfont,#font
             SFBfontsize,#font size
             "Switch",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)# static bool





SFBTextCalculator = MyText(\
             SFBTextx,#x
             SFBy + (SFBh/2),#y
             SFBfont,#font
             SFBfontsize,#font size
             "Calculator",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)# static bool
SFBTextMode = MyText(\
             SFBTextx,#x
             SFBy + (SFBh/2) + SFBTextySpread,#y
             SFBfont,#font
             SFBfontsize,#font size
             "Mode",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)


SFBTextSwitch = MyText(\
             SFBTextx,#x
             SFBy + (SFBh/2) - SFBTextySpreadb,#y
             SFBfont,#font
             SFBfontsize,#font size
             "Switch",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)# static bool

SFBTextCalculator_Mode = MyText(\
             SFBTextx,#x
             SFBy + (SFBh/2) + SFBTextySpreadb,#y
             SFBfont,#font
             SFBfontsize,#font size
             "Calculator Mode",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)


SFBTextFreeWrite = MyText(0, #x
             0, #y
             BOLDFONT, #Font
             22, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEcenter, #textcoordmode
             False)









def drawSpecialFunctionsButton(ButtonHover, ButtonPressed):
    SpecialFunctionsButton.draw()
    if ButtonPressed == SFBTextBorder or\
       KeyboardButtonPressedStatus[0][9] == 1:
        SFBTextBorder.draw2((LIGHTBLUE[0] - 15,\
                             LIGHTBLUE[1] - 15,\
                             LIGHTBLUE[2]))
    elif ButtonHover == SFBTextBorder:
        SFBTextBorder.draw2(LIGHTBLUE)
    else:
        SFBTextBorder.draw()
    

    SFBTextSwitch.write()
    SFBTextCalculator_Mode.write()

    #SFBTextFreeWrite.write3("Click here to add", 22,SFBTextSwitch.x,
      #                          SFBTextSwitch.y- 20 - 5)


######## Special Functions Screen #####################33

SFSx = CalcBoxx
SFSy = CalcBoxy
SFSw =  CalcBoxw
SFSh =  CalcBoxh
SFSColor = BLUE
SFSBorderColor = WHITE
SFSBorderMargin = CalcBoxBorderMARGIN


SpecialFunctionsScreen = Button(\
                 SFSx, SFSy, SFSw ,SFSh,
                 SFSColor, #bg color
                 None,#Button Text
                 None,# inputbox text
                 None,# text font
                 None,# text color
                 None, # text size
                 None,# text size adjustment
                 None,# text coord mode
                 None,# text x
                 None,# text y
                 None, # text x adj
                 None,# text y adj
                 True, # border bool
                 SFSBorderColor,# border color
                 SFSBorderMargin , # border margin 
                 None, #highlight Color
                 None, # pressed color
                 None, # mode tuple
                 textstaticbool = True)


# Special Functions Screen (SFS) Graphics


SFSMiddleBorder = MyRect(\
             CalcBoxx + (CalcBoxw/2) - (CalcBoxBorderMARGIN/2) , # x
             CalcBoxy, # y
             CalcBoxBorderMARGIN, # w
             CalcBoxh,# h
             WHITE,# color
             thickness = 0)# thickness

SFSTitleSpaceh = 75 # not including any borders

SFSTitleDividor = MyRect(\
             CalcBoxx, # x
             CalcBoxy + CalcBoxBorderMARGIN + SFSTitleSpaceh, # y
             CalcBoxw, # w
             CalcBoxBorderMARGIN,# h
             WHITE,# color
             thickness = 0)# thickness

SFSTitleLeftTextBackground = MyRect(\
             CalcBoxx + CalcBoxBorderMARGIN + KPBMargin, # x
             CalcBoxy + CalcBoxBorderMARGIN + KPBMargin, # y
             (CalcBoxw/2) - (1.5 * CalcBoxBorderMARGIN)\
             - (2 * KPBMargin), # w
             SFSTitleSpaceh - (2 * KPBMargin) ,# h
             BLUE,# color
             thickness = 0)# thickness

SFSTitleRightTextBackground = MyRect(\
             CalcBoxx + (CalcBoxw/2) +\
             (CalcBoxBorderMARGIN/2) + KPBMargin, # x
             CalcBoxy + CalcBoxBorderMARGIN + KPBMargin, # y
             (CalcBoxw/2) - (1.5 * CalcBoxBorderMARGIN)\
             - (2 * KPBMargin), # w
             SFSTitleSpaceh - (2 * KPBMargin) ,# h
             BLUE,# color
             thickness = 0)# thickness

SFSTitleFontSize = 29

SFSTitleLeftText = MyText(\
             SFSTitleLeftTextBackground.x + (SFSTitleLeftTextBackground.w/2),#x
             SFSTitleLeftTextBackground.y + (SFSTitleLeftTextBackground.h/2),#y
             SFBfont,#font
             SFSTitleFontSize,#font size
             "functions",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)# static bool 

SFSTitleRightText = MyText(\
             SFSTitleRightTextBackground.x + (SFSTitleRightTextBackground.w/2),#x
             SFSTitleRightTextBackground.y + (SFSTitleRightTextBackground.h/2),#y
             SFBfont,#font
             SFSTitleFontSize,#font size
             "constants",#text
             SFBTextColor,#text color
             SFBTextCoordmode,#text coord mode
             True)# static bool 


#SFS Navigation buttons
SFSNavButtonh = 17


SFSLeftUpButton = MyRect(\
             SFSx + SFSBorderMargin, # x
             SFSTitleDividor.y + SFSTitleDividor.h, # y
             (CalcBoxw/2) - (1.5 * CalcBoxBorderMARGIN), # w
             SFSNavButtonh,# h
             BLUE,# color
             thickness = 0)


SFSRightUpButton = MyRect(\
             SFSx + SFSw/2 + (0.5 * CalcBoxBorderMARGIN), # x
             SFSLeftUpButton.y, # y
             SFSLeftUpButton.w, # w
             SFSLeftUpButton.h,# h
             BLUE,# color
             thickness = 0)



SFSLeftDownButton = MyRect(\
             SFSLeftUpButton.x, # x
             CalcBox.y + CalcBox.h - CalcBoxBorderMARGIN - SFSNavButtonh, # y
             (CalcBoxw/2) - (1.5 * CalcBoxBorderMARGIN), # w
             SFSNavButtonh,# h
             BLUE,# color
             thickness = 0)


SFSRightDownButton = MyRect(\
             SFSRightUpButton.x, # x
             SFSLeftDownButton.y, # y
             SFSLeftDownButton.w, # w
             SFSLeftDownButton.h,# h
             BLUE,# color
             thickness = 0)


# SFS Navigation Button Arrows
SFSButtonArroww = 40

SFSLeftUpButtonArrow = MyEquiTri(\
             SFSLeftUpButton.x + (SFSLeftUpButton.w/2)  - (SFSButtonArroww/2), #Left x
             SFSLeftUpButton.y, # y value of highest point
             SFSButtonArroww, # w
             SFSLeftUpButton.h, # h    
             True,# pointing up or down
             (  0,   0, 130), # color
             thickness = 0)

SFSRightUpButtonArrow = MyEquiTri(\
             SFSRightUpButton.x + (SFSRightUpButton.w/2)  - (SFSButtonArroww/2), #Left x
             SFSRightUpButton.y, # y value of highest point
             SFSButtonArroww, # w
             SFSRightUpButton.h, # h    
             True,# pointing up or down
             (  0,   0, 130), # color
             thickness = 0)

SFSLeftDownButtonArrow = MyEquiTri(\
             SFSLeftDownButton.x + (SFSLeftDownButton.w/2)  - (SFSButtonArroww/2), #Left x
             SFSLeftDownButton.y, # y value of highest point
             SFSButtonArroww, # w
             SFSLeftDownButton.h, # h    
             False,# pointing up or down
             (  0,   0, 130), # color
             thickness = 0)


SFSRightDownButtonArrow = MyEquiTri(\
             SFSRightDownButton.x + (SFSRightDownButton.w/2)  - (SFSButtonArroww/2), #Left x
             SFSRightDownButton.y, # y value of highest point
             SFSButtonArroww, # w
             SFSRightDownButton.h, # h    
             False,# pointing up or down
             (  0,   0, 130), # color
             thickness = 0)



SFSButtonList = [SFSLeftUpButton,
    SFSLeftDownButton,
    SFSRightUpButton,
    SFSRightDownButton]

SFSButtonArrowList = [
    SFSLeftUpButtonArrow,
    SFSLeftDownButtonArrow,
    SFSRightUpButtonArrow,
    SFSRightDownButtonArrow]



def drawSFSNavButtons(ButtonPressed, ButtonHover):
    for i in range(4):
        if (SFSButtonList[i] == ButtonPressed) or \
           (ScrollWheelVariable[0] == i) or \
           (ScrollWheelVariable[1+i] > 0):
            SFSButtonList[i].draw2(DARKLIGHTBLUE)
            SFSButtonArrowList[i].draw((  0,   0, 190))
        elif SFSButtonList[i] == ButtonHover:
            SFSButtonList[i].draw2(LIGHTBLUE)
            SFSButtonArrowList[i].draw((  0,   0, 160))
        else:
            SFSButtonList[i].draw2()
            SFSButtonArrowList[i].draw()


# Special functions screen Seperators
NumberOfSFSSlots = [4]



def getSFSSeperatorYValues(NumberOfSlots, offset):
    NumberOfSlots = NumberOfSFSSlots[0]
    Top = SFSLeftUpButton.y + SFSLeftUpButton.h
    Bottom = SFSLeftDownButton.y
    Difference = Bottom - Top
    Spacing = int(Difference/NumberOfSlots)
    YList = []
    for i in range(NumberOfSlots + 1):
        YList.append((Top + i *Spacing) + offset) 
    return(YList)


def createSFSSeperators():
    YValues = getSFSSeperatorYValues(NumberOfSFSSlots[0],0)
    Seperators = []
    SepratorHeight = CalcBoxBorderMARGIN
    for i in range(len(YValues)):
        Seperators.append(MyRect(\
             CalcBoxx , # x
             YValues[i], # y
             CalcBoxw, # w
             SepratorHeight,# h
             WHITE,# color
             thickness = 0))
    return(Seperators)

SFSSeperators = createSFSSeperators()

def drawSFSSeperators():
    for seperator in SFSSeperators:
        seperator.draw()


# SFS Text Background

def createSFSTextBackground():
    YValues = getSFSSeperatorYValues(NumberOfSFSSlots[0], KPBMargin)
    YValues = YValues[:-1]
    XValues = [SFSLeftUpButton.x, SFSRightUpButton.x]
    Rectangles = []
    Width = SFSLeftUpButton.w
    Height = YValues[1] - YValues[0] - CalcBoxBorderMARGIN
    for x in XValues:
        for y in YValues:
            Rectangles.append(\
                MyRect(\
             x, # x
             y, # y
             Width, # w
             Height,# h
             BLUE,# color
             thickness = 0)  \
             )
    return(Rectangles)

SFSTextBackgroundBoxes = createSFSTextBackground()

def drawSFSTextBackgroundBoxes(ButtonPressed, ButtonHover):    
    for box in SFSTextBackgroundBoxes:
        if ButtonPressed == box:
            box.draw2(LIGHTBLACK)
        elif ButtonHover == box:
            box.draw2(BLACK)
        else:
            box.draw()





# Special Functions Data and Text Slots
                            
SFSFunctionsTextSlotStartIndex = [0]


SpecialFunctionsList = [("abs(x)", "Absolute value of x", "abs"),
                        ("cosh(x)", "Hyperbolic cosine function", "cosh"),
                        ("ceiling(x)", "The smallest integral value ≥ x", "ceiling"),
                        ("fac(x)", "x!", "fac"),
                        ("floor(x)", "The smallest integral value ≤ x", "floor"),
                        ("Γ(x)", "Gamma function", "Γ"),
                        ("H(x)", "Heaviside step function", "H"),
                        ("max(a,b,c, ...)","Max value of the arguments", "max"),
                        ("min(a,b,c, ...)","Min value of the arguments", "min"),
                        ("mod(a,m)", "a (mod m) with 0 ≤ a < m ","mod"),
                        ("sinh(x)", "Hyperbolic sine function", "sinh")]

def CreateSpecialFunctionsTextSlots(NumberOfSFSSlots):
    NumberOfSFSSlots = NumberOfSFSSlots[0]
    XDistancefromLeftOfTextBackground = 3
    X = SFSTitleLeftTextBackground.x + XDistancefromLeftOfTextBackground
    YDistancefromTopOfTextBackground = -2
    YValues = \
            getSFSSeperatorYValues(NumberOfSFSSlots,\
                                   KPBMargin + CalcBoxBorderMARGIN \
                                   + YDistancefromTopOfTextBackground)
    TopTextSlotFontSize = 30
    BottomTextSlotFontSize = 24
    YDistanceFromTopTextSlotToBottomTextSlot = 18

    TopTextSlots = []
    for i in range(NumberOfSFSSlots):
        TopTextSlots.append(MyText(\
             X, #x
             YValues[i], #y
             BOLDFONT, #Font
             TopTextSlotFontSize, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False)) #staticbool)

    BottomTextSlots = []
    for i in range(NumberOfSFSSlots):
        BottomTextSlots.append(MyText(\
             X, #x
             YValues[i] + TopTextSlotFontSize\
             + YDistanceFromTopTextSlotToBottomTextSlot, #y
             BASICFONT, #Font
             BottomTextSlotFontSize, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False)) #staticbool)


        
    return TopTextSlots, BottomTextSlots


SFSFunctionsTopTextSlots = CreateSpecialFunctionsTextSlots(NumberOfSFSSlots)[0]
SFSFunctionsBottomTextSlots  = CreateSpecialFunctionsTextSlots(NumberOfSFSSlots)[1]




def drawSFSFunctionsTextSlots():
    for i in range(NumberOfSFSSlots[0]):
        SFSFunctionsTopTextSlots[i].write2(SpecialFunctionsList[\
           (SFSFunctionsTextSlotStartIndex[0] + i)\
                    % len(SpecialFunctionsList)][0])
        # TO ADD AN IMAGE FOR GAMMA MAKE AN IF STATEMENT HERE
        # CAN ALSO PUT A LINK TO WIKIPEDIA FOR MORE INFO
        SFSFunctionsBottomTextSlots[i].write2(SpecialFunctionsList[\
           (SFSFunctionsTextSlotStartIndex[0] + i)\
                    % len(SpecialFunctionsList)][1])
    
    # Keeping start index inbetween 0 and 7
    if SFSFunctionsTextSlotStartIndex[0] >= len(SpecialFunctionsList)  \
               or SFSFunctionsTextSlotStartIndex[0] < 0:
                SFSFunctionsTextSlotStartIndex[0] = \
                     SFSFunctionsTextSlotStartIndex[0]%len(SpecialFunctionsList)
    

# SFS constants  stuff

SFSConstantsTextSlotStartIndex = [0]

SFSConstantsList = [("c {in m/s}", "Speed of light in a vacuum", "c"),
                    ("Euler", "Euler's Number","Euler"),
                    ("ε {in (A²·s⁴)/(kg·m³)}", "Permittivity of free space", "ε"),
                    ("g {in m/s²}", "Accelration due to gravity on Earth", "g"),
                    ("G {in m³/(kg·s)}","Newtonian constant of gravitation", "G"),
                    ("h {in J·s}", "Planck's constant over 2π", "h"),
                    ("k {in (kg·m²)/(s²·K)}", "Boltzmann constant", "k"),
                    ("π", "(Circumference ÷ Diameter) for a circle","π")]

def CreateSFSConstantsTextSlots(NumberOfSFSSlots):
    NumberOfSFSSlots = NumberOfSFSSlots[0]
    XDistancefromLeftOfTextBackground = 2
    X = SFSTitleRightTextBackground.x + XDistancefromLeftOfTextBackground
    YDistancefromTopOfTextBackground = -2
    YValues = \
            getSFSSeperatorYValues(NumberOfSFSSlots,\
                                   KPBMargin + CalcBoxBorderMARGIN \
                                   + YDistancefromTopOfTextBackground)
    TopTextSlotFontSize = 30
    BottomTextSlotFontSize = 24
    YDistanceFromTopTextSlotToBottomTextSlot = 18

    TopTextSlots = []
    for i in range(NumberOfSFSSlots):
        TopTextSlots.append(MyText(\
             X, #x
             YValues[i], #y
             BOLDFONT, #Font
             TopTextSlotFontSize, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False)) #staticbool)

    BottomTextSlots = []
    for i in range(NumberOfSFSSlots):
        BottomTextSlots.append(MyText(\
             X, #x
             YValues[i] + TopTextSlotFontSize\
             + YDistanceFromTopTextSlotToBottomTextSlot, #y
             BASICFONT, #Font
             BottomTextSlotFontSize, #Fontsize
             "", #text
             WHITE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             False)) #staticbool)


        
    return TopTextSlots, BottomTextSlots



SFSConstantsTopTextSlots = CreateSFSConstantsTextSlots(NumberOfSFSSlots)[0]
SFSConstantsBottomTextSlots  = CreateSFSConstantsTextSlots(NumberOfSFSSlots)[1]


def drawSFSConstantsTextSlots():
    for i in range(NumberOfSFSSlots[0]):
        SFSConstantsTopTextSlots[i].write2(SFSConstantsList[\
           (SFSConstantsTextSlotStartIndex[0] + i)\
                    % len(SFSConstantsList)][0])
        SFSConstantsBottomTextSlots[i].write2(SFSConstantsList[\
           (SFSConstantsTextSlotStartIndex[0] + i)\
                    % len(SFSConstantsList)][1])
       


def drawSpecialFunctionsMenu(ButtonPressed, ButtonHover):
    SpecialFunctionsScreen.draw()
    SFSMiddleBorder.draw()
    SFSTitleDividor.draw()
    SFSTitleLeftTextBackground.draw()
    SFSTitleRightTextBackground.draw()
    SFSTitleLeftText.write()
    SFSTitleRightText.write()
    drawSFSNavButtons(ButtonPressed, ButtonHover)
    drawSFSSeperators()
    drawSFSTextBackgroundBoxes(ButtonPressed, ButtonHover)
    drawSFSFunctionsTextSlots()
    drawSFSConstantsTextSlots()
    #SFSFunctionsScrollWheelZone.draw()
    #SFSConstantsScrollWheelZone.draw()

    

## ScrollWheel Function stuff


SFSFunctionsScrollWheelZone = MyRect(\
             SFSTextBackgroundBoxes[0].x, # x
             SFSTextBackgroundBoxes[0].y, # y
             SFSLeftUpButton.w, # w
             # 1 below via trial and error (yes I know thats bad)
             (SFSLeftDownButton.y - 1) - \
             SFSTextBackgroundBoxes[0].y, # h
             GREEN, # color
             thickness = 0)

SFSConstantsScrollWheelZone = MyRect(\
             SFSFunctionsScrollWheelZone.x\
             + SFSFunctionsScrollWheelZone.w + KPBMargin, # x
             SFSFunctionsScrollWheelZone.y, # y
             SFSFunctionsScrollWheelZone.w, # w
             SFSFunctionsScrollWheelZone.h, # h
             PINK, # color
             thickness = 0)

COMPLETESFSFunctionsScrollWheelZone = []
#COMPLETESFSFunctionsScrollWheelZone.extend(SFSButtonList[:2])
COMPLETESFSFunctionsScrollWheelZone.extend(SFSTextBackgroundBoxes[:NumberOfSFSSlots[0]])
COMPLETESFSFunctionsScrollWheelZone.append(SFSFunctionsScrollWheelZone)

COMPLETESFSConstantsScrollWheelZone = []
#COMPLETESFSConstantsScrollWheelZone.extend(SFSButtonList[2:])
COMPLETESFSConstantsScrollWheelZone.extend(SFSTextBackgroundBoxes[NumberOfSFSSlots[0]:])
COMPLETESFSConstantsScrollWheelZone.append(SFSConstantsScrollWheelZone)




# function that keeps SFS index in a good range
# Keeping start index inbetween 0 and 7
def KeepSFSFunctionsStartIndexInRange():
    if SFSFunctionsTextSlotStartIndex[0] >= len(SpecialFunctionsList)  \
               or SFSFunctionsTextSlotStartIndex[0] < 0:
                SFSFunctionsTextSlotStartIndex[0] = \
                     SFSFunctionsTextSlotStartIndex[0]%len(SpecialFunctionsList)

def KeepSFSConstantsStartIndexInRange():
    if SFSConstantsTextSlotStartIndex[0] >= len(SFSConstantsList)  \
               or SFSConstantsTextSlotStartIndex[0] < 0:
                SFSConstantsTextSlotStartIndex[0] = \
                     SFSConstantsTextSlotStartIndex[0]%len(SFSConstantsList)
