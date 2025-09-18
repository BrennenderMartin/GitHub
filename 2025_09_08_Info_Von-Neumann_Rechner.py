
class ALU:
    """
    selten auch Zentraleinheit oder Prozessor genannt,
    führt Rechenoperationen und boolesche Verknüpfungen aus.
    (Die Begriffe Zentraleinheit und Prozessor werden im Allgemeinen
    in anderer Bedeutung verwendet.)
    """
    def __init__(self):
        self.registers = {}
    
    def set(self, name, value):
        self.registers[name] = value
    
    
    def add(self, num1_name, num2_name):
        self.registers["R"] = int(self.registers[num1_name]) + int(self.registers[num2_name])
    
    def mtp(self, num1_name, num2_name):
        self.registers["R"] = int(self.registers[num1_name]) * int(self.registers[num2_name])
    
    def sub(self, num1_name, num2_name):
        self.registers["R"] = int(self.registers[num1_name]) - int(self.registers[num2_name])
    
    def div(self, num1_name, num2_name):
        self.registers["R"] = int(self.registers[num1_name]) / int(self.registers[num2_name])
    
    
    def get(self, name):
        return self.registers[name]
    
    
    def check_method(self, name):
        if   name == "ADD": return "ADD"
        elif name == "MTP" : return "MTP"
        elif name == "SUB": return "SUB"
        elif name == "DIV": return "DIV"
        else: raise Exception("Error: method unknown; Valid Methods: ADD, MTP, SUB, DIV")
    
    def edit_string(self, string):
        return_string = ""
        for i in range(len(string)):
            if string[i] == "_": return_string += " "
            elif string[i] == ";": return_string += ","
            else: return_string += string[i]
        return return_string
    
    def split(self, by, content):
        value1 = ""
        value2 = ""
        got = False
        for i in range(len(content)):
            if content[i] == by: got = True
            else:
                if got: value2 += content[i]
                else: value1 += content[i]
        return value1, value2

class ControlUnit:
    """
    interpretiert die Anweisungen eines Programms und
    verschaltet dementsprechend Datenquelle, -senke und
    notwendige ALU-Komponenten; das Steuerwerk regelt auch
    die Befehlsabfolge.
    """
    def __init__(self):
        self.bus = BUS()
    
    def run_program(self):
        for i in range(self.bus.get_length_program()):
            line = self.bus.get_next_line_program(i)
            command, values = self.bus.alu_split(" ", line)
            self.logic_handler(command, values.strip())
    
    def logic_handler(self, command, values):
        match command:
            case "SET":
                self.bus.set_memory(int(values), self.bus.get_input())
            
            case "SFR":
                name, index = self.bus.alu_split(",", values)
                self.bus.set_memory(int(index), self.bus.get_registers(name))
            
            case "STORE":
                index, value = self.bus.alu_split(",", values)
                self.bus.set_memory(int(index), value)
            
            case "LOAD":
                name, value = self.bus.alu_split(",", values)
                self.bus.set_registers(name, self.bus.get_data_memory(int(value)))
            
            case "RUN":
                name, num1_name, num2_name = values.split(",")
                string = num1_name + "," + num2_name
                self.logic_handler(self.bus.alu_check_method(int(name)), string)
            
            case "CHECK":
                self.bus.alu_check_method(int(values))
            
            case "ADD":
                num1_name, num2_name = self.bus.alu_split(",", values)
                self.bus.alu_add(num1_name, num2_name)
            
            case "MTP":
                num1_name, num2_name = self.bus.alu_split(",", values)
                self.bus.alu_mtp(num1_name, num2_name)
            
            case "SUB":
                num1_name, num2_name = self.bus.alu_split(",", values)
                self.bus.alu_sub(num1_name, num2_name)
            
            case "DIV":
                num1_name, num2_name = self.bus.alu_split(",", values)
                self.bus.alu_div(num1_name, num2_name)
            
            case "OUTPUT":
                output = self.bus.get_data_memory(int(values))
                if type(output) is str: self.bus.output(self.bus.alu_edit_string(output))
                elif type(output) is int: self.bus.output(output)
                elif type(output) is float: self.bus.output(round(output, 3))
                else: print(f"Invalid outputting type ({type(output)})! (neither str nor int nor float)")

class BUS:
    """
    dient zur Kommunikation zwischen
    den einzelnen Komponenten (Steuerbus, Adressbus, Datenbus)
    """
    def __init__(self):
        self.alu = ALU()
        self.memory = Memory()
        self.iounit = IOUnit()
    
    def set_memory(self, position, value):
        self.memory.set(position, value)
    
    def set_registers(self, name, value):
        self.alu.set(name, value)
    
    
    def output(self, output):
        self.iounit.output(output)
    
    
    def get_next_line_program(self, line):
        return self.memory.get_line_program(line)
    
    def get_length_program(self):
        return self.memory.get_length_program()
    
    def get_data_memory(self, index):
        return self.memory.get(index)
    
    def get_input(self):
        return self.iounit.inputs()
    
    def get_registers(self, name):
        return self.alu.get(name)
    
    
    def alu_add(self, num1_name, num2_name):
        return self.alu.add(num1_name, num2_name)
    
    def alu_mtp(self, num1_name, num2_name):
        return self.alu.mtp(num1_name, num2_name)
    
    def alu_sub(self, num1_name, num2_name):
        return self.alu.sub(num1_name, num2_name)
    
    def alu_div(self, num1_name, num2_name):
        return self.alu.div(num1_name, num2_name)
    
    def alu_check_method(self, name):
        return self.alu.check_method(self.get_data_memory(name))
    
    def alu_edit_string(self, string):
        return self.alu.edit_string(string)
    
    def alu_split(self, by, content):
        return self.alu.split(by, content)

class Memory:
    """
    speichert sowohl Programme als auch Daten,
    welche für das Rechenwerk zugänglich sind.
    """
    def __init__(self):
        self.memory = {
            "data": {},
            "program": [
                "STORE 4,Enter_a_method;_that_shall_be_executed(Valid_names:_ADD;_MTP;_SUB;_DIV)", #Store to Memory
                "OUTPUT 4", # Gives the IOUnit data[i] to print it
                "SET 0", # Sets data[i] as gotten input
                "CHECK 0",
                
                "STORE 5,Enter_an_integer;_that_shall_be_used",
                "OUTPUT 5",
                "SET 1",
                "OUTPUT 5",
                "SET 2",
                
                "LOAD A,1", # Sets ALU.registers{"A": data[1]}
                "LOAD B,2", # Sets ALU.registers{"B": data[2]}
                
                "RUN 0,A,B", # runs given method(saved in mem[0]) with ALU.registers{"A"} and ALU.registers{"B"}
                
                "SFR R,3", # Gets output from ALU and stores it in data[3] (Store from Registers)
                "OUTPUT 3"
            ]
        }
    
    def set(self, position, value):
        self.memory["data"][position] = value
    
    def get(self, index):
        return self.memory["data"][index]
    
    def get_line_program(self, line: int):
        return self.memory["program"][line]
    
    def get_length_program(self):
        return len(self.memory["program"])

class IOUnit:
    """
    steuert die Ein- und Ausgabe von Daten,
    zum Anwender (Tastatur, Bildschirm) oder
    zu anderen Systemen (Schnittstellen).
    """
    def output(self, output):
        print(output, end="")
    
    def inputs(self):
        return input(": ")

controlunit = ControlUnit()
controlunit.run_program()