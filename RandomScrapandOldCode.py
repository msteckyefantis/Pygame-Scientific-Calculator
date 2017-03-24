                # Mouse button released
                elif ( event.type == MOUSEBUTTONUP ):
                    mouseButtonUpCalcMode(ButtonPressed)
                     # If released on the same button it was pressed down on
                     if ( ButtonPressed != None ) and \
                        isMouseInButtonZone(pygame.mouse.get_pos(),
                                            ButtonPressed):
                         # if released on keypad button that types
                         if (ButtonPressed not in NonTextKPButtons) and \
                            (ButtonPressed in CompleteKPButtonList):
                             CalcModeInputBox.buttontext = \
                                    CalcModeInputBox.buttontext + \
                                    ButtonPressed.inputboxtext
                             
                         # if released on clear button
                         elif ButtonPressed == ClearButton:
                             CalcModeInputBox.buttontext = \
                                    ""
                             
                         # if released on inverse button
                         elif ButtonPressed == INVButton:
                             if ModesList[1] == keypad:
                                 ModesList[1] = INVkeypad
                             else:
                                 ModesList[1] = keypad
                             
                         # if delete button is pressed and released
                         elif ButtonPressed == DeleteButton:
                             deleteInputBoxCharacter(CalcModeInputBox)

                         # if the enter button is pressed     
                         #elif ButtonPressed == EnterButton:
                             
                         ButtonPressed = None


                     # If released NOT on the same button it was pressed down on
                     else:
                         ButtonPressed = None
#############

FUCKYOU = MyText(666,
             222,
             BASICFONT,
             69,
             "1",
             PINK,
             TXTCOORDMODEmidleft,
             False)

FUCKYOU.text = str( int(FUCKYOU.text) + 1)

FUCKYOU.write()


#############

def TESTDRAW():
    for a in range(len(CalcBoxTextCoords)):
        pygame.draw.rect(DISPLAYSURF, BLACK,
                             (CalcBox.rectparam[0],
                              CalcBoxTextCoords[a][0],
                              12,12) )
        pygame.draw.rect(DISPLAYSURF, BLACK,
                             (CalcBox.rectparam[0],
                              CalcBoxTextCoords[a][1],
                              12,12) )



###
Slot1TOP =  MyText(CalcBox.rectparam[0],
                CalcOutputTextYCoords[0][0],
                BASICFONT,
                22,
                CalcOutputList[Slot1TextIndex],
                BLACK,
                TXTCOORDMODEmidleft,
                False)


#####

ScrollButton = Button( \
ScrollButtonx,
CalcBox.y,
ScrollButtonWidth,
getScrollButtonHeight(),
BLUE, #bg color
None, # button text
None, # input box text
None, #text font
None, # text color
None, # text size
None, # text size adjustment
None, # text coordmode 
None,# text x position
None, # text y position
None,# text x position adjustment
None, # text y position adjustment
False, # border bool
None, # border color
None, # border margin
YELLOW, # highlight color
ORANGE, # pressed color
None, # mode tuple
textstaticbool = True) #text static bool




# calculator box text background

def CreateCalcBoxTextBackground(NumberOfCalcBoxSections, CalcBoxLineWidth):
    X = CalcBox.rectparam[0] + KPBMargin
    NewYList = []
    NewYList.append(CalcBox.rectparam[1])
    NewYList.extend(CalcBoxLineY)
    Y = []
    for i in range(len(NewYList)):
        Y.append(NewYList[i] + KPBMargin + CalcBoxLineWidth)
    W = CalcBox.rectparam[2] - (2 * KPBMargin)
    H = CalcBoxLineY[2] - CalcBoxLineY[1] \
        - (2 * KPBMargin) - CalcBoxLineWidth
    Color = DARKGRAY

    Rects = []
    for i in range(NumberOfCalcBoxSections):
        Rects.append( MyRect(X,
                             Y[i],
                             W,
                             H,
                             Color,
                             0))
    return Rects

CalcBoxTextBackground = \
 CreateCalcBoxTextBackground(NumberOfCalcBoxSections, CalcBoxLineWidth)


def drawCalcBoxTextBackground():
    for i in range(len(CalcBoxTextBackground)):
        CalcBoxTextBackground[i].draw()

