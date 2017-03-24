# FINAL FILE
import pygame, math, sys, copy
from pygame.locals import *
# initialize pygame
pygame.init()

from GlobalConstantsLibrary import *
from InputBoxLibrary import *
from KeypadLibrary import *
from MouseLibrary import *
from TextFormatingLibrary import *
from CalculatorOutput import *
from SpecialFunctionsAndConstants import *
from Keyboard import *




####################### Main Loop
        ###########################
                #########################
def main(): 
    # Global variables
    global FPSCLOCK, ButtonHover, ButtonPressed

    # FPSCLOCK setup and key repeat rate
    FPSCLOCK = pygame.time.Clock()
    pygame.key.set_repeat(500, 12)

    # Display setup
    pygame.display.set_caption("Michael Stecky-Efantis' Scientific Calculator")
    DISPLAYSURF.fill(DARKGRAY)


    
    # main game loop
    while True:
        # event handling loops

        #reseting keyboard button status
        KeyboardButtonPressedStatusReset()
        ScrollWheelVariableReset()
        
        
        #CalcMode Functions and Event loop
        if ModesList[0] == CalcMode:

            # Mouse Hover
    
            #Keypad Hover Check
            ButtonHover = getHoverState(ButtonPressed)

            # Setting ScrollButton to proper height
            if ScrollButtonPressedY[0] != None:
                ScrollButton.y = GetScrollButtonY()
                
                
            
            for event in pygame.event.get():
                # Quiting Function
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    keyboardPressedDownFunctions(event, ButtonHover,ButtonPressed)
                    #print(event.key)
                    #print(event)
                    
                # Mouse pressed down on a button
                elif ( event.type == MOUSEBUTTONDOWN) and\
                     (event.button == 1):
                    ButtonPressed = MousePressedDown(ButtonHover,
                                     pygame.mouse.get_pos())
                    # Setting Scroll Button data if scroll button is pressed
                    ScrollButtonMouseDown(ButtonPressed)  
                    
                # Mouse button released
                elif ( event.type == MOUSEBUTTONUP ):
                    mouseKeypadButtonUpFunctionsCM(ButtonPressed)
                    ButtonPressed = None
                    ScrollButtonPressedY[0] = None

                elif (event.type == MOUSEBUTTONDOWN) and \
                     ((event.button == 4) or (event.button == 5)):
                    ScrollWheelFunctions(ButtonPressed,ButtonHover,event)
                    

        

        #print(ButtonHover, ButtonPressed)



        #DRAWING STUFF

        #InputBox
        drawInputBox(ButtonHover, ButtonPressed)

        #Keypad
        drawKeypad()

        # Calculator History
        if ScreenMode[0] == None:
            drawCalcBox()
            drawScrollButton()



        # Memory Buttons
        drawMemButtons(ButtonPressed, ButtonHover)

        # Special Functions Menu
        drawSpecialFunctionsButton(ButtonHover, ButtonPressed)
        if ScreenMode[0] == SpecialFunctionsScreenMode:
            drawSpecialFunctionsMenu(ButtonPressed, ButtonHover)
            SFSPseudoScrollButton.draw()

        # Angle Mode Selector
        drawAngleModeSelectorBox(ButtonHover, ButtonPressed)
        
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)





########### FUNCTIONS THAT HAD TO GO LAST (they requried info)


def UpdateHoverStateBarStatus(ButtonHover, ButtonPressed):
    DisplayText = str(ButtonHover)
    if ButtonPressed == None:    
        #KeypadStuff
        if not bool(ButtonHover):
            HoverStatusBarData[0] = ""
        elif DisplayText == "clear":
            HoverStatusBarData[0] = "clear all input"
        elif DisplayText == "ans":
            HoverStatusBarData[0] = "last answer"
        elif DisplayText == "(":
            HoverStatusBarData[0] = "left bracket"
        elif DisplayText == ")":
            HoverStatusBarData[0] = "right bracket"
        elif DisplayText == ".":
            HoverStatusBarData[0] = "decimal point"
        elif DisplayText == "+":
            HoverStatusBarData[0] = "add"
        elif DisplayText == "-":
            HoverStatusBarData[0] = "subtract"
        elif DisplayText == "·":
            HoverStatusBarData[0] = "multiply"
        elif DisplayText == "÷":
            HoverStatusBarData[0] = "divide"
        elif DisplayText == "aˣ":
            HoverStatusBarData[0] = "exponentiate"
        elif DisplayText == "√":
            HoverStatusBarData[0] = "square root"
        elif DisplayText == "inv":
            HoverStatusBarData[0] = "inv. functions"
        elif DisplayText == "M":
            HoverStatusBarData[0] = "set memory"
        elif DisplayText == "MR":
            HoverStatusBarData[0] = "recall memory"
        elif DisplayText == "MC":
            HoverStatusBarData[0] = "clear memory"
        elif DisplayText == "M+":
            HoverStatusBarData[0] = "+ to memory"
        elif DisplayText == "M-":
            HoverStatusBarData[0] = "- from memory"
        elif DisplayText == "x = 18.0 y = 505":
            HoverStatusBarData[0] = "switch mode"
        elif ButtonHover == ScrollButton:
            HoverStatusBarData[0] = "scroll bar"
        elif (DisplayText == "rad")\
             and (AngleMode[0] == DegreeMode) :
            HoverStatusBarData[0] = "radian mode"
        elif (DisplayText == "deg")\
             and (AngleMode[0] == RadianMode) :
            HoverStatusBarData[0] = "degree mode"
        elif (DisplayText == "rad")\
             and (AngleMode[0] == RadianMode) :
            HoverStatusBarData[0] = ""
        elif (DisplayText == "deg")\
             and (AngleMode[0] == DegreeMode) :
            HoverStatusBarData[0] = ""
        elif ButtonHover == CommaModeTextBackGround:
            HoverStatusBarData[0] = "add comma"
        elif ButtonHover in SFSTextBackgroundBoxes:
            SFSBoxIndex = SFSTextBackgroundBoxes.index(ButtonHover)
            if SFSBoxIndex <= 3:
                HoverStatusBarData[0] = "insert function"
            else:
                HoverStatusBarData[0] = "insert constant"
        elif ButtonHover in SFSButtonList :
            SFSBoxIndex = SFSButtonList.index(ButtonHover)
            if SFSBoxIndex <= 1:
                HoverStatusBarData[0] = "browse ftns."
            else:
                HoverStatusBarData[0] = "browse cnsts."
        elif ButtonHover == CalcBox:
            HoverStatusBarData[0] = ""
        else:
            HoverStatusBarData[0] = str(ButtonHover)
    


def DrawInputBoxButtonText(ButtonHover, ButtonPressed):
    UpdateHoverStateBarStatus(ButtonHover, ButtonPressed)
    if ScreenMode[0] == None:
        CalcModeStatusTextSlot.write3("Calculation History", 13,\
                                       CMSx - 14, InputBoxButtony + 22)
        
    elif ScreenMode[0] == SpecialFunctionsScreenMode:
        CalcModeStatusTextSlot.write3("Special Functions", 12,\
                                       CMSx - 4, InputBoxButtony + 8)
        CalcModeStatusTextSlot.write3("and", 12,\
                                       CMSx + 32, InputBoxButtony + 22)
        CalcModeStatusTextSlot.write3("Constants", 12,\
                                       CMSx + 14, InputBoxButtony + 35)
        
    CalcModeStatusTextSlot.write3("Calculator", 19,\
                                       InputBoxButtonx + 12,
                                       InputBoxButtony + 5)
    CalcModeStatusTextSlot.write3("Mode", 19,\
                                       InputBoxButtonx + 30,
                                       InputBoxButtony + 26)
    CalcModeStatusTextSlot.write3("Status", 22,\
                                       InputBoxButtonx + 24,
                                       InputBoxButtony + 56)
    CalcModeStatusTextSlot.write3(HoverStatusBarData[0],
                                       17,\
                                       CMSx - 12, CMSy + 31)
    
# funciton that draws the inputbox
def drawInputBox(ButtonHover, ButtonPressed):
    FormatInputBoxTextSize(CalcModeInputBox,
                           CalcModeInputBox.w - (3* InputBoxTextXAdjustment),
                           InputBoxFontSize,
                           InputBoxFontSize - 18,
                           InputBoxy,
                           InputBoxy + 18)
    CalcModeInputBoxButton.draw()
    drawInputBoxButtonTextBorders()
    DrawInputBoxButtonText(ButtonHover, ButtonPressed)
    CalcModeInputBox.draw()
    DrawInputBoxBorder()
    drawCommaModeButton(ButtonPressed,ButtonHover)


    
# function that draws the keypad
def drawKeypad():
    KBC.draw()
    for button in CompleteKPButtonList:
        #   ModesList = [ProgramMode, KeypadMode]
        if (ModesList[0] in button.modetuple) and \
           (ModesList[1] in button.modetuple):
            #drawing each button
            if ButtonPressed == button:
                button.draw(button.pressedcolor)
            elif  (ButtonHover == button) and (ButtonPressed == None):
                button.draw(button.highlightcolor)
            else:
                button.draw()

             

    
if __name__ == '__main__':
    main()
