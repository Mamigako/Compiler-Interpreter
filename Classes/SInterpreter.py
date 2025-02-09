import sys


class SInterpreter:
    def __init__(self):
        self.stack = []
        self.values = {}


    def cycle(self):
        #performs the fetch-decode-execute cycle
        while True:
            next_line = self.fetch()

            if not next_line:  # Stop if input is empty
                break

            command = self.decode(next_line)

            self.execute(command)


    def fetch(self):
        next_line = sys.stdin.readline().strip()
        return next_line
    

    def decode(self, next_line : str):
        return next_line.strip().split(" ")



    def execute(self, command):
        operation = command[0]

        match operation:
            case "PUSH":
                if len(command) != 2:
                    sys.stdout.write(f"Syntax Error at {operation}")
                    sys.exit(1)

                variable = command[1]

                if variable.isdigit():
                    variable = int(variable)
                    self.stack.append(variable)

                elif variable.isalpha():
                    self.stack.append(variable)
                    if variable not in self.values.keys():
                        self.values[variable] = 0

                return
            

            case "ADD":
                first_num = self.stack.pop()
                second_num = self.stack.pop()

                if not (type(first_num) == int): 
                    first_num = self.values[first_num]

                if not (type(second_num) == int): 
                    second_num = self.values[second_num]

                result = first_num + second_num
                self.stack.append(result)
                return
            

            case "MULT":
                first_num = self.stack.pop()
                second_num = self.stack.pop()

                if not (type(first_num) == int): 
                    first_num = self.values[first_num]

                if not (type(second_num) == int): 
                    second_num = self.values[second_num]

                result = first_num * second_num
                self.stack.append(result)
                return


            case "UMINUS":
                last_number = self.stack.pop()

                if not (type(last_number) == int):
                    last_number = self.values[last_number]

                self.stack.append(-last_number)
                return
            

            case "ASSIGN":
                value = self.stack.pop()

                if not (type(value) == int):
                    value = self.values[value]

                variable = self.stack.pop()
                self.values[variable] = value
                return
            

            case "PRINT":
                last_element = self.stack.pop()
                sys.stdout.write(f"{self.values[last_element]}")
                return
            
            case "Syntax":
                sys.stdout.write("Syntax Error")
                sys.exit(1)




if __name__ == "__main__":
    interpreter = SInterpreter() 
    interpreter.cycle()