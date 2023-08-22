grammar Netlist;
options {
	tokenVocab = JavaScriptLexer;
	superClass = JavaScriptLexerBase;
}
subckts: subckt+;

subckt: subcktHeader subcktBody subcktFooter;

subcktHeader: SUBCKT_HEADER SPECIAL_ID node* NEWLINE;
subcktBody: ('parameters' parameters)? components?;
subcktFooter: 'ends' SPECIAL_ID;
node: SPECIAL_ID;

parameters: parameter+ NEWLINE?;

parameter: SPECIAL_ID ('=' singleExpression)?;

components: component+;

component: SPECIAL_ID '(' node*? ')' SPECIAL_ID parameters?;

arguments: '(' (argument (',' argument)* ','?)? ')';

argument: singleExpression | Identifier;

singleExpression:
	singleExpression arguments												# ArgumentsExpression
	| singleExpression {this.notLineTerminator()}? '++'						# PostIncrementExpression
	| singleExpression {this.notLineTerminator()}? '--'						# PostDecreaseExpression
	| '++' singleExpression													# PreIncrementExpression
	| '--' singleExpression													# PreDecreaseExpression
	| '+' singleExpression													# UnaryPlusExpression
	| '-' singleExpression													# UnaryMinusExpression
	| '~' singleExpression													# BitNotExpression
	| '!' singleExpression													# NotExpression
	| <assoc = right> singleExpression '**' singleExpression				# PowerExpression
	| singleExpression ('*' | '/' | '%') singleExpression					# MultiplicativeExpression
	| singleExpression ('+' | '-') singleExpression							# AdditiveExpression
	| singleExpression '??' singleExpression								# CoalesceExpression
	| singleExpression ('<<' | '>>' | '>>>') singleExpression				# BitShiftExpression
	| singleExpression ('<' | '>' | '<=' | '>=') singleExpression			# RelationalExpression
	| singleExpression ('==' | '!=') singleExpression						# EqualityExpression
	| singleExpression '&' singleExpression									# BitAndExpression
	| singleExpression '^' singleExpression									# BitXOrExpression
	| singleExpression '|' singleExpression									# BitOrExpression
	| singleExpression '&&' singleExpression								# LogicalAndExpression
	| singleExpression '||' singleExpression								# LogicalOrExpression
	| singleExpression '?' singleExpression ':' singleExpression			# TernaryExpression
	| <assoc = right> singleExpression '=' singleExpression					# AssignmentExpression
	| <assoc = right> singleExpression assignmentOperator singleExpression	#
		AssignmentOperatorExpression
	| number					# LiteralExpression
	| SPECIAL_ID				# IdentifierExpression
	| '(' singleExpression ')'	# ParenthesizedExpression;

assignmentOperator:
	'*='
	| '/='
	| '%='
	| '+='
	| '-='
	| '<<='
	| '>>='
	| '>>>='
	| '&='
	| '^='
	| '|='
	| '**=';

number: pureNumber UNIT?;

pureNumber: INTEGER | FLOAT | SCIENTIFIC;

SUBCKT_HEADER: 'subckt';

SCIENTIFIC: (INTEGER | FLOAT) 'e' '-'? INTEGER;

FLOAT:
	INTEGER? '.' INTEGER ('e' '-'? INTEGER)?
	| INTEGER '.' ('e' '-'? INTEGER)?;

INTEGER: [0-9]+;

UNIT: [npumkfM];
SPECIAL_ID: (ID ('<' [0-9]+ '>')?) | (ID ('\\-' ID)+);
ID: [a-zA-Z_][a-zA-Z0-9_]*;

NEWLINE: '\r'? '\n';
COMMENT: '//' ~('\n' | '\r')* ('\n' | '\r' ('\n')?)? -> skip;

LINE_CONTINUATION: '\\' ('\n' | '\r' ('\n')?) -> skip; // 跳过行连接符
WS: [ \t\r\n]+ -> skip; // 跳过空格