# Generated from Hello.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#r.
    def enterR(self, ctx:HelloParser.RContext):
        pass

    # Exit a parse tree produced by HelloParser#r.
    def exitR(self, ctx:HelloParser.RContext):
        pass



del HelloParser