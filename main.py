#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:07:47 2020

@author: Veerendranath Korrapati
"""

"""
Description: Given ham and spam train folders containing ham and spam emails in text format respectively, 
this program uses Naïve Bayes approach to learn about ham and spam emails from training set, then reads ham and spam test folders, 
each containing some ham and spam emails, and calculatses percent of ham files and spam files classified correctly 
in their respective folders
"""

import glob
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#Stop Words are the common words that the program ingores which calculating percentages
stopWordsArray = ["a", "about", "above", "after",
                  "again", "against", "all", "am", "an", "and", "any", "are",
                  "be", "because", "before", "below", "between", "but", "by", "cannot",
                  "could", "couldn't", "did", "didn't", "do", "does", "don't", "down",
                  "each", "few", "for", "from", "futher", "had", "hadn't", "has",
                  "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
                  "her", "here", "hers", "herself", "him", "himself", "his", "how",
                  "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into",
                  "is", "it", "it's", "itself", "let's", "me", "more", "most",
                  "mustn't", "my", "myself", "no", "not", "nor", "off", "of",
                  "on", "once", "only", "or", "other", "ought", "our", "ours",
                  "out", "own", "same", "she", "she'd", "she'll", "she's", "should",
                  "so", "some", "such", "than", "that", "that's", "the", "their",
                  "theirs", "them", "themselves", "then", "there", "these", "these", "they",
                  "they'd", "they'll", "they're", "this", "those", "through", "to", "too",
                  "under", "until", "up", "very", "was", "wasn't", "we", "were",
                  "what", "when", "where", "which", "while", "who", "whome", "why",
                  "with", "won't", "would", "you", "you'd", "you'll", "you've", "your",
                  "yours", "yourself", "yourselves"]



"""
Function is used to read files from ham and spam training set.
It reads all the words that are present in ham training emails, 
when the function argument is ham training files location, and 
reads all words that are present in spam training emails, when 
the function argument is spam training files location

Function also returns number of ham/spam test files
"""
def readFile(list_of_files):
    temp = []
    All_words_array = []
    number_of_files = 0
    for file_name in list_of_files:
        number_of_files = number_of_files + 1
        input_file = open(file_name, 'r')
        try:
            file_contents = input_file.read()
        except:
            continue
        input_file.close()
        temp = file_contents.split()
        for word in temp:
            if not (word in stopWordsArray):
                All_words_array.append(word)
    
    return All_words_array, number_of_files #returns all words that are present in ham/spam training folder
    										#and number of ham/spam training files
                
               

"""
Creating path to ham training folder and calling readFile() function to get all 
ham words in training files and number of ham training files present 
"""
files_path_ham = "/Users/Veeru/Desktop/Github-Spam-Ham-Classifer/train/ham"
list_of_files = glob.glob(os.path.join(files_path_ham,"*.txt"))
All_ham_words_array, number_of_ham_files = readFile(list_of_files)


"""
Creating path to spam training folder and calling readFile() function to get 
all spam words in training files and number of spam training files present 
"""
files_path_spam = "/Users/Veeru/Desktop/Github-Spam-Ham-Classifer/train/spam"
list_of_files = glob.glob(os.path.join(files_path_spam,"*.txt"))
All_spam_words_array, number_of_spam_files = readFile(list_of_files)



"""
This function is used to create var array. 
var array: array that contains all unique words of ham and spam training files.
"""
def Create_var(All_words_array, var):
    for i in All_words_array:
        if not (i in var):
            var.append(i)
    return var


#calling Create_var() to create and initialize var array
var = []
Create_var(All_ham_words_array, var)
Create_var(All_spam_words_array, var)

"""
This function is used to count the number of times a word(unique word) in var array
appeared in All_ham_words_array / All_spam_words_array
"""
def Count_var(All_words_array, var):
    count = 0
    varCount = []
    for word_1 in var:
        count = 0
        for word_2 in All_words_array:
            if(word_1 == word_2):
                count += 1
        varCount.append(count)
    return varCount

#varHamCount is same size as var and contains the number to times 
#a word in var[i] appeared in All_ham_words_array and stores this number in 
#varHamCount[i] place
varHamCount = Count_var(All_ham_words_array, var)
#varSpamCount is same size as var and contains the number to times 
#a word in var[i] appeared in All_spam_words_array and stores this number in 
#varSpamCount[i] place
varSpamCount = Count_var(All_spam_words_array, var)





"""
This function is used to read all the files that are in ham/spam test folder
and uses Naive Bayes approach to calculate number of ham/spam test files that 
are correctly clasified in ham/spam test folder respectively

Function is explained in great detail in ReadMe
"""
def CalculateAccuracy(typeOfFile,list_of_test_files, number_of_files):
    AllPercentages = []
    percentageOfFiles = number_of_files / (number_of_ham_files + number_of_spam_files)
    total_number_of_test_files = 0
    
    for file_name in list_of_test_files:
        total_number_of_test_files += 1
        PercentageArray = []
        temp = []
        input_file = open(file_name, 'r')
        try:
            file_contents = input_file.read()
        except:
            continue
        input_file.close()
        temp = file_contents.split()
        
        for word in temp:
            try:
                index = var.index(word)
            except:
                continue
            
            numberOfOccurance = 0
            if typeOfFile == "ham":
                numberOfOccurance = varHamCount[index]
                probWordGivenHam = numberOfOccurance / (len(All_ham_words_array) + len(var))
                PercentageArray.append(probWordGivenHam)
                
            else:
                numberOfOccurance = varSpamCount[index]
                probWordGivenSpam = numberOfOccurance / (len(All_spam_words_array) + len(var))
                PercentageArray.append(probWordGivenSpam)
                
        logArray = np.log10(PercentageArray)
        logArrayABS = np.abs(logArray)
        logArrayAdd = 0
        for num in logArrayABS:
            logArrayAdd += num
            
        FinalPercentage = logArrayAdd * np.log10(percentageOfFiles)
        AllPercentages.append(FinalPercentage)
    
    finalArray = []
    for number in AllPercentages:
        tempVal = np.abs(number)
        finalArray.append(tempVal)
        
    numOfCorrectFiles = 0
    for number in finalArray:
        if number > 50:
            numOfCorrectFiles += 1
            
    return numOfCorrectFiles, total_number_of_test_files
            
               

   
    
    


"""
Creating path to ham test folder and calling CalculateAccuracy() function to get
number of ham files that are correctly classified in ham training set and tolal number of 
ham test files
"""
files_path_ham = "/Users/Veeru/Desktop/Github-Spam-Ham-Classifer/test/ham"
list_of_test_files_ham = glob.glob(os.path.join(files_path_ham,"*.txt"))
numOfHamFiles, total_number_of_ham_test_files = CalculateAccuracy("ham" ,list_of_test_files_ham, number_of_ham_files)


"""
Creating path to spam test folder and calling CalculateAccuracy() function to get
number of spam files that are correctly classified in spam training set and tolal number of 
spam test files
"""
files_path_spam = "/Users/Veeru/Desktop/Github-Spam-Ham-Classifer/test/spam"
list_of_test_files_spam = glob.glob(os.path.join(files_path_spam,"*.txt"))
numOfSpamFiles, total_number_of_spam_test_files = CalculateAccuracy("spam" ,list_of_test_files_spam, number_of_spam_files)





#Output
print("Accuracies for ham and spam test files without stop words")
print("\t->For accuracies with stop words, read output PDF")
print()
print("Total number of ham files in test: ", total_number_of_ham_test_files)
print("Total number of ham files correctly classified: ", numOfHamFiles)
hamPercent = (numOfHamFiles / total_number_of_ham_test_files) * 100
hamPercent = str(round(hamPercent, 2))
print("Percent of ham files correctly classified: ", hamPercent, "%")

print("-------------------------------------------------------")


print("Total number of spam files in test: ", total_number_of_spam_test_files)
print("Total number of spam files correctly classified: ", numOfSpamFiles)
spamPercent = (numOfSpamFiles / total_number_of_spam_test_files) * 100
spamPercent = str(round(spamPercent, 2))
print("Percent of spam files correctly classified: ", spamPercent, "%")







