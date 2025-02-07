import sys


class SInterpreter:


    def __init__(self):
        self.stack = []
        self.values = {}


    def cycle(self):
        #performs the fetch-decode-execute cycle

        next_line = self.fetch()

        operation = self.decode(next_line)

        self.execute(operation)


    def fetch(self):

        operation = sys.stdin.readline()
        return operation
    

    def decode(self, next_line):

        if "PUSH" in next_line:

            next_line = next_line[5:]

            if next_line.isdigit():
                next_line = int(next_line)
                self.stack.append(next_line)
                return "PUSH"
            
            elif next_line.isalpha():
                self.stack.append(next_line)
                self.values[next_line] = 0
                return "PUSH"
            
        else:
            return next_line



    def execute(self, operation):

        match operation:
            case "PUSH":
                return
            case "ADD":
                return
            case "MULT":
                return
            case "ASSIGN":
                return
            case "PRINT":
                return




if __name__ == "__main__":
    interpreter = SInterpreter() 
    interpreter.cycle()