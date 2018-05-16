import visualiser_StudentID as vs

def main():
    f1, f2, f3, f4, f5, f6 = read_input()
    ob = vs.AnalysisVisualiser(f1, f2, f3, f4, f5, f6)
    flow = 1
    ch = 0
    while(flow == 1):
        ch = input('Enter One Choice of your analysis \n1. character frequency\n2. punctuation frequency\n3. stopword frequency\n4. word length frequency\n ')
        ch = int(ch)
        if(ch == 1):

            ob.visualise_character_frequency()
            
        elif(ch == 2):
            ob.visualise_punctuation_frequency()

        elif(ch == 3):
            ob.visualise_stopword_frequency()

        elif(ch == 4):
            ob.visualise_word_length_frequency()
            print("hello")
        else:
            
            flow = 0
            
            
def read_input():
    
    f1 = open('Richard_II_Shakespeare.tok')
    f2 = open('Edward_II_Marlowe.tok')
    f3 = open('Hamlet_Shakespeare.tok')
    f4 = open('Henry_VI_Part1_Shakespeare.tok')
    f5 = open('Henry_VI_Part2_Shakespeare.tok')
    f6 = open('Jew_of_Malta_Marlowe.tok')

    return f1,f2,f3,f4,f5,f6


main()

