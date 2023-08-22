import sys
from antlr4 import *
from DataLexer import DataLexer
from DataParser import DataParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DataLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DataParser(stream)
    tree = parser.data()
    print(tree.toStringTree(recog=parser))
 
if __name__ == '__main__':
    main(sys.argv)