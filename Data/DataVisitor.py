# Generated from Data.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DataParser import DataParser
else:
    from DataParser import DataParser

# This class defines a complete generic visitor for a parse tree produced by DataParser.

class DataVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DataParser#data.
    def visitData(self, ctx:DataParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataParser#group.
    def visitGroup(self, ctx:DataParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DataParser#sequence.
    def visitSequence(self, ctx:DataParser.SequenceContext):
        return self.visitChildren(ctx)



del DataParser