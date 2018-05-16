import pandas as pd
import numpy as np
import word_StudentID as ws
import preprocessor_StudentID as pre
import character_Student as cha
import matplotlib.pyplot as plt


class AnalysisVisualiser:
    
    def __init__(self, df1, df2, df3, df4, df5, df6):

        self.df_rich = open('Richard_II_Shakespeare.tok')
        self.df_Edw = open('Edward_II_Marlowe.tok')
        self.df_ham = open('Hamlet_Shakespeare.tok')
        self.df_hen1 = open('Henry_VI_Part1_Shakespeare.tok')
        self.df_hen2 = open('Henry_VI_Part2_Shakespeare.tok')
        self.df_jew = open('Jew_of_Malta_Marlowe.tok')
        
        
    def visualise_character_frequency(self):
        ob1 = pre.Preprocessor()
        ob2 = pre.Preprocessor()
        ob3 = pre.Preprocessor()
        ob4 = pre.Preprocessor()
        ob5 = pre.Preprocessor()
        ob6 = pre.Preprocessor()
        
        print("part 1")
        
        ob1.tokenise(self.df_rich)
        ob2.tokenise(self.df_Edw)
        ob3.tokenise(self.df_ham)
        ob4.tokenise(self.df_hen1)
        ob5.tokenise(self.df_hen2)
        ob6.tokenise(self.df_jew)
        
        print("part 2")
        
        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()

        print("part 3")

        ob_ws1 = ws.WordAnalyser()
        ob_ws2 = ws.WordAnalyser()
        ob_ws3 = ws.WordAnalyser()
        ob_ws4 = ws.WordAnalyser()
        ob_ws5 = ws.WordAnalyser()
        ob_ws6 = ws.WordAnalyser()


        print("part 5")

        ob_cha1 = cha.CharacterAnalyser()
        ob_cha2 = cha.CharacterAnalyser()
        ob_cha3 = cha.CharacterAnalyser()
        ob_cha4 = cha.CharacterAnalyser()
        ob_cha5 = cha.CharacterAnalyser()
        ob_cha6 = cha.CharacterAnalyser()

        print("part 6")

        ac1 = ob_cha1.analyse_characters(token1)
        ac2 = ob_cha2.analyse_characters(token2)
        ac3 = ob_cha3.analyse_characters(token3)
        ac4 = ob_cha4.analyse_characters(token4)
        ac5 = ob_cha5.analyse_characters(token5)
        ac6 = ob_cha6.analyse_characters(token6)

        plt.plot(ac1['val'], ac1['frq'], label = 'Richard_II_Shakespeare')
        plt.plot(ac2['val'], ac2['frq'], label = 'Edward_II_Marlowe')
        plt.plot(ac3['val'], ac3['frq'], label = 'Hamlet_Shakespeare')
        plt.plot(ac4['val'], ac4['frq'], label = 'Henry_VI_Part1_Shakespeare')
        plt.plot(ac5['val'], ac5['frq'], label = 'Henry_VI_Part2_Shakespeare')
        plt.plot(ac6['val'], ac6['frq'], label = 'Jew_of_Malta_Marlowe')
        plt.title('character_frequency')
        plt.show()

        


        

    def visualise_punctuation_frequency(self):

        ob1 = pre.Preprocessor()
        ob2 = pre.Preprocessor()
        ob3 = pre.Preprocessor()
        ob4 = pre.Preprocessor()
        ob5 = pre.Preprocessor()
        ob6 = pre.Preprocessor()
        
        print("part 1")
        
        ob1.tokenise(self.df_rich)
        ob2.tokenise(self.df_Edw)
        ob3.tokenise(self.df_ham)
        ob4.tokenise(self.df_hen1)
        ob5.tokenise(self.df_hen2)
        ob6.tokenise(self.df_jew)
        
        print("part 2")
        
        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()

        print("part 3")

        ob_ws1 = ws.WordAnalyser()
        ob_ws2 = ws.WordAnalyser()
        ob_ws3 = ws.WordAnalyser()
        ob_ws4 = ws.WordAnalyser()
        ob_ws5 = ws.WordAnalyser()
        ob_ws6 = ws.WordAnalyser()

        print("part 4")

        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()

        print("part 5")

        ob_cha1 = cha.CharacterAnalyser()
        ob_cha2 = cha.CharacterAnalyser()
        ob_cha3 = cha.CharacterAnalyser()
        ob_cha4 = cha.CharacterAnalyser()
        ob_cha5 = cha.CharacterAnalyser()
        ob_cha6 = cha.CharacterAnalyser()

        print("part 6")

        ob_cha1.analyse_characters(token1)
        ob_cha2.analyse_characters(token2)
        ob_cha3.analyse_characters(token3)
        ob_cha4.analyse_characters(token4)
        ob_cha5.analyse_characters(token5)
        ob_cha6.analyse_characters(token6)
        
        print("part 7")
        
        pun1 = ob_cha1.get_punctuation_frequency()
        pun2 = ob_cha2.get_punctuation_frequency()
        pun3 = ob_cha3.get_punctuation_frequency()
        pun4 = ob_cha4.get_punctuation_frequency()
        pun5 = ob_cha5.get_punctuation_frequency()
        pun6 = ob_cha6.get_punctuation_frequency()

        print("part 8")

        plt.plot(pun1['val'], pun1['frq'], label = 'Richard_II_Shakespeare')
        plt.plot(pun2['val'], pun2['frq'], label = 'Edward_II_Marlowe')
        plt.plot(pun3['val'], pun3['frq'], label = 'Hamlet_Shakespeare')
        plt.plot(pun4['val'], pun4['frq'], label = 'Henry_VI_Part1_Shakespeare')
        plt.plot(pun5['val'], pun5['frq'], label = 'Henry_VI_Part2_Shakespeare')
        plt.plot(pun6['val'], pun6['frq'], label = 'Jew_of_Malta_Marlowe')
        plt.title('punctuation_frequency')
        plt.show()


        
        

        


    def visualise_stopword_frequency(self):

        ob1 = pre.Preprocessor()
        ob2 = pre.Preprocessor()
        ob3 = pre.Preprocessor()
        ob4 = pre.Preprocessor()
        ob5 = pre.Preprocessor()
        ob6 = pre.Preprocessor()
        
        print("part 1")
        
        ob1.tokenise(self.df_rich)
        ob2.tokenise(self.df_Edw)
        ob3.tokenise(self.df_ham)
        ob4.tokenise(self.df_hen1)
        ob5.tokenise(self.df_hen2)
        ob6.tokenise(self.df_jew)
        
        print("part 2")
        
        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()

        print("part 3")

        ob_ws1 = ws.WordAnalyser()
        ob_ws2 = ws.WordAnalyser()
        ob_ws3 = ws.WordAnalyser()
        ob_ws4 = ws.WordAnalyser()
        ob_ws5 = ws.WordAnalyser()
        ob_ws6 = ws.WordAnalyser()

        print("part 4")

        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()


        stop1 = ob_ws1.get_stopword_frequency()
        stop2 = ob_ws2.get_stopword_frequency()
        stop3 = ob_ws3.get_stopword_frequency()
        stop4 = ob_ws4.get_stopword_frequency()
        stop5 = ob_ws5.get_stopword_frequency()
        stop6 = ob_ws6.get_stopword_frequency()

        plt.plot(stop1['val'], stop1['frq'], label = 'Richard_II_Shakespeare')
        plt.plot(stop2['val'], stop2['frq'], label = 'Edward_II_Marlowe')
        plt.plot(stop3['val'], stop3['frq'], label = 'Hamlet_Shakespeare')
        plt.plot(stop4['val'], stop4['frq'], label = 'Henry_VI_Part1_Shakespeare')
        plt.plot(stop5['val'], stop5['frq'], label = 'Henry_VI_Part2_Shakespeare')
        plt.plot(stop6['val'], stop6['frq'], label = 'Jew_of_Malta_Marlowe')
        plt.title('stopword_frequency')
        plt.show()
         

        


    def visualise_word_length_frequency(self):
        
        ob1 = pre.Preprocessor()
        ob2 = pre.Preprocessor()
        ob3 = pre.Preprocessor()
        ob4 = pre.Preprocessor()
        ob5 = pre.Preprocessor()
        ob6 = pre.Preprocessor()
        
        print("part 1")
        
        ob1.tokenise(self.df_rich)
        ob2.tokenise(self.df_Edw)
        ob3.tokenise(self.df_ham)
        ob4.tokenise(self.df_hen1)
        ob5.tokenise(self.df_hen2)
        ob6.tokenise(self.df_jew)
        
        print("part 2")
        
        token1 = ob1._tokenised_list()
        token2 = ob2._tokenised_list()
        token3 = ob3._tokenised_list()
        token4 = ob4._tokenised_list()
        token5 = ob5._tokenised_list()
        token6 = ob6._tokenised_list()

        print("part 3")


        ob_ws1 = ws.WordAnalyser()
        ob_ws2 = ws.WordAnalyser()
        ob_ws3 = ws.WordAnalyser()
        ob_ws4 = ws.WordAnalyser()
        ob_ws5 = ws.WordAnalyser()
        ob_ws6 = ws.WordAnalyser()

        print("part 4")

        ob_ws1.analyse_word(token1)
        ob_ws2.analyse_word(token2)
        ob_ws3.analyse_word(token3)
        ob_ws4.analyse_word(token4)
        ob_ws5.analyse_word(token5)
        ob_ws6.analyse_word(token6)

        print("part 5")

        le_frq1 = ob_ws1.get_word_length_frequency()
        le_frq2 = ob_ws2.get_word_length_frequency()
        le_frq3 = ob_ws3.get_word_length_frequency()
        le_frq4 = ob_ws4.get_word_length_frequency()
        le_frq5 = ob_ws5.get_word_length_frequency()
        le_frq6 = ob_ws6.get_word_length_frequency()

        print("part 6")

        
        

        plt.plot(le_frq1['val'], le_frq1['frq'], label = 'Richard_II_Shakespeare')
        plt.plot(le_frq2['val'], le_frq2['frq'], label = 'Edward_II_Marlowe' )
        plt.plot(le_frq3['val'], le_frq3['frq'], label = 'Hamlet_Shakespeare' )
        plt.plot(le_frq4['val'], le_frq4['frq'], label = 'Henry_VI_Part1_Shakespeare')
        plt.plot(le_frq5['val'], le_frq5['frq'], label = 'Henry_VI_Part2_Shakespeare')
        plt.plot(le_frq6['val'], le_frq6['frq'], label = 'Jew_of_Malta_Marlowe')
        plt.title('word_length_frequency')
        plt.show()
        
                                           


                                              
