import re

from Function import *

class NormeChecker:
    def __init__(self, filename):
        self._filename = filename
        self._typeReg = r"(int|float|char|double)"
        self._beginWithReg = r"^"
        self._requiredReg = r"+"
        self._spaceReg = r"( )"
        self._oneOrMoreReg = r"+"
        self._zeroOrMoreReg = r"*"
        self._alphaNumericReg = r"([a-z]|[A-Z]|[0-9])"
        self._alphaNumericReg = r"\w"
        self._openParentheseReg = r"\("
        self._closeParentheseReg = r"\)"
        self._anythingReg = r"."
        self._openScopeReg = r"\{"
        self._closeScopeReg = r"\}"

        self._functionList = []

    def isAFunction(self, line):
        return re.match("\w*\s\w*\([\w*\ ,]*\)\s*{"
                        , line) is not None

    def isAPrototype(self, line):
        return re.match("\w*\s\w*\([\w*\ ,]*\)\s*;",
                        line) is not None

    def loadFile(self):
        i = 0
        isInFunction = False

        with open(self.Filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if self.isAFunction(line)== True:
                    function = Function(line, i)
                    self._functionList.append(function)
                    isInFunction = True
                elif self.isAPrototype(line) and isInFunction == True:
                    isInFunction = False
                    functionString = ""
                elif isInFunction == True:
                    function.function += line
                ++i

    def display(self):
        for file in self._functionList:
            print("function : ")
            print(file.function)

    def check(self):
        for file in self._functionList:
            file.getFaults()

# properties
    def _get_filename(self):
        return self._filename

    def _set_filename(self, newFilename):
        self._filename = newFilename

    Filename = property(_get_filename, _set_filename)

norme = NormeChecker("test.c")
norme.loadFile()
norme.display()
norme.check()
