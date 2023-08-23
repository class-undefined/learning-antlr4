lexer grammar NetlistLexer;
Subckt: 'subckt';
ENDS: 'ends';
Parameters: 'parameters';
Assign: '=';
OpenParen: '(';
CloseParen: ')';
Comma: ',';
QuestionMark: '?';
QuestionMarkDot: '?.';
Colon: ':';
Ellipsis: '...';
Dot: '.';
PlusPlus: '++';
MinusMinus: '--';
Plus: '+';
Minus: '-';
BitNot: '~';
Not: '!';
Multiply: '*';
Divide: '/';
Modulus: '%';
Power: '**';
NullCoalesce: '??';
Hashtag: '#';
RightShiftArithmetic: '>>';
LeftShiftArithmetic: '<<';
RightShiftLogical: '>>>';
LessThan: '<';
MoreThan: '>';
LessThanEquals: '<=';
GreaterThanEquals: '>=';
Equals_: '==';
NotEquals: '!=';
IdentityEquals: '===';
IdentityNotEquals: '!==';
BitAnd: '&';
BitXOr: '^';
BitOr: '|';
And: '&&';
Or: '||';
MultiplyAssign: '*=';
DivideAssign: '/=';
ModulusAssign: '%=';
PlusAssign: '+=';
MinusAssign: '-=';
LeftShiftArithmeticAssign: '<<=';
RightShiftArithmeticAssign: '>>=';
RightShiftLogicalAssign: '>>>=';
BitAndAssign: '&=';
BitXorAssign: '^=';
BitOrAssign: '|=';
PowerAssign: '**=';
ARROW: '=>';

StringLiteral: '"' SCharSequence? '"';

fragment SCharSequence: SChar+;

fragment SChar:
	~["\\\r\n]
	| '\\\n' // Added line
	| '\\\r\n'; // Added line

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