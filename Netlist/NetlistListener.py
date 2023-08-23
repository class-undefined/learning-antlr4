# Generated from Netlist.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NetlistParser import NetlistParser
else:
    from NetlistParser import NetlistParser

# This class defines a complete listener for a parse tree produced by NetlistParser.
class NetlistListener(ParseTreeListener):

    # Enter a parse tree produced by NetlistParser#subckts.
    def enterSubckts(self, ctx:NetlistParser.SubcktsContext):
        pass

    # Exit a parse tree produced by NetlistParser#subckts.
    def exitSubckts(self, ctx:NetlistParser.SubcktsContext):
        pass


    # Enter a parse tree produced by NetlistParser#subckt.
    def enterSubckt(self, ctx:NetlistParser.SubcktContext):
        pass

    # Exit a parse tree produced by NetlistParser#subckt.
    def exitSubckt(self, ctx:NetlistParser.SubcktContext):
        pass


    # Enter a parse tree produced by NetlistParser#subcktHeader.
    def enterSubcktHeader(self, ctx:NetlistParser.SubcktHeaderContext):
        pass

    # Exit a parse tree produced by NetlistParser#subcktHeader.
    def exitSubcktHeader(self, ctx:NetlistParser.SubcktHeaderContext):
        pass


    # Enter a parse tree produced by NetlistParser#subcktBody.
    def enterSubcktBody(self, ctx:NetlistParser.SubcktBodyContext):
        pass

    # Exit a parse tree produced by NetlistParser#subcktBody.
    def exitSubcktBody(self, ctx:NetlistParser.SubcktBodyContext):
        pass


    # Enter a parse tree produced by NetlistParser#subcktFooter.
    def enterSubcktFooter(self, ctx:NetlistParser.SubcktFooterContext):
        pass

    # Exit a parse tree produced by NetlistParser#subcktFooter.
    def exitSubcktFooter(self, ctx:NetlistParser.SubcktFooterContext):
        pass


    # Enter a parse tree produced by NetlistParser#node.
    def enterNode(self, ctx:NetlistParser.NodeContext):
        pass

    # Exit a parse tree produced by NetlistParser#node.
    def exitNode(self, ctx:NetlistParser.NodeContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameters.
    def enterParameters(self, ctx:NetlistParser.ParametersContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameters.
    def exitParameters(self, ctx:NetlistParser.ParametersContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameter.
    def enterParameter(self, ctx:NetlistParser.ParameterContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameter.
    def exitParameter(self, ctx:NetlistParser.ParameterContext):
        pass


    # Enter a parse tree produced by NetlistParser#components.
    def enterComponents(self, ctx:NetlistParser.ComponentsContext):
        pass

    # Exit a parse tree produced by NetlistParser#components.
    def exitComponents(self, ctx:NetlistParser.ComponentsContext):
        pass


    # Enter a parse tree produced by NetlistParser#component.
    def enterComponent(self, ctx:NetlistParser.ComponentContext):
        pass

    # Exit a parse tree produced by NetlistParser#component.
    def exitComponent(self, ctx:NetlistParser.ComponentContext):
        pass


    # Enter a parse tree produced by NetlistParser#arguments.
    def enterArguments(self, ctx:NetlistParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by NetlistParser#arguments.
    def exitArguments(self, ctx:NetlistParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by NetlistParser#argument.
    def enterArgument(self, ctx:NetlistParser.ArgumentContext):
        pass

    # Exit a parse tree produced by NetlistParser#argument.
    def exitArgument(self, ctx:NetlistParser.ArgumentContext):
        pass


    # Enter a parse tree produced by NetlistParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:NetlistParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:NetlistParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#PowerExpression.
    def enterPowerExpression(self, ctx:NetlistParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#PowerExpression.
    def exitPowerExpression(self, ctx:NetlistParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:NetlistParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:NetlistParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#NotExpression.
    def enterNotExpression(self, ctx:NetlistParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#NotExpression.
    def exitNotExpression(self, ctx:NetlistParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:NetlistParser.PreDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:NetlistParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:NetlistParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:NetlistParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:NetlistParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:NetlistParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:NetlistParser.PostDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:NetlistParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:NetlistParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:NetlistParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:NetlistParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:NetlistParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:NetlistParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:NetlistParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:NetlistParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:NetlistParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:NetlistParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:NetlistParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:NetlistParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:NetlistParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:NetlistParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:NetlistParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:NetlistParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:NetlistParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:NetlistParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:NetlistParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:NetlistParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:NetlistParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:NetlistParser.AssignmentOperatorExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:NetlistParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#CoalesceExpression.
    def enterCoalesceExpression(self, ctx:NetlistParser.CoalesceExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#CoalesceExpression.
    def exitCoalesceExpression(self, ctx:NetlistParser.CoalesceExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NetlistParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NetlistParser#number.
    def enterNumber(self, ctx:NetlistParser.NumberContext):
        pass

    # Exit a parse tree produced by NetlistParser#number.
    def exitNumber(self, ctx:NetlistParser.NumberContext):
        pass


    # Enter a parse tree produced by NetlistParser#pureNumber.
    def enterPureNumber(self, ctx:NetlistParser.PureNumberContext):
        pass

    # Exit a parse tree produced by NetlistParser#pureNumber.
    def exitPureNumber(self, ctx:NetlistParser.PureNumberContext):
        pass



del NetlistParser