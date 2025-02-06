import sys
from LToken import LToken
from LLexer import LLexer

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
        
        if self.curr_token == LToken.END:
            return
        
        else:
            self.statement()

            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()

    def statement(self):
        self.next_token()
        if self.curr_token.token_code == LToken.ID:
            self.next_token()
            if self.curr_token.token_code == LToken.ASSIGN:
                self.expr()
            else:
                self.error()

        elif self.curr_token.token_code == LToken.PRINT:
            self.next_token()
            if self.curr_token.token_code == LToken.ID:
                sys.stdout.write(f"PUSH {self.curr_token.lexeme}");
                sys.stdout.write("PRINT");
                return

            else:
                self.error()

    def expr(self):
        pass

    def term(self):
        pass

    def factor(self):
        pass

    def error(self):
        print("Syntax error.")
        sys.exit()
