from Classes import LLexer
from Classes import LParser

if __name__ == "__main__":
    lexer = LLexer()
    parser = LParser(lexer)
    parser.parse()