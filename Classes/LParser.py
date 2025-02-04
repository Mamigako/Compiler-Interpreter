import sys
import LToken
import LLexer

class LParser:


    def __init__(self):
        self.curr_token = LToken()
        self.lexer = LLexer()

    def parse(self): 
        self.next_token() 
        self.statements() 
 
    def next_token(self): 
        self.curr_token = self.lexer.get_next_token() 
        if self.curr_token == LToken.ERROR:  # lexical error 
            self.error()

    def statements(self):
        pass

    def error(self):
        print("Syntax error.")
        sys.exit()