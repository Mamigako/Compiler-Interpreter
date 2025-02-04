import sys

class LLexer:

    def __init__(self):
        self.INT_PATTERN = "[0-9]+"
        self.ID_PATTERN = "[A-Za-z]+"
        self.END_PATTERN = "end"
        self.PRINT_PATTERN = "print"

    def get_next_token(self):
        sys.stdin.read(1)

    def error(self):
        return ERROR_TOKEN