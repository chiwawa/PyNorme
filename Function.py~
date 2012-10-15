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

        self._begin_line_number = nb
        self._currentIndex = 0;

        print "Check function\n%s" %self.function

    def checkKeywords(self, line, linenb):
        print("Check :" + line)
        if re.findall("(while|if|else|else if|return)\ {2+}\(|(while|if|else|else if|return)\(", line) is not None:
            print("Norme Error : missing space after keyword, line : " + str(linenb + self._begin_line_number))
            sys.exit()
            ##print (re.search(self.regexKeyword, self.function))

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
        s = self.getNextLine()
        while s is not None:
            self.checkKeywords(s, i)
            s = self.getNextLine()
            ++i

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
