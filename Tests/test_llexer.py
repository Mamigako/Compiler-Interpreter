from LToken import LToken
from LLexer import LLexer

if __name__ == "__main__":
    lexer = LLexer()
    curr_token = LToken("",LToken.ERROR)

    while curr_token.token_code != LToken.END:
        curr_token = lexer.get_next_token()
        print(curr_token.lexeme)
