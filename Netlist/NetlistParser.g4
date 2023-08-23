parser grammar NetlistParser;
options {
	tokenVocab = NetlistLexer;
}
subckts: subckt+;

subckt: subcktHeader subcktBody subcktFooter;

subcktHeader: Subckt SPECIAL_ID node* NEWLINE;
subcktBody: (Parameters parameters)? components?;
subcktFooter: ENDS SPECIAL_ID;
node: SPECIAL_ID;

parameters: parameter+ NEWLINE?;

parameter: SPECIAL_ID (Assign singleExpression)?;

components: component+;

component:
	SPECIAL_ID OpenParen node*? CloseParen SPECIAL_ID parameters?;

arguments:
	OpenParen (argument (Comma argument)* Comma?)? CloseParen;

argument: singleExpression;

singleExpression:
	singleExpression arguments											# ArgumentsExpression
	| singleExpression {this.notLineTerminator()}? PlusPlus				# PostIncrementExpression
	| singleExpression {this.notLineTerminator()}? MinusMinus			# PostDecreaseExpression
	| PlusPlus singleExpression											# PreIncrementExpression
	| MinusMinus singleExpression										# PreDecreaseExpression
	| Plus singleExpression												# UnaryPlusExpression
	| Minus singleExpression											# UnaryMinusExpression
	| BitNot singleExpression											# BitNotExpression
	| Not singleExpression												# NotExpression
	| <assoc = right> singleExpression Power singleExpression			# PowerExpression
	| singleExpression (Multiply | Divide | Modulus) singleExpression	# MultiplicativeExpression
	| singleExpression (Plus | Minus) singleExpression					# AdditiveExpression
	| singleExpression NullCoalesce singleExpression					# CoalesceExpression
	| singleExpression (
		LeftShiftArithmetic
		| RightShiftArithmetic
		| RightShiftLogical
	) singleExpression # BitShiftExpression
	| singleExpression (
		LessThan
		| MoreThan
		| LessThanEquals
		| GreaterThanEquals
	) singleExpression														# RelationalExpression
	| singleExpression (Equals_ | NotEquals) singleExpression				# EqualityExpression
	| singleExpression BitAnd singleExpression								# BitAndExpression
	| singleExpression BitXOr singleExpression								# BitXOrExpression
	| singleExpression BitOr singleExpression								# BitOrExpression
	| singleExpression And singleExpression									# LogicalAndExpression
	| singleExpression Or singleExpression									# LogicalOrExpression
	| singleExpression QuestionMark singleExpression Colon singleExpression	# TernaryExpression
	| <assoc = right> singleExpression Assign singleExpression				# AssignmentExpression
	| <assoc = right> singleExpression assignmentOperator singleExpression	#
		AssignmentOperatorExpression
	| number								# LiteralExpression
	| SPECIAL_ID							# IdentifierExpression
	| OpenParen singleExpression CloseParen	# ParenthesizedExpression;

assignmentOperator:
	MultiplyAssign
	| DivideAssign
	| ModulusAssign
	| PlusAssign
	| MinusAssign
	| LeftShiftArithmeticAssign
	| RightShiftArithmeticAssign
	| RightShiftLogicalAssign
	| BitAndAssign
	| BitXorAssign
	| BitOrAssign
	| PowerAssign;

number: pureNumber UNIT?;
string: StringLiteral;
pureNumber: INTEGER | FLOAT | SCIENTIFIC;
