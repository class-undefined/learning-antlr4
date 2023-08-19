import sys
from antlr4 import *
from ArrayLexer import ArrayLexer
from ArrayParser import ArrayParser
from ArrayVisitor import ArrayVisitor
from ArrayListener import ArrayListener
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ArrayLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArrayParser(stream)
    tree = parser.init()
    listener = ArrayListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree) 
    print()
    ArrayVisitor().visit(tree)
    print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)