# FILE 3

import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from InputBoxLibrary import *


# Drawing Keypad Button Container (KBC)
KBCSideMargin = 15

KBCButtonName = "Keypad Button Container"
KBCx = KBCSideMargin
KBCy = InputBoxButtony + InputBoxButtonh + KBCSideMargin
KBCw = 253
KBCh = 304
KBCbgcolor = WHITE
#KBCbgcolor = GRAY
KBCbuttontext = None
KBCinputboxtext = None
KBCtextfont = None
KBCtextcolor = None
KBCtextsize = None
KBCtextsizeadjustment = None
KBCtextcoordmode = None
KBCtextXposition = None
KBCtextYposition = None
KBCtextXpositionadjustment = None
KBCtextYpositionadjustment = None
KBCborderbool = True
KBCbordercolor = WHITE
#KBCbordercolor = DARKGRAY
#KBCbordermargin = 5
KBCbordermargin = 0
KBCmodetuple = (CalcMode)

KBC = Button(KBCx,
        KBCy,
        KBCw,
        KBCh,
        KBCbgcolor,
        KBCbuttontext,
        KBCinputboxtext,
        KBCtextfont,
        KBCtextcolor,
        KBCtextsize,
        KBCtextsizeadjustment,
        KBCtextcoordmode,
        KBCtextXposition,
        KBCtextYposition,
        KBCtextXpositionadjustment,
        KBCtextYpositionadjustment,
        KBCborderbool,
        KBCbordercolor,
        KBCbordermargin,
        None,
        None,
        KBCmodetuple)



# Getting Keypad Button Locations (KPB = Keypad Button)
# KPBA = Keypad Button A
KPBAW = (KBC.rectparam[2] - (KPBMargin * 6) ) /5
KPBAH = (KBC.rectparam[3] - (KPBMargin * 8) ) /7


#Getting pixel coordinates
def getPixelCoordinates(StartX,StartY):
    Coordinates = []
    for x in range(5):
        Coordinates.append([])
        for y in range(7):
            Coordinates[x].append( (StartX + (x * (KPBAW + KPBMargin) ),StartY + (y * (KPBAH + KPBMargin)) )  )

    return Coordinates
    

TopLeftKPBPixelCoords =  getPixelCoordinates(KBC.rectparam[0] + KPBMargin, KBC.rectparam[1] + KPBMargin) 
CenterKPBPixelCoords =  getPixelCoordinates(KBC.rectparam[0] + KPBMargin + (KPBAW / 2), KBC.rectparam[1] + KPBMargin  + (KPBAH / 2))

######
# Creating A-type Buttons
KPSQRT = "√"
KPEXP =  "aˣ"
KP7 = "7"
KP4 = "4"
KP1 = "1"
KP8 = "8"
KP5 = "5"
KP2 = "2" 
KP9 = "9"
KP6 = "6"
KP3 = "3"
KPDOT = "."
KPDIVIDE = "÷" 
KPMULTIPLY = "·"
KPMINUS = "-"
KPPLUS = "+"
KPLBRACKET = "("
KPRBRACKET = ")"


def createButtonA(x,
                  y,
                  ButtonText,
                  InputBoxText,
                  textsizeadjustment,
                  textXpositionadjustment,
                  textYpositionadjustment):
   ReturnButton = Button(TopLeftKPBPixelCoords[x][y][0],
                         TopLeftKPBPixelCoords[x][y][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         ButtonText, 
                         InputBoxText,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         28,# FONT SIZE
                         textsizeadjustment,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[x][y][0],
                         CenterKPBPixelCoords[x][y][1],#15
                         textXpositionadjustment + 1,
                         textYpositionadjustment,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))
   return ReturnButton
                         


# Creating Keypad A Buttons Dictionary

KPBAdic = {
#Name      : [ x, y, Button Text, Input Box Text, textsizeadjustment, text X adj, text y adj]
KPSQRT     : [ 3, 1, KPSQRT, "√(", 0, 0, -2],
KPEXP      : [ 3, 2, KPEXP,  "^(", 0, 0, -2],
KP7        : [ 0, 3, KP7 , KP7, 0, 0, -2],
KP4        : [ 0, 4, KP4 , KP4, 0, 0, -2],
KP1        : [ 0, 5, KP1 , KP1, 0, 0, -2],
KP8        : [ 1, 3, KP8 , KP8, 0, 0, -2],
KP5        : [ 1, 4, KP5 , KP5, 0, 0, -2],
KP2        : [ 1, 5, KP2 , KP2, 0, 0, -2],
KP9        : [ 2, 3, KP9 , KP9, 0, 0, -2],
KP6        : [ 2, 4, KP6 , KP6, 0, 0, -2],
KP3        : [ 2, 5, KP3 , KP3, 0, 0, -2],
KPDOT      : [ 2, 6, KPDOT , KPDOT, 0, 0, -2],
KPDIVIDE   : [ 3, 3, KPDIVIDE , "/", 0, 0, -2],
KPMULTIPLY : [ 3, 4, KPMULTIPLY , KPMULTIPLY, 0, 0, -2],
KPMINUS    : [ 3, 5, KPMINUS , KPMINUS, 0, 0, -2],
KPPLUS     : [ 3, 6, KPPLUS , KPPLUS, 0, 0, -2],
KPLBRACKET : [ 0, 0,KPLBRACKET, KPLBRACKET, 0, 0, -2],
KPRBRACKET : [ 1, 0, KPRBRACKET, KPRBRACKET, 0,0, -2]}
# Creating the Buttons and putting them in a list

def createButtonList(createButtonFunction, ButtonsDic):
    ButtonList = []
    for element in ButtonsDic:
        ButtonList.append(createButtonFunction(ButtonsDic[element][0],
                                          ButtonsDic[element][1],
                                          ButtonsDic[element][2],
                                          ButtonsDic[element][3],
                                          ButtonsDic[element][4],
                                          ButtonsDic[element][5],
                                          ButtonsDic[element][6]) )
    return ButtonList

ATypeButtons = createButtonList(createButtonA,KPBAdic)

######
# Creating B-type Buttons
KPLN = "ln"
KPLOG = "log"
KPSIN = "sin"
KPCOS = "cos"
KPTAN = "tan"

def createButtonB(x,
                  y,
                  ButtonText,
                  InputBoxText,
                  textsizeadjustment,
                  textXpositionadjustment,
                  textYpositionadjustment):
   ReturnButton = Button(TopLeftKPBPixelCoords[x][y][0],
                         TopLeftKPBPixelCoords[x][y][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         ButtonText, 
                         InputBoxText,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         22,# FONT SIZE
                         textsizeadjustment,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[x][y][0],
                         CenterKPBPixelCoords[x][y][1],#15
                         textXpositionadjustment,
                         textYpositionadjustment,
                         False, # NO BORDER unlike inbetween usa and mexico
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, CalcMode))
   return ReturnButton

KPBBdic ={
#Name      : [ x, y, Button Text, Input Box Text, textsizeadjustment, text X adj, text y adj]
KPLN       : [ 0, 1, KPLN, "ln(", 0, 0, 0],
KPLOG      : [ 1, 1, KPLOG, "log(", 0, 0, 0],
KPSIN      : [ 0, 2, KPSIN, "sin(", 0, 0, 0],
KPCOS      : [ 1, 2, KPCOS, "cos(", 0, 0, 0],
KPTAN      : [ 2, 2, KPTAN, "tan(", 0, 0, 0]}

BTypeButtons = createButtonList(createButtonB, KPBBdic)


######
# Creating INVERSE B-type Buttons
KPEXPE = "eˣ"
KPEXP10 = "10ˣ"
KPARCSIN = "arcsin"
KPARCCOS = "arccos"
KPARCTAN = "arctan"

def createButtonINVB(x,
                  y,
                  ButtonText,
                  InputBoxText,
                  textsizeadjustment,
                  textXpositionadjustment,
                  textYpositionadjustment):
   ReturnButton = Button(TopLeftKPBPixelCoords[x][y][0],
                         TopLeftKPBPixelCoords[x][y][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         ButtonText, 
                         InputBoxText,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         22,# FONT SIZE
                         textsizeadjustment,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[x][y][0],
                         CenterKPBPixelCoords[x][y][1],#15
                         textXpositionadjustment,
                         textYpositionadjustment,
                         False, # NO BORDER unlike inbetween usa and mexico
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (INVkeypad, CalcMode))
   return ReturnButton

KPBINVBdic ={
#Name      : [ x, y, Button Text, Input Box Text, textsizeadjustment, text X adj, text y adj]
KPEXPE     : [ 0, 1, KPEXPE, "e^(", 0, 0, 0],
KPEXP10    : [ 1, 1, KPEXP10 , "10^(", 0, 0, 0],
KPARCSIN      : [ 0, 2, KPARCSIN, "arcsin(", -8, 0, 0],
KPARCCOS      : [ 1, 2, KPARCCOS, "arccos(", -8, 0, 0],
KPARCTAN      : [ 2, 2, KPARCTAN, "arctan(", -8, 0, 0]}

INVBTypeButtons = createButtonList(createButtonINVB, KPBINVBdic)


######
# Creating keypad buttons type C
KPX = "x"
KPY = "y"
KP0 = "0"

def createButtonC(x,
                  y,
                  ButtonText,
                  InputBoxText,
                  textsizeadjustment,
                  textXpositionadjustment,
                  textYpositionadjustment):
   ReturnButton = Button(TopLeftKPBPixelCoords[x][y][0],
                         TopLeftKPBPixelCoords[x][y][1],
                         (KPBAW),  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         ButtonText, 
                         InputBoxText,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         28,# FONT SIZE
                         textsizeadjustment,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[x][y][0],
                         CenterKPBPixelCoords[x][y][1],#15
                         textXpositionadjustment,
                         textYpositionadjustment - 1,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad)) # ADD GRAPHING MODE
   return ReturnButton


KPBCdic ={
#Name      : [ x, y, Button Text, Input Box Text, textsizeadjustment, text X adj, text y adj]
KPX      : [ 0, 0, KPX, KPX, 0, 0, 0],
KPY      : [ 1, 0, KPY , KPY, 0, 0, 0]}


CTypeButtons = createButtonList(createButtonC, KPBCdic)


##########
# Creating INV, DELETE, ZERO AND ENTER BUTTONS
KPINV = "inv"
INVButton = Button(TopLeftKPBPixelCoords[2][1][0],
                         TopLeftKPBPixelCoords[2][1][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         KPINV, 
                         None,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         22,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[2][1][0],
                         CenterKPBPixelCoords[2][1][1],#15
                         0,
                         0,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))


KP0 = "0"
ZeroButton = Button(TopLeftKPBPixelCoords[0][6][0],
                         TopLeftKPBPixelCoords[0][6][1],
                         (2 * KPBAW) + KPBMargin,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         KP0, 
                         KP0,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         28,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[0][6][0] + (.5 * KPBAW),
                         CenterKPBPixelCoords[0][6][1],#15
                         0,
                         -1,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))

KPCLEAR = "clear"
ClearButton = Button(TopLeftKPBPixelCoords[3][0][0],
                         TopLeftKPBPixelCoords[3][0][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         KPCLEAR, 
                         None,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         15,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[3][0][0],
                         CenterKPBPixelCoords[3][0][1],#15
                         0,
                         -1,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))

KPANS = "ans"
ANSButton = Button(TopLeftKPBPixelCoords[2][0][0],
                         TopLeftKPBPixelCoords[2][0][1],
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         KPANS, 
                         "ans",
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         22,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[2][0][0],
                         CenterKPBPixelCoords[2][0][1],#15
                         0,
                         -1,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))


KPDELETE = "delete"
DeleteButton = Button(TopLeftKPBPixelCoords[4][0][0],
                         TopLeftKPBPixelCoords[4][0][1],
                         KPBAW,  # APPROPRIATE H AND W
                         (KPBAH * 3) + (KPBMargin * 2) ,#5
                         BLUE, # COLOR
                         KPDELETE, 
                         None,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         13,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[4][2][0],
                         CenterKPBPixelCoords[4][2][1],#15
                         0,
                         0,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))

KPENTER = "enter"
EnterButton = Button(TopLeftKPBPixelCoords[4][3][0],
                         TopLeftKPBPixelCoords[4][3][1],
                         KPBAW,  # APPROPRIATE H AND W
                         (KPBAH * 4) + (KPBMargin * 3) ,#5
                         BLUE, # COLOR
                         KPENTER, 
                         None,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         15,# FONT SIZE
                         0,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[4][6][0],
                         CenterKPBPixelCoords[4][6][1],#15
                         0,
                         0,
                         False,
                         None,
                         None,
                         BLACK,
                         LIGHTBLACK,
                         (keypad, INVkeypad, CalcMode))


# Creating keypad button list with all buttons
CompleteKPButtonList = []
CompleteKPButtonList.extend(ATypeButtons)
CompleteKPButtonList.extend(BTypeButtons)
CompleteKPButtonList.extend(INVBTypeButtons)
CompleteKPButtonList.extend(CTypeButtons)
CompleteKPButtonList.append(ZeroButton) 
CompleteKPButtonList.append(INVButton)
CompleteKPButtonList.append(EnterButton)
CompleteKPButtonList.append(DeleteButton)
CompleteKPButtonList.append(ClearButton)
CompleteKPButtonList.append(ANSButton)


NonTextKPButtons = [INVButton, DeleteButton, EnterButton, ClearButton, \
                    ANSButton]
    
#(self,
 #                x, y, w ,h,
  #               bgcolor,
   #              buttontext,
    #             inputboxtext,
     #            textfont,
      #           textcolor,
       #          textsize,
        #         textsizeadjustment,
         #        textcoordmode,
          #       textXposition,
           #      textYposition,
            #     textXpositionadjustment,
             #    textYpositionadjustment,
              #   borderbool,
               #  bordercolor,
                # bordermargin,
                # highlightcolor,
                # pressedcolor,
                # modetuple,
                # textstaticbool = True)





##########################
##### Memory buttons ANGLEMEM SECTION


# NOTE THE RADIANSELECTOR BOX: RSB
# SHOULD ACTUALLY BE MEMORY SELECTOR BOX: MSB

# RadianSelectorBorderBox RSBB
RSBBx = InputBoxButtonx
RSBBy = KBCy + KBCh +  KBCSideMargin
RSBBw =  KBCw
RSBBh = KPBAH + (2 * KPBMargin) + (2 * KBCbordermargin)

RadianSelectorBorderBox = MyRect(\
             RSBBx,
             RSBBy,
             RSBBw,
             RSBBh,
             WHITE,
             thickness = 0)

# RadianSelctorInsideColor RSIC

RSICx = InputBoxButtonx + KBCbordermargin
RSICy = KBCy + KBCh +  KBCSideMargin + KBCbordermargin
RSICw =  KBCw - (2 * KBCbordermargin)
RSICh = KPBAH + (2 * KPBMargin)

RadianSelctorInsideColor = MyRect(\
             RSICx,
             RSICy,
             RSICw,
             RSICh,
             WHITE,
             thickness = 0)




# Memeory Buttons M, MR, MC, M+, M-

# Creating A-type Buttons
MEMM= "M"
MEMMR = "MR"
MEMMC = "MC"
MEMMPLUS = "M+"
MEMMMINUS = "M-"

def createMemButton(x,
                  y,
                  ButtonText,
                  InputBoxText,
                  textsizeadjustment,
                  textXpositionadjustment,
                  textYpositionadjustment):
   ReturnButton = Button(TopLeftKPBPixelCoords[x][y][0],
                         RSICy + KPBMargin,
                         KPBAW,  # APPROPRIATE H AND W
                         KPBAH,#5
                         BLUE, # COLOR
                         ButtonText, 
                         InputBoxText,
                         BOLDFONT, #BOLD FONT
                         WHITE,#10 #FONT COLOR
                         20,# FONT SIZE
                         textsizeadjustment,
                         TXTCOORDMODEcenter, #TXT CORD IN CENTER
                         CenterKPBPixelCoords[x][y][0],
                         RSICy + KPBMargin + int((.5 * KPBAH)),#15
                         textXpositionadjustment,
                         textYpositionadjustment,
                         False,
                         None,
                         None,
                         (RED[0] + 0, RED[1] + 85, RED[2] + 85),
                         (RED[0] + 0, RED[1] + 120, RED[2] + 120),
                         (keypad, INVkeypad, CalcMode))
   return ReturnButton
                         


# Creating Memory Buttons Dictionary

MEMdic = [
#Name      : [ x, y, Button Text, Input Box Text, textsizeadjustment, text X adj, text y adj]
[MEMM, 0, 0, MEMM, None, 0, 0, 0],
[MEMMR, 1, 0, MEMMR,  None, 0, 0, 0],
[MEMMC,  2, 0, MEMMC , None, 0, 0, 0],
[MEMMPLUS , 3, 0, MEMMPLUS , None, 0, 0, 0],
[MEMMMINUS , 4, 0, MEMMMINUS , None, 0, 0, 0]]


# Creating the Buttons and putting them in a list

def createButtonListFromButtonsList(createButtonFunction, List):
    NewButtonList = []
    for i in range(len(List)):
        NewButtonList.append(createButtonFunction(\
                                          List[i][1],
                                          List[i][2],
                                          List[i][3],
                                          List[i][4],
                                          List[i][5],
                                          List[i][6],
                                          List[i][7]) )
    return NewButtonList




MemButtons = createButtonListFromButtonsList(createMemButton, MEMdic)









# Memory Buttons Symbol MBS

MBSx = InputBoxx + InputBoxw - 18
MBSy = InputBoxButtony + 18
MBSFont = BOLDFONT
MBSFontsize = 20
MBStext = "M"
MBStextcolor = WHITE
MBStextcoordmode = TXTCOORDMODEcenter

MemoryButtonSymbol = MyText(\
             MBSx,
             MBSy,
             MBSFont,
             MBSFontsize,
             MBStext,
             MBStextcolor,
             MBStextcoordmode,
             True)
    


# Drawing all of the memory (and angle mode) stuff

def drawMemButtons(ButtonPressed, ButtonHover):
    RadianSelectorBorderBox.draw()
    RadianSelctorInsideColor.draw()
    for button in MemButtons:
        if ButtonPressed == button:
            button.draw(button.pressedcolor)
        elif ButtonHover == button:
            button.draw(button.highlightcolor)
        else:
            button.draw()
    if Memory[0] != None:
        MemoryButtonSymbol.write()





######## Radian mode stuff ###################

# Real Real Border Box RRBB

RRBBx = CalcModeInputBox.x + CalcModeInputBox.w + KPBMargin
RRBBy = CalcModeInputBox.y
RRBBw = WINDOWWIDTH - RRBBx - KPBMargin
RRBBh = CalcModeInputBox.h
RRBBColor = BLUE
RRBBBorderColor = BLUE
RRBBBorderWidth = 0

RadianModeButtonBorder = Button(
                 RRBBx, #x
                 RRBBy, #y
                 RRBBw, #w
                 RRBBh, #h
                 RRBBColor, #bg color
                 None, #buttontext
                 None, #inputboxtext
                 None, #textfont
                 None, #textcolor
                 None, #textsize
                 None, #textsizeadjustment
                 None, #textcoordmode
                 None, #textXposition
                 None, #textYposition
                 None, #textXpositionadjustment
                 None, #textYpositionadjustment
                 True, #borderbool
                 RRBBBorderColor, #bordercolor
                 RRBBBorderWidth, #bordermargin
                 None, #highlightcolor
                 None, #pressedcolor
                 None, #modetuple
                 True)



RadianSelectorButtonx = RRBBx + InputBoxBorderMARGIN + KPBMargin
RadianSelectorButtony = RRBBy + KPBMargin

RadianSelectorButtonHeight = int((CalcModeInputBox.h - (3 *KPBMargin)) /2)
RadianSelectorButtonWidth = (RadianModeButtonBorder.w) - (2 * KPBMargin) \
                            - (2 * InputBoxBorderMARGIN)

AngleModeSelectorTextSize = 20

AngleModeSelectorONColor = BLUE

AngleModeSelectorOFFColor = GRAY

RadianModeButton = Button(
                 RadianSelectorButtonx, #x
                 RadianSelectorButtony, #y
                 RadianSelectorButtonWidth, #w
                 RadianSelectorButtonHeight, #h
                 AngleModeSelectorONColor, #bg color
                 "rad", #buttontext
                 None, #inputboxtext
                 BOLDFONT, #textfont
                 WHITE, #textcolor
                 AngleModeSelectorTextSize, #textsize
                 0, #textsizeadjustment
                 TXTCOORDMODEcenter, #textcoordmode
                 (RadianSelectorButtonx) + (RadianSelectorButtonWidth/2) , #textXposition
                 RadianSelectorButtony + (RadianSelectorButtonHeight/2), #textYposition
                 0, #textXpositionadjustment
                 0, #textYpositionadjustment
                 False, #borderbool
                 None, #bordercolor
                 None, #bordermargin
                 None, #highlightcolor
                 None, #pressedcolor
                 None, #modetuple
                 True)

DegreeModeButton = Button(
                 RRBBx + InputBoxBorderMARGIN + KPBMargin, #x
                 RadianModeButton.y + \
                 RadianModeButton.h + KPBMargin, #y
                 RadianSelectorButtonWidth, #w
                 RadianSelectorButtonHeight, #h
                 AngleModeSelectorOFFColor, #bg color
                 "deg", #buttontext
                 None, #inputboxtext
                 BOLDFONT, #textfont
                 WHITE, #textcolor
                 AngleModeSelectorTextSize, #textsize
                 0, #textsizeadjustment
                 TXTCOORDMODEcenter, #textcoordmode
                 (RadianSelectorButtonx) + (RadianSelectorButtonWidth/2), #textXposition
                 (RadianSelectorButtony) + (RadianSelectorButtonHeight/2) +\
                 +  RadianModeButton.h + KPBMargin, #textYposition
                 0, #textXpositionadjustment
                 0, #textYpositionadjustment
                 False, #borderbool
                 None, #bordercolor
                 None, #bordermargin
                 None, #highlightcolor
                 None, #pressedcolor
                 None, #modetuple
                 True)


AngleSelctorButtons = [RadianModeButton, DegreeModeButton]

RadianModeButtonBorder2 = MyRect(RRBBx + InputBoxButtonBorderMARGIN,
                                 CalcModeInputBox.y,
                                 RRBBw - (2*InputBoxButtonBorderMARGIN),
                                 CalcModeInputBox.h,
                                 WHITE,
                                 0)

                                 


def SwitchAngleModes():
    if AngleMode[0] == RadianMode:
        AngleMode[0] = DegreeMode
        RadianModeButton.bgcolor = AngleModeSelectorOFFColor
        DegreeModeButton.bgcolor = AngleModeSelectorONColor
    else:
        AngleMode[0] = RadianMode
        RadianModeButton.bgcolor = AngleModeSelectorONColor
        DegreeModeButton.bgcolor = AngleModeSelectorOFFColor


def drawAngleModeSelectorBox(ButtonHover, ButtonPressed):
    RadianModeButtonBorder2.draw()
    if AngleMode[0] == RadianMode:
        RadianModeButton.draw()
        if ButtonPressed == DegreeModeButton:
            DegreeModeButton.draw(LIGHTGRAY)
        elif ButtonHover == DegreeModeButton:
            DegreeModeButton.draw(ALMOSTLIGHTGRAY)
        else:
            DegreeModeButton.draw()
    elif AngleMode[0] == DegreeMode:
        DegreeModeButton.draw()
        if ButtonPressed == RadianModeButton:
            RadianModeButton.draw(LIGHTGRAY)
        elif ButtonHover == RadianModeButton:
            RadianModeButton.draw(ALMOSTLIGHTGRAY)
        else:
            RadianModeButton.draw()
