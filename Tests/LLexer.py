import sys
from LToken import LToken


class LLexer:

    

    def __init__(self):
        #Regex patterns for reference, probably wont need them.
        self.INT_PATTERN = "[0-9]+"
        self.ID_PATTERN = "[A-Za-z]+"
        self.END_PATTERN = "end"
        self.PRINT_PATTERN = "print"
        self.next_operator = None
        self.current_token = None



    def get_next_token(self):

        if self.next_operator is None:
            character = sys.stdin.read(1)
        else:
            # If the next_operator is a whitespace, ignore it and get the next token.
            if self.next_operator.isspace():
                self.next_operator = None
                return self.get_next_token()

            if self.next_operator == "=":
                self.current_token = LToken("=", LToken.ASSIGN)
            elif self.next_operator == ";":
                self.current_token = LToken(";", LToken.SEMICOL)
            elif self.next_operator == "+":
                self.current_token = LToken("+", LToken.PLUS)
            elif self.next_operator == "-":
                self.current_token = LToken("-", LToken.MINUS)
            elif self.next_operator == "*":
                self.current_token = LToken("*", LToken.MULT) 
            elif self.next_operator == "(":
                self.current_token = LToken("(", LToken.LPAREN)
            elif self.next_operator == ")":
                self.current_token = LToken(")", LToken.RPAREN)
        
            self.next_operator = None
            return self.current_token

        # Handle whitespace.
        while character and character.isspace():
            character = sys.stdin.read(1)
            if not character:
                return


        #If character is a number.
        if character.isdigit():
            lexeme = character

            while True:
                next_character = sys.stdin.read(1)
                
                if not next_character.isdigit():
                    self.next_operator = next_character
                    return LToken(lexeme, LToken.INT)
                else:
                    lexeme += next_character

        #Check for operators and special characters.
        if character == "=":
            return LToken(character, LToken.ASSIGN)
        elif character == ";":
            return LToken(character, LToken.SEMICOL)
        elif character == "+":
            return LToken(character, LToken.PLUS)
        elif character == "-":
            return LToken(character, LToken.MINUS)
        elif character == "*":
            return LToken(character, LToken.MULT) 
        elif character == "(":
            return LToken(character, LToken.LPAREN)
        elif character == ")":
            return LToken(character, LToken.RPAREN)

        #If character is a letter or special symbol.
        if character.isalpha():
            lexeme = character

            while True:
                next_character = sys.stdin.read(1)
            
                if not next_character or not next_character.isalpha():
                    break

                lexeme += next_character
            

            #Check for "print" and "end".
            if lexeme == "print":
                return LToken(lexeme, LToken.PRINT)
            elif lexeme == "end":
                return LToken(lexeme, LToken.END)
            else:
                return LToken(lexeme, LToken.ID)
            

        #If input is incorrect, return error token.
        return self.error()


    def error(self):
        return LToken("ERROR", LToken.ERROR)
