import sys
from antlr4 import *
from NetlistLexer import NetlistLexer
from NetlistParser import NetlistParser
from NetlistVisitor import NetlistVisitor
from NetlistListener import NetlistListener
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = NetlistLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NetlistParser(stream)
    tree = parser.subckt()
    listener = NetlistListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree) 
    print()
    NetlistVisitor().visit(tree)
    print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)