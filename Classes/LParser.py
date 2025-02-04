import sys
import LToken
import LLexer

class LParser:


    def __init__(self):
        self.curr_token = None
        self.lexer = LLexer()

    def parse(self): 
        self.next_token() 
        self.statements() 
 
    def next_token(self): 
        self.curr_token = self.lexer.get_next_token() 
        if self.curr_token is None:
            return
        if self.curr_token.token_code == LToken.ERROR:  # lexical error 
            self.error()

    def statements(self):
        pass

    def statement(self):
        pass

    def expr(self):
        pass

    def term(self):
        pass

    def factor(self):
        pass

    def error(self):
        print("Syntax error.")
        sys.exit()