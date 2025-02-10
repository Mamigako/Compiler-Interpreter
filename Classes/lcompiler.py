from llexer import LLexer
from lparser import LParser

if __name__ == "__main__":
    """
    This class compiles language L to language S.
    """
    lexer = LLexer()
    parser = LParser(lexer)
    parser.parse()
