# File 5
import pygame, math, sys, copy
from pygame.locals import *
from GlobalConstantsLibrary import *
from InputBoxLibrary import *
from CalculatorOutput import *




# Deleting a single key, pass this function when
# detele keypad button or delete on keyboard is pressed

# special cases
InputBoxDeleteTextSpecialCaseList = [ "arccos(", "arcsin(",
                                      "arctan(", "e^(", "10^(",
                                      "tan(", "sin(", "cos(",
                                      "ln(", "log(", "√(", "^("]
                                      
    
def deleteInputBoxCharacter(INPUTBOX):
    deletedyet = False
    for text in InputBoxDeleteTextSpecialCaseList:
        if INPUTBOX.buttontext.endswith(text):
            INPUTBOX.buttontext = INPUTBOX.buttontext[:-len(text)]
            deletedyet = True
            break
    if not deletedyet:
        INPUTBOX.buttontext = INPUTBOX.buttontext[:-1]

### Formating text input string

# Radians to degrees functionn 

def degtorad(x):
    return x * ((math.pi)/180)




# Functions to that are altered
CNST1 = AccelerationDueToGravityOnEarth = 9.81
CNST2 = PI = math.pi
CNST3 = PlanksConstant = round(1.054571800 * (10**-34),45)
CNST4 = NewtonianG = 6.67408e-11
CNST5 = SpeedOfLight = 299792458
CNST6 = BoltzmannConstant = 1.38064852e-23
CNST7 = VacuumPermittivity =  8.854187817e-12
CNST8 = math.exp(1)

FunctionFormatList = [ \
["arcsin(", "FTN1("],
["arccos(", "FTN2("],
["arctan(", "FTN3("],
["sinh(", "FTN4("],
["cosh(", "FTN4N("],
["sin(", "FTN5("],
["cos(", "FTN6("],
["tan(", "FTN7("],
["ln(", "FTN8("],
["log(", "FTN9("],
["exp(", "FTN10("],
["e^(", "FTN10("],
["^(", " **("],
["^", " **"],
["·", "*"],
["√(", "FTN11("],
["mod(", "FTN12("],
["Γ(", "FTN13("],
["fac(","FTN14("],
["floor(", "FTN15("],
["ceiling(", "FTN16("],
["H(", "FTN17("],
["answer", "FTN18()"],
["ans", "FTN18()"],
["g", "CNST1"],
["π", "CNST2"],
["Pie", "CNST2"],
["PI", "CNST2"],
["Pi", "CNST2"],
["pi", "CNST2"],
["h", "CNST3"],
["G", "CNST4" ],
["c","CNST5"],
["Euler","CNST8"],
["k","CNST6"],
["ε", "CNST7"]]

#Functions that require multiple arguments, and the number of commas requried
# - 1 corresponds to no limit of number of arguments
MultiArgumentFunctionList = [("mod",1), ("max", -1), ("min",-1)]


ErrorEpsilon = 1e-15


def FTN1(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    return math.asin(x)

def FTN2(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    return math.acos(x)

def FTN3(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    return math.atan(x)

def FTN5(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    if abs(math.sin(x)) < ErrorEpsilon:
            return 0
    return math.sin(x)

def FTN6(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    if abs(math.cos(x)) < ErrorEpsilon:
            return 0
    return math.cos(x)

def FTN7(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    if abs(math.tan(x)) < ErrorEpsilon:
            return 0
    return math.tan(x)

def FTN8(x):
    return math.log(x)

def FTN9(x):
    return math.log(x, 10)

def FTN10(x):
    return math.exp(x)

def FTN11(x):
    return x**.5

def FTN4(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    return math.sinh(x)

def FTN4N(x):
    if AngleMode[0] == DegreeMode:
        x = degtorad(x)
    return math.cosh(x)



# SFSMode Special Functions

def FTN12(a,m): # a (mod m)
    return a%m

 
def FTN17(x): # heaviside
    if x < 0:
        return 0
    elif x == 0:
        return 0.5
    elif x > 0:
        return 1


def FTN13(x):
    return math.gamma(x)
def FTN14(x):
    total = 1
    for i in range(1,x+1):
        total = total*i
    return total
 
def FTN15(x): #floor
    return math.floor(x)

def FTN16(x): #ceiling
    return math.ceil(x)

def FTN18(): # get previous answer
    History = CalcOutputHistory
    if len(History) > 0:
        return float(History[0][1])
    else:
        return 0





# Evaluate and checks for invalid/bad input



def evlatuateText(Text):
    try:
        EvaluatedText = eval(Text)
        if str(type(EvaluatedText)) ==\
           "<class 'builtin_function_or_method'>":
            return "Syntax Error"
        elif str(type(EvaluatedText)) == \
             "<class 'type'>":
            return "Syntax Error"
    except SyntaxError:
        return "Syntax Error"
    except ZeroDivisionError:
        return "Zero Division Error"
    except NameError:
        return "Name Error"
    except ValueError:
        return "Value Error"
    except OverflowError:
        return "Overflow Error"
    except TypeError:
        return "Inappropriate Number of Arguments"
    return str(EvaluatedText)

#Error List
ErrorList = ["Syntax Error", "Zero Division Error", "Name Error", "Value Error",
             "Overflow Error", "inf", "Inappropriate Number of Arguments", \
             "No complex numbers allowed... yet!"]

TextInputErrorsList = ["··", "//"]


# function used to restore inputboxtext to blank after button pressed
# when error is displayed

def makeInputBoxTextBlankIfErrored():
    if CalcModeInputBox.buttontext in ErrorList:
        CalcModeInputBox.buttontext = ""


def SigFigRound(number,sigfigs):
    if float(number) == float("inf"):
        return "inf"
    if float(number) == 0:
        return "0"
    else:
        FinalNumber = str(round(float(number),
                -int(math.log10(abs(float(number)))) + (sigfigs - 1)))
        return  FinalNumber
                


def FormatHelperFunction(text):
    #check to make sure text is not list
    #if type(eval(text)) == list:
     #   return "Syntax Error"
    
    if text in ErrorList:
        return text
    # dealing with complex numbers (not allowed)
    elif type(eval(text)) == list:
        return "Syntax Error"
    elif type(eval(text)) == tuple:
        return "Syntax Error"
    elif complex(text).imag !=  0:
        return "No complex numbers allowed... yet!"
    else:
        return text


def formatTextInput(TextInput):
    # Change the functions to functions readable by python
    # USE FOR ELEMENT IN FUNCTIONALTERLIST: WHILE ELMENT[0] in current text
    # REPLACE ELEMENT[0] by ELEMENT[1]
    if TextInput == "":
        return ""
    if TextInput in ErrorList:
        return ""

    # making sure python ** exponentiation isnt used (or other errors found)

    for element in TextInputErrorsList:
        if (element in TextInput):
            return "Syntax Error"



    
    FormatedText = TextInput
    for element in FunctionFormatList:
        if element[0] in FormatedText:
            FormatedText = FormatedText.replace(element[0], \
                                                element[1])
    EvaluatedText = evlatuateText(FormatedText)
    if EvaluatedText[-2:] == ".0":
        EvaluatedText = EvaluatedText[:-2]

 
    #print(EvaluatedText)
    
    EvaluatedText = FormatHelperFunction(EvaluatedText)

    
    # error removal stuff:
    # dealing with built in functions like abs

    if EvaluatedText in ErrorList:
        return EvaluatedText

    
    
    #CAN COMBINE THIS
    if EvaluatedText not in ErrorList:
        RoundedText = SigFigRound(EvaluatedText,30)
        if RoundedText[-2:] == ".0":
            RoundedText = RoundedText[:-2]
    
    # AND THIS
    if len(EvaluatedText) >= 32: 
        return RoundedText
    else:
        return EvaluatedText
            



# MEMORY BUTTON FUNCTIONS





# SetMemory() is in text Formmating library
def SetMemory():
    Text = formatTextInput(CalcModeInputBox.buttontext)
    if (Text != "") and (Text not in ErrorList):
        Memory[0] = Text
        
def MemoryRecall():
    CalcModeInputBox.buttontext = Memory[0]
    
def ClearMemory():
    Memory[0] = None

def AddToMemory():
    FormatedText = formatTextInput(CalcModeInputBox.buttontext)
    if (FormatedText not in ErrorList) and\
       (FormatedText != ""):
        Memory[0] = str( float(Memory[0]) + float(CalcModeInputBox.buttontext) )
        if Memory[0][-2:] == ".0":
                Memory[0] = Memory[0][:-2]

def SubtractFromMemory():
    FormatedText = formatTextInput(CalcModeInputBox.buttontext)
    if (FormatedText not in ErrorList) and\
       (FormatedText != ""):
        Memory[0] = str( float(Memory[0]) - float(CalcModeInputBox.buttontext) )
        if Memory[0][-2:] == ".0":
                Memory[0] = Memory[0][:-2]

                
# Comma mode



def IsInCommaMode():
    # Checks to see total number of commas vs number of commas requrired
    Text = CalcModeInputBox.buttontext
    NumberOfCommasRequired = 0
    FunctionRightIndices = []
    for function in MultiArgumentFunctionList:
        if function[0] + "(" in Text:
            if (function[1] == -1) or \
               (NumberOfCommasRequired == -1):
                NumberOfCommasRequired = -1
            else:
                NumberOfCommasRequired += function[1]
            FunctionRightIndices.append(Text.rfind(function[0]))
    TotalNumberOfCommas = Text.count(",")
    # this is bad in terms of how to deal with the comma mode,
    # but this is just a quick/easy/not-perfect way to do it
    if len(FunctionRightIndices) > 1:
        RightmostFunctionIndex = max(FunctionRightIndices)
    elif len(FunctionRightIndices) == 1:
        RightmostFunctionIndex = FunctionRightIndices[0]
    else:
        RightmostFunctionIndex = None
    if RightmostFunctionIndex != None:
        NumberofLeftBrackets = Text.count("(", RightmostFunctionIndex)
        NumberofRightBrackets = Text.count(")", RightmostFunctionIndex)
        if NumberofRightBrackets >= NumberofLeftBrackets:
            return False

    if NumberOfCommasRequired == -1:
        return True
    elif NumberOfCommasRequired > TotalNumberOfCommas:
        return True
    else:
        return False


#this is a VERY professional way of taking care of the
#alignment issue ...
CommaModeStuffxAdjustment = KPBMargin
CommaModeStuffyAdjustment = - CommaModeStuffxAdjustment

CommaModeText = MyText(InputBoxx + 5 + CommaModeStuffxAdjustment, #x
             InputBoxButtony + InputBoxh - 18 + CommaModeStuffyAdjustment, #y
             BOLDFONT, #Font
             12, #Fontsize
             "Click Here to add a comma to seperate function arguments", #text
             BLUE, #textcolor
             TXTCOORDMODEtopleft, #textcoordmode
             True) #staticbool


CommaModeTextBackGround = MyRect(InputBoxx + CommaModeStuffxAdjustment,
                                 CommaModeText.y,
                                 380,
                                 (InputBoxy + InputBoxh) - CommaModeText.y\
                                 + CommaModeStuffyAdjustment,
                                 WHITE,
                                 0)
                                 
CommaModeTextBackGroundBorder = MyRect(CommaModeTextBackGround.x,
                                 CommaModeTextBackGround.y + CommaModeStuffyAdjustment ,
                                 CommaModeTextBackGround.w + CommaModeStuffxAdjustment,
                                 CommaModeTextBackGround.h - CommaModeStuffyAdjustment,
                                 WHITE,
                                 0)
    
def drawCommaModeButton(ButtonPressed,ButtonHover):
    CommaMode[0] = IsInCommaMode()
    if CommaMode[0]:
        CommaModeTextBackGroundBorder.draw()
        if ButtonPressed == CommaModeTextBackGround:
            CommaModeTextBackGround.draw2(GRAY)
            CommaModeText.writeColor(BLACK)
        elif ButtonHover == CommaModeTextBackGround:
            CommaModeTextBackGround.draw2(BLACK)
            CommaModeText.writeColor(WHITE)
        else:
            CommaModeTextBackGround.draw()
            CommaModeText.write()
        
    
