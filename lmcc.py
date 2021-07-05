# LMC compiler

from common import log,readfile
import sys




class LMParser:
    
    def __init__(self,contents):
        self.memory = []
        self.tokenized = []
        self.token_map = { }
        self.program = contents

        self.keywords = ["ADD","SUB","LDA","STA","BRA","BRZ","BRP","INP","OUT","HLT","DAT"]
        #TODO we need to handle DAT
        self.opcode_map = {
            "ADD" : "1" ,
            "SUB" : "2" ,
            "LDA" : "3" ,
            "STA" : "5" ,
            "BRA" : "6" ,
            "BRZ" : "7" ,
            "BRP" : "8" ,
            "INP" : "901" ,
            "OUT" : "902" ,
            "HLT" : "000"
            }
    

    def tokenize(self):
        for line in self.program:
            line = line.strip()
            val = line.split()
            print(val)

    def error(self,msg):
        #something serious happened , lets quit with a message
        print(msg)
        sys.exit()

    def lexical_analysis(self):
        pass

    def expand_labels(self):
        for

    def generate_code(self):
        pass


def mainstub():
    print("compile the .lma files")
    program = readfile("sample.lma")
    parser = LMParser(program)
    parser.tokenize()
    parser.expand_labels()
    parser.lexical_analysis()
    parser.generate_code()
    

mainstub()    

    
    
