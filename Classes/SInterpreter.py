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
        next_line = sys.stdin.readline()
        return next_line
    

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
                first_num = self.stack.pop()
                second_num = self.stack.pop()
                result = first_num + second_num
                self.stack.append(result)
                return
            
            case "MULT":
                first_num = self.stack.pop()
                second_num = self.stack.pop()
                result = first_num * second_num
                self.stack.append(result)
                return

            case "UMINUS":
                #self.stack[len(self.stack) - 1] = - self.stack[len(self.stack) - 1]
                last_number = self.stack.pop()
                self.stack.append(-last_number)
                return
            
            case "ASSIGN":
                value = self.stack.pop()
                variable = self.stack.pop()
                self.values[variable] = value
                return
            
            case "PRINT":
                last_element = self.stack.pop()
                sys.stdout.write(f"{last_element}")
                return




if __name__ == "__main__":
    interpreter = SInterpreter() 
    interpreter.cycle()