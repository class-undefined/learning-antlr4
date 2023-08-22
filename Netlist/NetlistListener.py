# Generated from Netlist.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .NetlistParser import NetlistParser
else:
    from NetlistParser import NetlistParser

# This class defines a complete listener for a parse tree produced by NetlistParser.
class NetlistListener(ParseTreeListener):

    # Enter a parse tree produced by NetlistParser#subckt.
    def enterSubckt(self, ctx:NetlistParser.SubcktContext):
        pass

    # Exit a parse tree produced by NetlistParser#subckt.
    def exitSubckt(self, ctx:NetlistParser.SubcktContext):
        pass


    # Enter a parse tree produced by NetlistParser#node.
    def enterNode(self, ctx:NetlistParser.NodeContext):
        pass

    # Exit a parse tree produced by NetlistParser#node.
    def exitNode(self, ctx:NetlistParser.NodeContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameter.
    def enterParameter(self, ctx:NetlistParser.ParameterContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameter.
    def exitParameter(self, ctx:NetlistParser.ParameterContext):
        pass


    # Enter a parse tree produced by NetlistParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:NetlistParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:NetlistParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#genericSelection.
    def enterGenericSelection(self, ctx:NetlistParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by NetlistParser#genericSelection.
    def exitGenericSelection(self, ctx:NetlistParser.GenericSelectionContext):
        pass


    # Enter a parse tree produced by NetlistParser#genericAssocList.
    def enterGenericAssocList(self, ctx:NetlistParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by NetlistParser#genericAssocList.
    def exitGenericAssocList(self, ctx:NetlistParser.GenericAssocListContext):
        pass


    # Enter a parse tree produced by NetlistParser#genericAssociation.
    def enterGenericAssociation(self, ctx:NetlistParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by NetlistParser#genericAssociation.
    def exitGenericAssociation(self, ctx:NetlistParser.GenericAssociationContext):
        pass


    # Enter a parse tree produced by NetlistParser#postfixExpression.
    def enterPostfixExpression(self, ctx:NetlistParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#postfixExpression.
    def exitPostfixExpression(self, ctx:NetlistParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:NetlistParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by NetlistParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:NetlistParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by NetlistParser#unaryExpression.
    def enterUnaryExpression(self, ctx:NetlistParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#unaryExpression.
    def exitUnaryExpression(self, ctx:NetlistParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#unaryOperator.
    def enterUnaryOperator(self, ctx:NetlistParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by NetlistParser#unaryOperator.
    def exitUnaryOperator(self, ctx:NetlistParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by NetlistParser#castExpression.
    def enterCastExpression(self, ctx:NetlistParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#castExpression.
    def exitCastExpression(self, ctx:NetlistParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:NetlistParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:NetlistParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#shiftExpression.
    def enterShiftExpression(self, ctx:NetlistParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#shiftExpression.
    def exitShiftExpression(self, ctx:NetlistParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#relationalExpression.
    def enterRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#relationalExpression.
    def exitRelationalExpression(self, ctx:NetlistParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#equalityExpression.
    def enterEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#equalityExpression.
    def exitEqualityExpression(self, ctx:NetlistParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#andExpression.
    def enterAndExpression(self, ctx:NetlistParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#andExpression.
    def exitAndExpression(self, ctx:NetlistParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:NetlistParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:NetlistParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:NetlistParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:NetlistParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:NetlistParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:NetlistParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:NetlistParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:NetlistParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:NetlistParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by NetlistParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:NetlistParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by NetlistParser#expression.
    def enterExpression(self, ctx:NetlistParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#expression.
    def exitExpression(self, ctx:NetlistParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#constantExpression.
    def enterConstantExpression(self, ctx:NetlistParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#constantExpression.
    def exitConstantExpression(self, ctx:NetlistParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#declaration.
    def enterDeclaration(self, ctx:NetlistParser.DeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#declaration.
    def exitDeclaration(self, ctx:NetlistParser.DeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:NetlistParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by NetlistParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:NetlistParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by NetlistParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:NetlistParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by NetlistParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:NetlistParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by NetlistParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:NetlistParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:NetlistParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:NetlistParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by NetlistParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:NetlistParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by NetlistParser#initDeclarator.
    def enterInitDeclarator(self, ctx:NetlistParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#initDeclarator.
    def exitInitDeclarator(self, ctx:NetlistParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:NetlistParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:NetlistParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:NetlistParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:NetlistParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:NetlistParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:NetlistParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#structOrUnion.
    def enterStructOrUnion(self, ctx:NetlistParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by NetlistParser#structOrUnion.
    def exitStructOrUnion(self, ctx:NetlistParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by NetlistParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:NetlistParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by NetlistParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:NetlistParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by NetlistParser#structDeclaration.
    def enterStructDeclaration(self, ctx:NetlistParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#structDeclaration.
    def exitStructDeclaration(self, ctx:NetlistParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:NetlistParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by NetlistParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:NetlistParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by NetlistParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:NetlistParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by NetlistParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:NetlistParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by NetlistParser#structDeclarator.
    def enterStructDeclarator(self, ctx:NetlistParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#structDeclarator.
    def exitStructDeclarator(self, ctx:NetlistParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:NetlistParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:NetlistParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#enumeratorList.
    def enterEnumeratorList(self, ctx:NetlistParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by NetlistParser#enumeratorList.
    def exitEnumeratorList(self, ctx:NetlistParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by NetlistParser#enumerator.
    def enterEnumerator(self, ctx:NetlistParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#enumerator.
    def exitEnumerator(self, ctx:NetlistParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:NetlistParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by NetlistParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:NetlistParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by NetlistParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:NetlistParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:NetlistParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#typeQualifier.
    def enterTypeQualifier(self, ctx:NetlistParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#typeQualifier.
    def exitTypeQualifier(self, ctx:NetlistParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:NetlistParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:NetlistParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:NetlistParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:NetlistParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#declarator.
    def enterDeclarator(self, ctx:NetlistParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#declarator.
    def exitDeclarator(self, ctx:NetlistParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:NetlistParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:NetlistParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#vcSpecificModifer.
    def enterVcSpecificModifer(self, ctx:NetlistParser.VcSpecificModiferContext):
        pass

    # Exit a parse tree produced by NetlistParser#vcSpecificModifer.
    def exitVcSpecificModifer(self, ctx:NetlistParser.VcSpecificModiferContext):
        pass


    # Enter a parse tree produced by NetlistParser#gccDeclaratorExtension.
    def enterGccDeclaratorExtension(self, ctx:NetlistParser.GccDeclaratorExtensionContext):
        pass

    # Exit a parse tree produced by NetlistParser#gccDeclaratorExtension.
    def exitGccDeclaratorExtension(self, ctx:NetlistParser.GccDeclaratorExtensionContext):
        pass


    # Enter a parse tree produced by NetlistParser#gccAttributeSpecifier.
    def enterGccAttributeSpecifier(self, ctx:NetlistParser.GccAttributeSpecifierContext):
        pass

    # Exit a parse tree produced by NetlistParser#gccAttributeSpecifier.
    def exitGccAttributeSpecifier(self, ctx:NetlistParser.GccAttributeSpecifierContext):
        pass


    # Enter a parse tree produced by NetlistParser#gccAttributeList.
    def enterGccAttributeList(self, ctx:NetlistParser.GccAttributeListContext):
        pass

    # Exit a parse tree produced by NetlistParser#gccAttributeList.
    def exitGccAttributeList(self, ctx:NetlistParser.GccAttributeListContext):
        pass


    # Enter a parse tree produced by NetlistParser#gccAttribute.
    def enterGccAttribute(self, ctx:NetlistParser.GccAttributeContext):
        pass

    # Exit a parse tree produced by NetlistParser#gccAttribute.
    def exitGccAttribute(self, ctx:NetlistParser.GccAttributeContext):
        pass


    # Enter a parse tree produced by NetlistParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:NetlistParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by NetlistParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:NetlistParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by NetlistParser#pointer.
    def enterPointer(self, ctx:NetlistParser.PointerContext):
        pass

    # Exit a parse tree produced by NetlistParser#pointer.
    def exitPointer(self, ctx:NetlistParser.PointerContext):
        pass


    # Enter a parse tree produced by NetlistParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:NetlistParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by NetlistParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:NetlistParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:NetlistParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:NetlistParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameterList.
    def enterParameterList(self, ctx:NetlistParser.ParameterListContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameterList.
    def exitParameterList(self, ctx:NetlistParser.ParameterListContext):
        pass


    # Enter a parse tree produced by NetlistParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:NetlistParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:NetlistParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#identifierList.
    def enterIdentifierList(self, ctx:NetlistParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by NetlistParser#identifierList.
    def exitIdentifierList(self, ctx:NetlistParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by NetlistParser#typeName.
    def enterTypeName(self, ctx:NetlistParser.TypeNameContext):
        pass

    # Exit a parse tree produced by NetlistParser#typeName.
    def exitTypeName(self, ctx:NetlistParser.TypeNameContext):
        pass


    # Enter a parse tree produced by NetlistParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:NetlistParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:NetlistParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:NetlistParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by NetlistParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:NetlistParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by NetlistParser#typedefName.
    def enterTypedefName(self, ctx:NetlistParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by NetlistParser#typedefName.
    def exitTypedefName(self, ctx:NetlistParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by NetlistParser#initializer.
    def enterInitializer(self, ctx:NetlistParser.InitializerContext):
        pass

    # Exit a parse tree produced by NetlistParser#initializer.
    def exitInitializer(self, ctx:NetlistParser.InitializerContext):
        pass


    # Enter a parse tree produced by NetlistParser#initializerList.
    def enterInitializerList(self, ctx:NetlistParser.InitializerListContext):
        pass

    # Exit a parse tree produced by NetlistParser#initializerList.
    def exitInitializerList(self, ctx:NetlistParser.InitializerListContext):
        pass


    # Enter a parse tree produced by NetlistParser#designation.
    def enterDesignation(self, ctx:NetlistParser.DesignationContext):
        pass

    # Exit a parse tree produced by NetlistParser#designation.
    def exitDesignation(self, ctx:NetlistParser.DesignationContext):
        pass


    # Enter a parse tree produced by NetlistParser#designatorList.
    def enterDesignatorList(self, ctx:NetlistParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by NetlistParser#designatorList.
    def exitDesignatorList(self, ctx:NetlistParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by NetlistParser#designator.
    def enterDesignator(self, ctx:NetlistParser.DesignatorContext):
        pass

    # Exit a parse tree produced by NetlistParser#designator.
    def exitDesignator(self, ctx:NetlistParser.DesignatorContext):
        pass


    # Enter a parse tree produced by NetlistParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:NetlistParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:NetlistParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#statement.
    def enterStatement(self, ctx:NetlistParser.StatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#statement.
    def exitStatement(self, ctx:NetlistParser.StatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#labeledStatement.
    def enterLabeledStatement(self, ctx:NetlistParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#labeledStatement.
    def exitLabeledStatement(self, ctx:NetlistParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#compoundStatement.
    def enterCompoundStatement(self, ctx:NetlistParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#compoundStatement.
    def exitCompoundStatement(self, ctx:NetlistParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#blockItemList.
    def enterBlockItemList(self, ctx:NetlistParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by NetlistParser#blockItemList.
    def exitBlockItemList(self, ctx:NetlistParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by NetlistParser#blockItem.
    def enterBlockItem(self, ctx:NetlistParser.BlockItemContext):
        pass

    # Exit a parse tree produced by NetlistParser#blockItem.
    def exitBlockItem(self, ctx:NetlistParser.BlockItemContext):
        pass


    # Enter a parse tree produced by NetlistParser#expressionStatement.
    def enterExpressionStatement(self, ctx:NetlistParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#expressionStatement.
    def exitExpressionStatement(self, ctx:NetlistParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#selectionStatement.
    def enterSelectionStatement(self, ctx:NetlistParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#selectionStatement.
    def exitSelectionStatement(self, ctx:NetlistParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#iterationStatement.
    def enterIterationStatement(self, ctx:NetlistParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#iterationStatement.
    def exitIterationStatement(self, ctx:NetlistParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#forCondition.
    def enterForCondition(self, ctx:NetlistParser.ForConditionContext):
        pass

    # Exit a parse tree produced by NetlistParser#forCondition.
    def exitForCondition(self, ctx:NetlistParser.ForConditionContext):
        pass


    # Enter a parse tree produced by NetlistParser#forDeclaration.
    def enterForDeclaration(self, ctx:NetlistParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#forDeclaration.
    def exitForDeclaration(self, ctx:NetlistParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#forExpression.
    def enterForExpression(self, ctx:NetlistParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by NetlistParser#forExpression.
    def exitForExpression(self, ctx:NetlistParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by NetlistParser#jumpStatement.
    def enterJumpStatement(self, ctx:NetlistParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by NetlistParser#jumpStatement.
    def exitJumpStatement(self, ctx:NetlistParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by NetlistParser#compilationUnit.
    def enterCompilationUnit(self, ctx:NetlistParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by NetlistParser#compilationUnit.
    def exitCompilationUnit(self, ctx:NetlistParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by NetlistParser#translationUnit.
    def enterTranslationUnit(self, ctx:NetlistParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by NetlistParser#translationUnit.
    def exitTranslationUnit(self, ctx:NetlistParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by NetlistParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:NetlistParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by NetlistParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:NetlistParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by NetlistParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:NetlistParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by NetlistParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:NetlistParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by NetlistParser#declarationList.
    def enterDeclarationList(self, ctx:NetlistParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by NetlistParser#declarationList.
    def exitDeclarationList(self, ctx:NetlistParser.DeclarationListContext):
        pass



del NetlistParser