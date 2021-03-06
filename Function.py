#!/usr/bin/python2.7

import sys
import re

class Function:
    """Classe qui parse une fonction
    - checkKeywords
    - checkDeclarativePart
    - checkFunctionCall
    """

    def __init__(self, func, nb):
        """Prends une fonction en parametre et la met dans l'attribut function"""
        self._function = func[0:func.rfind("}") + 1]
#        self._function = func[0:self._function.rfind("}")]
        self.keywords = list({"while", "if", "else if", "else", "return"})
        self.regexKeyword = r"while|if|else|else if|return"
        self.isInDeclarationPart = True

        print("Begin line : " + str(nb))
        self._begin_line_number = nb
        print("Begin line : " + str(self._begin_line_number))
        self._currentIndex = 0;

        print ("Check function\n" + self._function)

    def trimLine(self, line):
        return re.sub('".*"', "", line)

    def checkKeywords(self, line, fullstr, linenb):
        a = re.findall("(while|if|else|else\ if|return)\ {2,}\(", line)#; is not None:
        if len(a) > 0:
            print "Norme Error : too much spaces after keyword, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr
        a = re.findall("(while|if|else|else\ if|return)\(", line)#; is not None:
        if len(a) > 0:
            print "Norme Error : missing space after keyword, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr

    def checkFunctionSpaces(self, line, fullstr, linenb):
        a = re.findall("(?!while).*(?!return).*(?!if).*(?!else\ if).*\ {1,}\(", line)
        a = re.findall("\w*\ +\(", line)

        if len(a) > 0:
            if a[0].find("while") == -1 and a[0].find("return") == -1 and a[0].find("if") == -1 and a[0].find("else if") == -1:
                print "Norme Error : too much spaces after function call, line : %d" %(linenb + self.BeginLineNumber)
                print "-------> " + fullstr

    def checkSpaceBinaryOperator(self, line, fullstr, linenb):
        a = re.findall("[\+|/|-|\*|%|=](\w|\ {2,})", line) ## spaces after operators
        a2 = re.findall("(\w|\ {2,})[\+|/|-|\*|%|=]", line)
        if len(a) > 0 or len(a2) > 0:
            print "Norme Error : missing space after binary operator, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr

    def checkMisplacedScope(self, line, fullstr, linenb):
        a = re.findall("\w*\s\w*\([\w*\ *, = > < ! + -]*\)\s*{", line)
        if len(a) > 0:
            print "Norme Error : misplaced scope, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr

    def checkIfStillIsInDeclarationPart(self, line, fullstr, linenb):
        a = re.findall("^[\s]+$", line)
        if len(a) > 0 or len(line) == 0:
            self.isInDeclarationPart = False

    def checkIfDeclarationIsSeparated(self, line, fullstr, linenb):
        if self.isInDeclarationPart == True:
            print "Norme Error : function ended without separation between declarations and instructions: %d" %(linenb + self.BeginLineNumber)

    def checkDeclarativePart(self, line, fullstr, linenb):
        a = re.findall("\w+\s+\w+", line)
        if len(a) > 0:
            if a[0].find("return") != -1:
                return 0
            if self.isInDeclarationPart == False:
                print "Norme Error : declaration is only allowed in the beginning of the function : %d" %(linenb + self.BeginLineNumber)
                print "-------> " + fullstr
            a = re.findall("=", line)
            if len(a) > 0:
                print "Norme Error : initialization in declaration is not allowed : %d" %(self.BeginLineNumber)
                print "-------> " + fullstr

    def getNextLine(self):
        index = self.function.find("\n", self._currentIndex)
        if index == -1:
            return None

        s = self.function[self._currentIndex:index]
        self._currentIndex = index + 1;
        return s

    def getFaults(self):


        self.function = self.function[0:self.function.rfind("}") + 1]
        i = 0
        fullstr = self.getNextLine()
        ## check function signature
        fullstr = self.getNextLine()
        while fullstr is not None:
            s = self.trimLine(fullstr)
            self.checkIfStillIsInDeclarationPart(s, fullstr, i)
            self.checkKeywords(s, fullstr, i)
            self.checkFunctionSpaces(s, fullstr, i)
            self.checkSpaceBinaryOperator(s, fullstr, i)
            self.checkMisplacedScope(s, fullstr, i)
            self.checkDeclarativePart(s, fullstr, i)

            fullstr = self.getNextLine()
            i = i + 1
        self.checkIfDeclarationIsSeparated(fullstr, fullstr, i)

## Properties
    def _get_function(self):
        """Methode qui retourne l'attribut _function"""
        return self._function

    def _set_function(self, new_func):
        """Methode qui modifie l'attribut _function"""
        self.function = new_func

    function = property(_get_function, _set_function)

    def _get_begin_line_number(self):
        return self._begin_line_number
    def _set_begin_line_number(self, value):
        self._begin_line_number = value

    BeginLineNumber = property(_get_begin_line_number, _set_begin_line_number)
