import sys,argparse,importlib
from common import readfile,log





class lmc:
    def __init__(self):
        self.memory = []
        self.memsize = 100
        self.posflag = False
        self.accumulator = 0
        self.pc = 0 # initialize the program counter to 0
        for i in range(0,self.memsize):
            self.memory.append("000")

    def load_program(self,filename):
        lines = readfile(filename)
        counter = 0
        for line in lines:
            self.memory[counter] = line.strip()
            print(line.strip())
            counter = counter + 1

    def print_memory(self):
        print(self.memory)

        
    #1xx ADD
    #2xx SUB
    #3xx LDA
    #5xx STA
    #6xx BRA
    #7xx BRZ
    #8xx BRP
    
    def execute_complex_inst(self,inst):
        opcode = int(inst[0])
        mem_loc = int(inst[1:])
        log("opcode is " + str(opcode))
        if opcode == 1:
           self.accumulator = int(self.accumulator) + int(self.memory[mem_loc])
        elif opcode == 2:
           self.accumulator = self.accumulator - self.memory[mem_loc]
        elif opcode == 3:
           self.accumulator = int(self.memory[mem_loc])
        elif opcode == 5:
           self.memory[mem_loc] = self.accumulator
        elif opcode == 6:
           self.pc = mem_loc
        elif opcode == 7:
           if self.accumulator == 0:
               self.pc = mem_loc
           else:
               #do nothing
               pass
        elif opcode == 8:
            if self.accumulator >= 0:
                self.pc = mem_loc
            else:
                #do nothing
                pass
                
    def execute_instruction(self,inst):
        if inst in "901":
            self.accumulator = input("input:")
        elif inst in "902" :
            print(self.accumulator)
        elif inst in "000" :
            sys.exit()

        else:
            self.execute_complex_inst(inst)
    
    def run(self):
        #Fetch the instruction from the current location
        while self.pc != 100:
            inst = self.memory[self.pc]
            self.pc = self.pc + 1
            self.execute_instruction(inst)
            log("pc is now " + str(self.pc))

def mainstub():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    mylmc = lmc()
    mylmc.load_program(args.filename)
    mylmc.print_memory()
    mylmc.run()

mainstub()

   
