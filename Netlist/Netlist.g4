grammar Netlist;
options {
	tokenVocab = JavaScriptLexer;
	superClass = JavaScriptLexerBase;
}

subckt: SUBCKT_HEADER ID node+ NEWLINE parameters?;

node: ID ('<' INTEGER '>')?;

parameters: ('parameters' parameter+);

parameter: ID ('=' singleExpression)?;

arguments: '(' (argument (',' argument)* ','?)? ')';

argument: Ellipsis? (singleExpression | Identifier);

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
	| singleExpression ('==' | '!=' | '===' | '!==') singleExpression		# EqualityExpression
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
	| identifier				# IdentifierExpression
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

identifier: ID;
SUBCKT_HEADER: 'subckt';

SCIENTIFIC: (INTEGER | FLOAT) 'e' '-'? INTEGER;

FLOAT:
	INTEGER? '.' INTEGER ('e' '-'? INTEGER)?
	| INTEGER '.' ('e' '-'? INTEGER)?;

INTEGER: [0-9]+;

UNIT: [npumkfM];
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NEWLINE: '\r'? '\n';
COMMENT: '//' ~('\n' | '\r')* ('\n' | '\r' ('\n')?)? -> skip;

LINE_CONTINUATION: '\\' ('\n' | '\r' ('\n')?) -> skip; // 跳过行连接符
WS: [ \t\r\n]+ -> skip; // 跳过空格