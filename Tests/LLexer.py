import sys
from LToken import LToken


class LLexer:


    def __init__(self):
        #Regex patterns for reference, probably wont need them.
        self.INT_PATTERN = "[0-9]+"
        self.ID_PATTERN = "[A-Za-z]+"
        self.END_PATTERN = "end"
        self.PRINT_PATTERN = "print"



    def get_next_token(self):

        """Read single characters from stdin and return token based on specifications."""


        character = sys.stdin.read(1)


        # Handle whitespace.
        while character and character.isspace():
            character = sys.stdin.read(1)

            if not character:
                return None
        

        #If character is a number.
        if character.isdigit():
            lexeme = character

            while True:
                next_character = sys.stdin.read(1)

                if not next_character or not next_character.isdigit():
                    break
                lexeme += next_character

            return LToken(lexeme, LToken.INT)
        
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
            


        #Check for operators and special characters.
        

        #If input is incorrect, return error token.
        return self.error()



    def error(self):
        return LToken("ERROR", LToken.ERROR)
