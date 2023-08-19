# Generated from Array.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ArrayParser import ArrayParser
else:
    from ArrayParser import ArrayParser

# This class defines a complete generic visitor for a parse tree produced by ArrayParser.

class ArrayVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArrayParser#init.
    def visitInit(self, ctx:ArrayParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArrayParser#value.
    def visitValue(self, ctx:ArrayParser.ValueContext):
        print(ctx.getText())
        return self.visitChildren(ctx)



del ArrayParser