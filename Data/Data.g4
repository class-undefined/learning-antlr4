grammar Data;

data: group+;

group: INT sequence[$INT.int];

sequence[int n]
	locals[int i = 1;]: ({$i<=$n}? INT {$i+=1;})*; // match n integers

INT: [0-9]+; // match integers
WS: [ \t\n\r]+ -> skip; // toss out all whitespace