import pandas as pd
import numpy as npe
import preprocessor_StudentID

class CharacterAnalyser:
    def __init__(self):

        self.df=pd.DataFrame(columns=['character'])
        

    def __str__(self):
        for word in self.df:
            print(word)

    def analyse_characters(self, tokenised_list):
        
        c =[]
        for word in tokenised_list:
            
            c =list(word)
            for i in c:
                self.df.loc[len(self.df)] = [i]

        df1 = pd.DataFrame(columns=['frq'])
        df1['frq'] = self.df['character'].value_counts()
        df1['val'] = df1.index
        df1['asc'] = df1['val'].apply(ord)
        self.df1=df1

        return df1
    def get_punctuation_frequency(self):
        df1 = self.df1[ self.df1['asc'] < 65]
        return df1

