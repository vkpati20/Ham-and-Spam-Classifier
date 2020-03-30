<h1>Ham and Spam Classifer using Python</h1>

<h3>Files/Folders</h3>
Train folder: Contains two folders, Ham and Spam. Ham folder contains all the ham emails in .txt format and Spam folder contains all the spam emails in .txt format

Test folder: Contains two folders, Ham and Spam. Ham folder contains ham and spam emails in .txt format and Spam folder also contain ham and spam emails in .txt format

Output pdf: Contains the output of program with and without Stop words.<br>
  <em>Stop words: Words that are insignificant when classifying ham and spam emails<em>
  
 
<h3>Description</h3> 
Given ham and spam train folders containing ham and spam emails in text format respectively, this program uses <strong>Naïve Bayes</strong> approach to learn about ham and spam emails from training set, then reads ham and spam test folders, each containing some ham and spam emails, and calculatses percent of ham files and spam files classified correctly 
in their respective folders

<h3>Logic</h3>
1. The program reads all the words that are present in ham and spam training emails and stores them in All_ham_words_array and All_spam_words_array respectively.

2. Then the program creates var array that contain all the unique words that are present in All_ham_words_array and All_spam_words_array. Next, the program counts the number of times a unique word from var occured in All_ham_words_array and All_spam_words_array and stores the values in varHamCount and varSpamCount arrays

3.Naive Bayes approach
Goal is to get P(ham |test file) and P(spam | test file) for all the files that are inside their respective folder.<br> <em>P(ham | test file) = probability that the given file is ham</em><br>

P(ham | test file) = P(ham | 'word1', 'word2', word3', ....) 
                   = (P('word1', 'word2', word3', .... | ham)) * P(ham)
                   = (P('word1'| ham) * P('word2'| ham) * P('word3'| ham) * ....) * P(ham)
ex: P('word1' | ham) = count of word1 occurance in All_ham_words_array + 1 / (size of All_ham_words_array + size of var)
<em>count of word1 occurance in All_ham_words_array is given by varHamCount array</em>

ex: P(ham) = number of ham traiing files / (number of ham traiing files + number of traiing spam)

After calculating P('word1' | ham) = percentage each word in Ham test file, I take abs(log10(pergentage), and add all the percentages of all words to get (P('word1', 'word2', word3', .... | ham)). Then I take log(P(ham)) and multiply it with (P('word1', 'word2', word3', .... | ham)) to get P(ham | test file). I do this for all the files that are in ham test folder and store all the percentages of P(ham | test file) in AllPercentages array. 
Then I check if a value is greater than 50 in AllPercentages, consider it ham and if it is less than or equal to 50, consider it not ham. This gives me number of ham files in ham folder. 

<strong>DO THE SAME WITH SPAM TEST FILES</strong>

The program outputs:


