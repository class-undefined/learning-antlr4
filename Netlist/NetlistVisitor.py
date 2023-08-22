# Generated from Netlist.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .NetlistParser import NetlistParser
else:
    from NetlistParser import NetlistParser

# This class defines a complete generic visitor for a parse tree produced by NetlistParser.

class NetlistVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NetlistParser#subckt.
    def visitSubckt(self, ctx:NetlistParser.SubcktContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#node.
    def visitNode(self, ctx:NetlistParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameter.
    def visitParameter(self, ctx:NetlistParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:NetlistParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#genericSelection.
    def visitGenericSelection(self, ctx:NetlistParser.GenericSelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#genericAssocList.
    def visitGenericAssocList(self, ctx:NetlistParser.GenericAssocListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#genericAssociation.
    def visitGenericAssociation(self, ctx:NetlistParser.GenericAssociationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#postfixExpression.
    def visitPostfixExpression(self, ctx:NetlistParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:NetlistParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#unaryExpression.
    def visitUnaryExpression(self, ctx:NetlistParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#unaryOperator.
    def visitUnaryOperator(self, ctx:NetlistParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#castExpression.
    def visitCastExpression(self, ctx:NetlistParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#shiftExpression.
    def visitShiftExpression(self, ctx:NetlistParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#relationalExpression.
    def visitRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#equalityExpression.
    def visitEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#andExpression.
    def visitAndExpression(self, ctx:NetlistParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx:NetlistParser.ExclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx:NetlistParser.InclusiveOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:NetlistParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#expression.
    def visitExpression(self, ctx:NetlistParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#constantExpression.
    def visitConstantExpression(self, ctx:NetlistParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declaration.
    def visitDeclaration(self, ctx:NetlistParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declarationSpecifiers.
    def visitDeclarationSpecifiers(self, ctx:NetlistParser.DeclarationSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declarationSpecifiers2.
    def visitDeclarationSpecifiers2(self, ctx:NetlistParser.DeclarationSpecifiers2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx:NetlistParser.DeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx:NetlistParser.InitDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#initDeclarator.
    def visitInitDeclarator(self, ctx:NetlistParser.InitDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx:NetlistParser.StorageClassSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:NetlistParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx:NetlistParser.StructOrUnionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structOrUnion.
    def visitStructOrUnion(self, ctx:NetlistParser.StructOrUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structDeclarationList.
    def visitStructDeclarationList(self, ctx:NetlistParser.StructDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structDeclaration.
    def visitStructDeclaration(self, ctx:NetlistParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx:NetlistParser.SpecifierQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx:NetlistParser.StructDeclaratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#structDeclarator.
    def visitStructDeclarator(self, ctx:NetlistParser.StructDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx:NetlistParser.EnumSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#enumeratorList.
    def visitEnumeratorList(self, ctx:NetlistParser.EnumeratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#enumerator.
    def visitEnumerator(self, ctx:NetlistParser.EnumeratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#enumerationConstant.
    def visitEnumerationConstant(self, ctx:NetlistParser.EnumerationConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx:NetlistParser.AtomicTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#typeQualifier.
    def visitTypeQualifier(self, ctx:NetlistParser.TypeQualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx:NetlistParser.FunctionSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx:NetlistParser.AlignmentSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declarator.
    def visitDeclarator(self, ctx:NetlistParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#directDeclarator.
    def visitDirectDeclarator(self, ctx:NetlistParser.DirectDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#vcSpecificModifer.
    def visitVcSpecificModifer(self, ctx:NetlistParser.VcSpecificModiferContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx:NetlistParser.GccDeclaratorExtensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx:NetlistParser.GccAttributeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#gccAttributeList.
    def visitGccAttributeList(self, ctx:NetlistParser.GccAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#gccAttribute.
    def visitGccAttribute(self, ctx:NetlistParser.GccAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx:NetlistParser.NestedParenthesesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#pointer.
    def visitPointer(self, ctx:NetlistParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#typeQualifierList.
    def visitTypeQualifierList(self, ctx:NetlistParser.TypeQualifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameterTypeList.
    def visitParameterTypeList(self, ctx:NetlistParser.ParameterTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameterList.
    def visitParameterList(self, ctx:NetlistParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:NetlistParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#identifierList.
    def visitIdentifierList(self, ctx:NetlistParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#typeName.
    def visitTypeName(self, ctx:NetlistParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx:NetlistParser.AbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx:NetlistParser.DirectAbstractDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#typedefName.
    def visitTypedefName(self, ctx:NetlistParser.TypedefNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#initializer.
    def visitInitializer(self, ctx:NetlistParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#initializerList.
    def visitInitializerList(self, ctx:NetlistParser.InitializerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#designation.
    def visitDesignation(self, ctx:NetlistParser.DesignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#designatorList.
    def visitDesignatorList(self, ctx:NetlistParser.DesignatorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#designator.
    def visitDesignator(self, ctx:NetlistParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx:NetlistParser.StaticAssertDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#statement.
    def visitStatement(self, ctx:NetlistParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#labeledStatement.
    def visitLabeledStatement(self, ctx:NetlistParser.LabeledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#compoundStatement.
    def visitCompoundStatement(self, ctx:NetlistParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#blockItemList.
    def visitBlockItemList(self, ctx:NetlistParser.BlockItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#blockItem.
    def visitBlockItem(self, ctx:NetlistParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#expressionStatement.
    def visitExpressionStatement(self, ctx:NetlistParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#selectionStatement.
    def visitSelectionStatement(self, ctx:NetlistParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#iterationStatement.
    def visitIterationStatement(self, ctx:NetlistParser.IterationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#forCondition.
    def visitForCondition(self, ctx:NetlistParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#forDeclaration.
    def visitForDeclaration(self, ctx:NetlistParser.ForDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#forExpression.
    def visitForExpression(self, ctx:NetlistParser.ForExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#jumpStatement.
    def visitJumpStatement(self, ctx:NetlistParser.JumpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#compilationUnit.
    def visitCompilationUnit(self, ctx:NetlistParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#translationUnit.
    def visitTranslationUnit(self, ctx:NetlistParser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx:NetlistParser.ExternalDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:NetlistParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetlistParser#declarationList.
    def visitDeclarationList(self, ctx:NetlistParser.DeclarationListContext):
        return self.visitChildren(ctx)



del NetlistParser