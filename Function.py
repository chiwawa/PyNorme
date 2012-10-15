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
        self._function = func
        self.keywords = list({"while", "if", "else if", "else", "return"})
        self.regexKeyword = r"while|if|else|else if|return"

        print("Begin line : " + str(nb))
        self._begin_line_number = nb
        print("Begin line : " + str(self._begin_line_number))
        self._currentIndex = 0;

        print "Check function\n%s" %self.function

    def trimLine(self, line):
        return re.sub('".*"', "", line)

    def checkKeywords(self, line, fullstr, linenb):
        a = re.findall("(while|if|else|else\ if|return)\ {2,}\(|(while|if|else|else\ if|return)\(", line)#; is not None:
        if len(a) > 0:
            print "Norme Error : missing space after keyword, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr

    def checkSpaceBinaryOperator(self, line, fullstr, linenb):
        a = re.findall("[\+|/|-|\*|%|=](\w|\ {2,})", line) ## spaces after operators
        a2 = re.findall("(\w|\ {2,})[\+|/|-|\*|%|=]", line)
        if len(a) > 0 or len(a2) > 0:
            print "Norme Error : missing space after binary operator, line : %d" %(linenb + self.BeginLineNumber)
            print "-------> " + fullstr

    def checkDeclarativePart(self):
        """Verifie les declarations de variable de l'attribut function"""

    def checkFunctionCall(self):
        """Verifie les appels de function de l'attribut function"""

    def getNextLine(self):
        index = self.function.find("\n", self._currentIndex)
        if index == -1:
            return None

        s = self.function[self._currentIndex:index]
        self._currentIndex = index + 1;
        return s

    def getFaults(self):
        i = 0
        fullstr = self.getNextLine()
        while fullstr is not None:
            s = self.trimLine(fullstr)
            self.checkKeywords(s, fullstr, i)
            self.checkSpaceBinaryOperator(s, fullstr, i)

            fullstr = self.getNextLine()
            i = i + 1

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
