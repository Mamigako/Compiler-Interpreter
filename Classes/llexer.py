import sys
from ltoken import LToken


class LLexer:
    """
    This class tokenizes input from language L.
    """
    def __init__(self):
        self.next_operator = None # Used when there are no spaces between tokens
        self.current_token = None


    def get_next_token(self):

        if self.next_operator is None:
            character = sys.stdin.read(1)

            if character == "": 
                return LToken("", LToken.ERROR) 

        else:
            # Handle case where we already detected an operator in the previous iteration
            if self.next_operator.isspace():
                self.next_operator = None
                return self.get_next_token()

            character = self.next_operator
            self.next_operator = None


        # To handle whitespace
        while character.isspace():
            character = sys.stdin.read(1)

            if character == "":  
                return LToken("", LToken.ERROR)


        if character.isdigit():
            lexeme = character

            while True:
                next_character = sys.stdin.read(1)

                if not next_character.isdigit():
                    self.next_operator = next_character  # Store for next iteration
                    return LToken(lexeme, LToken.INT)
                
                lexeme += next_character


        # If character is a letter (ID, PRINT, END)
        if character.isalpha():
            lexeme = character

            while True:
                next_character = sys.stdin.read(1)

                if not next_character.isalpha():
                    self.next_operator = next_character  # Store for next iteration
                    break

                lexeme += next_character

            if lexeme == "print":
                return LToken(lexeme, LToken.PRINT)
            
            elif lexeme == "end":
                return LToken(lexeme, LToken.END)
            
            else:
                return LToken(lexeme, LToken.ID)

        # To check for single-character tokens
        token_map = {
            "=": LToken.ASSIGN,
            ";": LToken.SEMICOL,
            "+": LToken.PLUS,
            "-": LToken.MINUS,
            "*": LToken.MULT,
            "(": LToken.LPAREN,
            ")": LToken.RPAREN
        }

        if character in token_map:
            return LToken(character, token_map[character])

        
        return self.error(character)


    def error(self, character):
        return LToken(f"{character}", LToken.ERROR)
