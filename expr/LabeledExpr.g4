grammar LabeledExpr;

import CommonLexerRules;
// 小写开头的是解析规则 它们描述了如何从tokens组合并匹配语言的更高级结构。 
// 大写开头的是词法规则 它们用于匹配输入文本中的具体字符序列。生成的tokens由这些规则定义，它们在解析过程中作为输入的原子单位。
stat:
	expr NEWLINE			# printExpr
	| ID '=' expr NEWLINE	# assign
	| NEWLINE				# blank;
expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| INT							# int
	| ID							# id
	| '(' expr ')'					# parens;

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';