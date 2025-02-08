import sys
from LToken import LToken
from LLexer import LLexer

class LParser:


    def __init__(self, lexer):
        self.curr_token = None
        self.lexer = lexer

    def parse(self): 
        self.next_token() 
        self.statements() 
        sys.stdout.write("\n")
 
    def next_token(self): 
        self.curr_token = self.lexer.get_next_token() 
        if self.curr_token is None:
            return
        if self.curr_token.token_code == LToken.ERROR:  # lexical error 
            self.error()

    def statements(self):


        #Statements -> Statement ; Statements | end 
        #Statement -> id = Expr | print id 
        #Expr- > Term | Term + Expr  
        #Term -> Factor | Factor * Term 
        #Factor -> int | id | - Factor | ( Expr ) 

        # Production: Statements -> Statement ; Statements | end
        if self.curr_token.token_code == LToken.END:
            return
        
        else:
            self.statement() 
        
            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error() 

    def statement(self):

        if self.curr_token.token_code == LToken.PRINT:
            self.next_token()  
        
            if self.curr_token.token_code == LToken.ID:
                sys.stdout.write("PUSH " + self.curr_token.lexeme + "\n")
                self.next_token()  #TODO: Check if there was no semi-colon after the print
                sys.stdout.write("PRINT" + "\n")
            else:
                self.error()
        
        elif self.curr_token.token_code == LToken.ID:
            var_name = self.curr_token.lexeme
            sys.stdout.write("PUSH " + var_name + "\n")  
            self.next_token()  
        
            if self.curr_token.token_code == LToken.ASSIGN:
                self.next_token()  
                self.expr()       
                sys.stdout.write("ASSIGN" + "\n")   
            else:
                self.error()
        else:
            self.error()

    def expr(self):
        # Production: Expr -> Term | Term + Expr
        self.term()
        
        if self.curr_token is not None and self.curr_token.token_code == LToken.PLUS:
            self.next_token() 
            self.expr()      
            sys.stdout.write("ADD" + "\n")

    def term(self):
        # Production: Term -> Factor | Factor * Term
        self.factor()
        
        if self.curr_token is not None and self.curr_token.token_code == LToken.MULT:
            self.next_token()  
            self.term()      
            sys.stdout.write("MULT" + "\n")

    def factor(self):
        # Production: Factor -> int | id | - Factor | ( Expr )
        if self.curr_token.token_code == LToken.INT:
            sys.stdout.write("PUSH " + self.curr_token.lexeme + "\n")
            self.next_token()  
        
        elif self.curr_token.token_code == LToken.ID:
            sys.stdout.write("PUSH " + self.curr_token.lexeme + "\n")
            self.next_token()  
        
        elif self.curr_token.token_code == LToken.MINUS:
            self.next_token()  
            self.factor()
            sys.stdout.write("UMINUS" + "\n")
        
        elif self.curr_token.token_code == LToken.LPAREN:

            self.next_token()  
            self.expr()
            
            if self.curr_token.token_code == LToken.RPAREN:
                self.next_token()  
            else:
                self.error()
        else:
            self.error()

    def error(self):
        sys.stdout.write("Syntax error." + "\n")
        sys.exit()

