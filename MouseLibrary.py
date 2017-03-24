# File 4

import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from InputBoxLibrary import *
from KeypadLibrary import *
from TextFormatingLibrary import *
from CalculatorOutput import *
from SpecialFunctionsAndConstants import *



# determines if mouse is over a button
def isMouseInButtonZone(MOUSEPOSITION, button):
    if          (MOUSEPOSITION[0] >= button.rectboundary[0]) \
            and (MOUSEPOSITION[0] <= button.rectboundary[1]) \
            and (MOUSEPOSITION[1] >= button.rectboundary[2]) \
            and (MOUSEPOSITION[1] <= button.rectboundary[3]):
            return True
    else:
        return False

def isMouseInMyRect(MOUSEPOSITION, button): # LOL AT NAME WTF
    if          (MOUSEPOSITION[0] >= (button.x) )\
            and (MOUSEPOSITION[0] <= (button.x + button.w) )\
            and (MOUSEPOSITION[1] >= (button.y)) \
            and (MOUSEPOSITION[1] <= (button.y + button.h)):
            return True
    else:
        return False

# returns the button if the mouse is hovering over a button
def getHoverState(ButtonPressed):
    #if ButtonPressed == None:
    if True:
        #Checking if Mouse is hovering a keypad button
        for button in CompleteKPButtonList:
        # Making sure the for loop only goes through buttons in the
        # right keypad mode
            if (ModesList[0] in button.modetuple) and \
               (ModesList[1] in button.modetuple):  
                if isMouseInButtonZone(pygame.mouse.get_pos(), button):
                    return button
        # Checking if mouse is hovering Memory Buttons
        for button in MemButtons:
            if isMouseInButtonZone(pygame.mouse.get_pos(), button):
                return button
        #checking if mouse is hovering special functions button
        if isMouseInMyRect(pygame.mouse.get_pos(), SFBTextBorder):
            return SFBTextBorder
        #Checking if Mouse is hovering Angle selector Button
        for button in AngleSelctorButtons:
            if isMouseInMyRect(pygame.mouse.get_pos(), button ):
                return button
        #Checking if mouse in on SFS NavButton
        if ScreenMode[0] == SpecialFunctionsScreenMode:
            for button in SFSButtonList:
                if isMouseInMyRect(pygame.mouse.get_pos(), button):
                    return button
        #Checking if mouse is on SFS Function or Constant button
            for button in SFSTextBackgroundBoxes:
                if isMouseInMyRect(pygame.mouse.get_pos(), button):
                    return button
        if ScreenMode[0] == None:
            if isMouseInMyRect(pygame.mouse.get_pos(), ScrollButton):
                return ScrollButton
        # checking if mouse is hovering SFS button
        if (CommaMode[0] == True) and \
           isMouseInMyRect(pygame.mouse.get_pos(), CommaModeTextBackGround):
            return CommaModeTextBackGround
        # checking if mouse is hovering CalcBox
        if (ScreenMode[0] == None) and \
           isMouseInMyRect(pygame.mouse.get_pos(), CalcBox):
            return CalcBox
        return None
    else:
        return None



# what happens when mouse button is pressed down

def MousePressedDown(ButtonHover,
                     mouseposition):
    ButtonPressed = ButtonHover
    return ButtonPressed



# what happens when the mouse button is released when keypad button is pressed

def mouseKeypadButtonUpFunctionsCM(ButtonPressed):
    # if mouse button is released on the same button it pressed
    if ( ButtonPressed != None ) and \
            (ButtonPressed in CompleteKPButtonList) and \
                isMouseInButtonZone(pygame.mouse.get_pos(),
                    ButtonPressed):
        # removing error text when button is pressed and released
        if (CalcModeInputBox.buttontext in ErrorList)\
            and (ButtonPressed != INVButton):
            CalcModeInputBox.buttontext = ""
        else:
            # if released on a keypad button that types
            if (ButtonPressed not in NonTextKPButtons):
                makeInputBoxTextBlankIfErrored()
                CalcModeInputBox.buttontext += \
                ButtonPressed.inputboxtext
                if InputBoxTextSizeHitLimit():
                    CalcModeInputBox.buttontext =\
                     CalcModeInputBox.buttontext[:-len(ButtonPressed.inputboxtext)]
                                     
            # if released on the clear button
            elif ButtonPressed == ClearButton:
                CalcModeInputBox.buttontext = ""
                                 
            # if released on inverse button
            elif ButtonPressed == INVButton:
                if ModesList[1] == keypad:
                    ModesList[1] = INVkeypad
                else:
                    ModesList[1] = keypad
                #for testing keybaord stuff
                #print(KeyboardButtonPressedStatus[0])
                    
                                 
            # if delete button is pressed and released
            elif ButtonPressed == DeleteButton:
                makeInputBoxTextBlankIfErrored()
                deleteInputBoxCharacter(CalcModeInputBox)

             # if released on the answer button
            elif ButtonPressed == ANSButton:
                if len(CalcOutputHistory) >= 1:
                    CalcModeInputBox.buttontext += CalcOutputHistory[0][1]
                    if InputBoxTextSizeHitLimit():
                        CalcModeInputBox.buttontext =\
                        CalcModeInputBox.buttontext[:-len(CalcOutputHistory[0][1])]
                else:
                    pass
                
            # if pressed and released on enter button     
            elif ButtonPressed == EnterButton:
                EnterButtonFunctions()              
                
       

        # if pressed and released on Special functions button
    elif (ButtonPressed == SFBTextBorder) and \
         isMouseInMyRect(pygame.mouse.get_pos(),
                    SFBTextBorder):
        if ScreenMode[0] == None:
            ScreenMode[0] =  SpecialFunctionsScreenMode
        else:
            ScreenMode[0] = None


        
#       # if a memory section button is pressed and released
    elif ButtonPressed in MemButtons and \
                            isMouseInButtonZone(pygame.mouse.get_pos(),
                            ButtonPressed):
        if ButtonPressed == RadianModeButton:
            SwitchAngleModes()
        elif (ButtonPressed == MemButtons[0]) and \
             ( CalcModeInputBox.buttontext != ""):
            SetMemory()
        elif (ButtonPressed == MemButtons[1]) and \
             (Memory[0] != None):
            MemoryRecall()
        elif (ButtonPressed == MemButtons[2]):
            ClearMemory()  
        elif (ButtonPressed == MemButtons[3]) and \
             (Memory[0] != None):
            AddToMemory()
        elif (ButtonPressed == MemButtons[4]) and \
             (Memory[0] != None):
            SubtractFromMemory()
#       # if an angle selector section button is pressed and released
    elif ((ButtonPressed == RadianModeButton) and \
         (AngleMode[0] == DegreeMode) and \
         isMouseInMyRect(pygame.mouse.get_pos(), \
                         RadianModeButton) ) \
                         or \
        ((ButtonPressed == DegreeModeButton) and \
         (AngleMode[0] == RadianMode) and \
         isMouseInMyRect(pygame.mouse.get_pos(), \
                         DegreeModeButton)):
        SwitchAngleModes()

#       # if SFS NAV button is pressed while in SFS Mode
    elif (ScreenMode[0] == SpecialFunctionsScreenMode) and \
          (ButtonPressed in SFSButtonList) and\
          (isMouseInMyRect(pygame.mouse.get_pos(),
                          ButtonPressed)):
        if ButtonPressed == SFSLeftDownButton:
            SFSFunctionsTextSlotStartIndex[0] += 1
        elif ButtonPressed == SFSLeftUpButton:
            SFSFunctionsTextSlotStartIndex[0] +=  -1
        elif ButtonPressed == SFSRightDownButton:
            SFSConstantsTextSlotStartIndex[0] += 1
        elif ButtonPressed == SFSRightUpButton:
            SFSConstantsTextSlotStartIndex[0] +=  -1
       # Keeping start index inbetween 0 and 7(did differently for SFS functions)
        if SFSConstantsTextSlotStartIndex[0] >= len(SFSConstantsList)  \
                               or SFSConstantsTextSlotStartIndex[0] < 0:
            SFSConstantsTextSlotStartIndex[0] = \
                SFSConstantsTextSlotStartIndex[0]%len(SFSConstantsList)
                    
         # if SFS ftn/csnt button is pressed  and released while in SFS Mode    
    elif (ScreenMode[0] == SpecialFunctionsScreenMode) and \
         (ButtonPressed in SFSTextBackgroundBoxes) and\
         (isMouseInMyRect(pygame.mouse.get_pos(),
                          ButtonPressed)):
        if (CalcModeInputBox.buttontext in ErrorList):
            CalcModeInputBox.buttontext = ""
        else:
            PressedSFSIndex = SFSTextBackgroundBoxes.index(ButtonPressed)
            # dealing with case when function button is pressed
            if PressedSFSIndex < (len(SFSTextBackgroundBoxes)/2):
                SFSListItemIndexIndex = \
                 (PressedSFSIndex + SFSFunctionsTextSlotStartIndex[0])% \
                 len(SpecialFunctionsList)
                CalcModeInputBox.buttontext += \
                    SpecialFunctionsList[SFSListItemIndexIndex][2] + "("
                if InputBoxTextSizeHitLimit():
                            CalcModeInputBox.buttontext =\
                            CalcModeInputBox.buttontext[:-len(SpecialFunctionsList[SFSListItemIndexIndex][2] + "(")]
           # dealing with case when constant button is pressed
            elif PressedSFSIndex >= (len(SFSTextBackgroundBoxes)/2):
                PressedSFSIndex += NumberOfSFSSlots[0]
                SFSListItemIndexIndex = \
                 (PressedSFSIndex + SFSConstantsTextSlotStartIndex[0])% \
                 len(SFSConstantsList)
                CalcModeInputBox.buttontext += \
                    SFSConstantsList[SFSListItemIndexIndex][2]
                if InputBoxTextSizeHitLimit():
                            CalcModeInputBox.buttontext =\
                            CalcModeInputBox.buttontext[:-len(SFSConstantsList[SFSListItemIndexIndex][2])]
    elif CommaMode[0] and (ButtonPressed == CommaModeTextBackGround) and\
          isMouseInMyRect(pygame.mouse.get_pos(),CommaModeTextBackGround):
        CalcModeInputBox.buttontext += ","

# Enter Button Functions

def EnterButtonFunctions(): 
    Unformated_Text = CalcModeInputBox.buttontext
    Formated_Text =  formatTextInput(CalcModeInputBox.buttontext)
    # screening out bad input
    if Unformated_Text == "":
        pass
    # condititon if same input is pressed as previous input
    #elif CalcOutputHistory != [] and\
     #    Unformated_Text == CalcOutputHistory[0][0][:-2]:
      #  pass
    elif Formated_Text in ErrorList:
        CalcModeInputBox.buttontext = Formated_Text
    # condititon if same input is pressed as unformated previous input
    elif (CalcOutputHistory != []) and\
        (Unformated_Text == CalcOutputHistory[0][1]):
        CalcModeInputBox.buttontext = ""
    else:
        CalcOutputHistory.insert(0, (Unformated_Text + " =", Formated_Text))
        CalcModeInputBox.buttontext = Formated_Text
        UpdateScrollButtonHeight()
        ScrollButton.y = CalcBoxy





# what happends when Scroll Button is Pressed Down
def ScrollButtonMouseDown(ButtonPressed):
    if ButtonPressed == ScrollButton:
        if ScrollButtonPressedY[0] == None:
            ScrollButtonPressedY[0] = pygame.mouse.get_pos()[1]\
                                      - ScrollButton.y


# Updating the Scroll Button y value if the scroll button is pressed
def GetScrollButtonY():
    NewScrollButtonY =  pygame.mouse.get_pos()[1] - ScrollButtonPressedY[0]
    NewScrollButtonBottomY = NewScrollButtonY + ScrollButton.h
    if NewScrollButtonY < CalcBoxy:
        return CalcBoxy
    elif NewScrollButtonBottomY > (CalcBoxy + CalcBoxh):
        return (CalcBoxy + CalcBoxh) - ScrollButton.h
    else:
        return NewScrollButtonY






# Checks if mouse is in SFS functions scroll zone
def IsMouseInSFSScrollWheelZone():
    if ScreenMode[0] == SpecialFunctionsScreenMode:
        for zone in COMPLETESFSFunctionsScrollWheelZone:
            if isMouseInMyRect(pygame.mouse.get_pos(), zone):
                return "Function Zone"
        for zone in COMPLETESFSConstantsScrollWheelZone:
            if isMouseInMyRect(pygame.mouse.get_pos(), zone):
                return "Consant Zone"
