# Generated from Netlist.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NetlistParser import NetlistParser
else:
    from NetlistParser import NetlistParser

# This class defines a complete generic visitor for a parse tree produced by NetlistParser.

class NetlistVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NetlistParser#subckts.
    def visitSubckts(self, ctx:NetlistParser.SubcktsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#subckt.
    def visitSubckt(self, ctx:NetlistParser.SubcktContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#subcktHeader.
    def visitSubcktHeader(self, ctx:NetlistParser.SubcktHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#subcktBody.
    def visitSubcktBody(self, ctx:NetlistParser.SubcktBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#subcktFooter.
    def visitSubcktFooter(self, ctx:NetlistParser.SubcktFooterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#node.
    def visitNode(self, ctx:NetlistParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameters.
    def visitParameters(self, ctx:NetlistParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameter.
    def visitParameter(self, ctx:NetlistParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#components.
    def visitComponents(self, ctx:NetlistParser.ComponentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#component.
    def visitComponent(self, ctx:NetlistParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#arguments.
    def visitArguments(self, ctx:NetlistParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#argument.
    def visitArgument(self, ctx:NetlistParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:NetlistParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#PowerExpression.
    def visitPowerExpression(self, ctx:NetlistParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:NetlistParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#NotExpression.
    def visitNotExpression(self, ctx:NetlistParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:NetlistParser.PreDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:NetlistParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:NetlistParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:NetlistParser.PostDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:NetlistParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:NetlistParser.BitXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:NetlistParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:NetlistParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:NetlistParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:NetlistParser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:NetlistParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:NetlistParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:NetlistParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:NetlistParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:NetlistParser.AssignmentOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#CoalesceExpression.
    def visitCoalesceExpression(self, ctx:NetlistParser.CoalesceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#number.
    def visitNumber(self, ctx:NetlistParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#pureNumber.
    def visitPureNumber(self, ctx:NetlistParser.PureNumberContext):
        return self.visitChildren(ctx)



del NetlistParser