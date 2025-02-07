from LLexer import LLexer
from LParser import LParser

if __name__ == "__main__":
    lexer = LLexer()
    parser = LParser(lexer)
    parser.parse()