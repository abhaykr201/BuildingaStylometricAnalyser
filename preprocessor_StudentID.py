import pandas as pd

class Preprocessor:
    def __init__(self):
        self.token=[]

    def __str__(self):
        line =''

        for word in self.token:
            if(line != '\r\n'):
                line = line +" "+ word
            
        return line
        

    def tokenise(self, input_sequence):
        #self.token = input_sequence.split(' ')
        for i in input_sequence:
            d = list(i.split(' '))
            self.token = self.token + d

    def _tokenised_list(self):
        return self.token






