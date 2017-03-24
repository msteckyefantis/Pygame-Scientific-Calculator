import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from InputBoxLibrary import *
from KeypadLibrary import *
from TextFormatingLibrary import *
from CalculatorOutput import *
from SpecialFunctionsAndConstants import *
from MouseLibrary import *




KeyboardAcceptableKeyList = \
[".", ",", "-", "+", "/", "^", "(", ")"]




def KeyboardMoveScrollBar(UpBool):
    Zones = getScrollButtonYPartitionZones()
    if UpBool:
        for i in range(1, len(Zones)):
            if (Zones[i][0] <= ScrollButton.y) and \
               (Zones[i][1] >= ScrollButton.y):
                ScrollButton.y = Zones[i-1][0]
    else:
        LastZoneIndex = len(Zones) - 1
        for i in range(LastZoneIndex-1,-1,-1):
            if (Zones[i][0] <= ScrollButton.y) and \
               (Zones[i][1] >= ScrollButton.y):
                ScrollButton.y = Zones[i+1][0]
        for i in range(LastZoneIndex, LastZoneIndex - 1, - 1):
            if (Zones[i][0] <= ScrollButton.y) and \
               (Zones[i][1] >= ScrollButton.y):
                ScrollButton.y = (CalcBoxy + CalcBoxh) \
                        -(ScrollButton.h)

#Deal with *, backspace, enter, 
def keyboardPressedDownFunctions(event, ButtonHover,ButtonPressed):
    if CalcModeInputBox.buttontext in ErrorList:
        CalcModeInputBox.buttontext = ""
    elif (event.unicode.isalnum()) or \
       (event.unicode in KeyboardAcceptableKeyList):
        CalcModeInputBox.buttontext += event.unicode
        if InputBoxTextSizeHitLimit():
                    CalcModeInputBox.buttontext =\
                     CalcModeInputBox.buttontext[:-len(event.unicode)]
    # multiply
    elif event.unicode == "*":
        CalcModeInputBox.buttontext += "·"
        if InputBoxTextSizeHitLimit():
            CalcModeInputBox.buttontext =\
                     CalcModeInputBox.buttontext[:-len("·")]
    # backspace
    elif (event.unicode == '\x08') or \
         (event.key == 127):
        deleteInputBoxCharacter(CalcModeInputBox)
    # enter
    elif event.unicode == '\r':
        EnterButtonFunctions()
    # esssssc
    elif event.unicode == '\x1b':
        CalcModeInputBox.buttontext  = ""
    # up button
    elif (ScreenMode[0] == None) and (event.key == 273) \
         and (ButtonPressed == None):
        KeyboardMoveScrollBar(True)
    # down button
    elif (ScreenMode[0] == None) and (event.key == 274) \
         and (ButtonPressed == None):
        KeyboardMoveScrollBar(False)
    # tab
    elif event.key == 9 and \
         KeyboardButtonPressedStatus[0][9] != 1:
        if ScreenMode[0] == None:
            ScreenMode[0] = SpecialFunctionsScreenMode
        else:
            ScreenMode[0] = None
    # space bar
    elif event.key  == 32 and \
         CalcModeInputBox.buttontext != "":
        CalcModeInputBox.buttontext += " "

        # TEST KEY '
    elif event.unicode == "'":
        #print(pygame.key.get_pressed())
        keylisty = pygame.key.get_pressed()
        indexlisty = []
        for i in range(len(keylisty)):
            if keylisty[i] == 1:
                indexlisty.append(i)
        print(indexlisty)



## keyboard Pressed Down Status



#### ScrollWheel functions






def ScrollWheelFunctions(ButtonPressed,ButtonHover,event):
    # scrolling up
    if (event.button == 4):
        if (ButtonHover == CalcBox):
            KeyboardMoveScrollBar(True)
        elif IsMouseInSFSScrollWheelZone() == "Function Zone":
            SFSFunctionsTextSlotStartIndex[0] -= 1
            KeepSFSFunctionsStartIndexInRange()
            ScrollWheelVariable[0] = 0
            ScrollWheelVariable[1] = 1 #timer
        elif IsMouseInSFSScrollWheelZone() == "Consant Zone":
            SFSConstantsTextSlotStartIndex[0] -= 1
            KeepSFSConstantsStartIndexInRange()
            ScrollWheelVariable[0] = 2
            ScrollWheelVariable[3] = 1 #timer
    # scrolling down
    elif (event.button == 5):
        if (ButtonHover == CalcBox):
            KeyboardMoveScrollBar(False)
        elif IsMouseInSFSScrollWheelZone() == "Function Zone":
            SFSFunctionsTextSlotStartIndex[0] += 1
            KeepSFSFunctionsStartIndexInRange()
            ScrollWheelVariable[0] = 1
            ScrollWheelVariable[2] = 1
        elif IsMouseInSFSScrollWheelZone() == "Consant Zone":
            SFSConstantsTextSlotStartIndex[0] += 1
            KeepSFSConstantsStartIndexInRange()
            ScrollWheelVariable[0] = 3
            ScrollWheelVariable[4] = 1

def ScrollWheelVariableReset():
    ScrollWheelVariable[0] = None
    for i in range(1,5):
        if ScrollWheelVariable[i] > 0:
            ScrollWheelVariable[i] -= .2 #0 to 1, increase to speed up
            #if ScrollWheelVariable[i] < 0: 
             #   ScrollWheelVariable[i] = 0
