# Generated from Data.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DataParser import DataParser
else:
    from DataParser import DataParser

# This class defines a complete listener for a parse tree produced by DataParser.
class DataListener(ParseTreeListener):

    # Enter a parse tree produced by DataParser#data.
    def enterData(self, ctx:DataParser.DataContext):
        pass

    # Exit a parse tree produced by DataParser#data.
    def exitData(self, ctx:DataParser.DataContext):
        pass


    # Enter a parse tree produced by DataParser#group.
    def enterGroup(self, ctx:DataParser.GroupContext):
        pass

    # Exit a parse tree produced by DataParser#group.
    def exitGroup(self, ctx:DataParser.GroupContext):
        pass


    # Enter a parse tree produced by DataParser#sequence.
    def enterSequence(self, ctx:DataParser.SequenceContext):
        pass

    # Exit a parse tree produced by DataParser#sequence.
    def exitSequence(self, ctx:DataParser.SequenceContext):
        pass



del DataParser