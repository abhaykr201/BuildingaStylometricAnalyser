import pandas as pd
#import preprocessor_StudentID
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class WordAnalyser:
    def __init__(self):
        self.df = pd.DataFrame(columns=['col'])
        
    def __str__(self):
        s=''
        for word in self.df:
            s = s+" "+word

    def analyse_word(self, tokenised_list):
        self.df = pd.DataFrame({'col':tokenised_list})
        
        df1 = pd.DataFrame(columns=['frq'])
        df1['frq'] = self.df['col'].value_counts()
        df1['val'] = df1.index
        self.df =  df1
        self.tokenised_list = tokenised_list
        return df1
        
        
    def get_stopword_frequency(self):
        stop_word = set(stopwords.words('english'))

        filtered_sentence = []

        for w in self.tokenised_list:
            if(w in stop_word):
                filtered_sentence.append(w)

        df = pd.DataFrame({'col':filtered_sentence})
        df1 = pd.DataFrame(columns = ['frq'])
        
        df1['frq'] = df['col'].value_counts()
        df1['val'] = df1.index
        return df1

    def get_word_length_frequency(self):

        df = pd.DataFrame({'col':self.tokenised_list})
        df['len'] = df['col'].str.len()
        df1 = pd.DataFrame(columns=['frq'])
        df1['frq'] = df['len'].value_counts()
        df1['val'] = df1.index
        return df1
        
    
  
        
        


