# Generated from Array.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ArrayParser import ArrayParser
else:
    from ArrayParser import ArrayParser

# This class defines a complete listener for a parse tree produced by ArrayParser.
class ArrayListener(ParseTreeListener):

    # Enter a parse tree produced by ArrayParser#init.
    def enterInit(self, ctx:ArrayParser.InitContext):
        print("\"", end="")
        pass

    # Exit a parse tree produced by ArrayParser#init.
    def exitInit(self, ctx:ArrayParser.InitContext):
        print("\"", end="")
        pass


    # Enter a parse tree produced by ArrayParser#value.
    def enterValue(self, ctx:ArrayParser.ValueContext):
        if ctx.INT() is not None:
            print(f"[{ctx.INT().getText()}]", end="")
        pass


    # Exit a parse tree produced by ArrayParser#value.
    def exitValue(self, ctx:ArrayParser.ValueContext):
        pass



del ArrayParser