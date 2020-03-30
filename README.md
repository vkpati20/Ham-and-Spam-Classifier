<h1>Ham and Spam Classifer using Python</h1>

<h3>Files/Folders</h3>
Train folder: Contains two folders, Ham and Spam. Ham folder contains all the ham emails in .txt format and Spam folder contains all the spam emails in .txt format<br>
<br>
Test folder: Contains two folders, Ham and Spam. Ham folder contains ham and spam emails in .txt format and Spam folder also contain ham and spam emails in .txt format<br>
<br>

Output pdf: Contains the output of program with and without Stop words.<br>
  <em>Stop words: Words that are insignificant when classifying ham and spam emails</em>
  
  <hr>
 
<h3>Description</h3> 
Given Ham and Spam train folders containing ham and spam emails in text format respectively, this program uses <strong>Naïve Bayes</strong> approach to learn about ham and spam emails from training set, then reads ham and spam test folders, each containing some ham and spam emails, and calculates percent of ham files and spam files classified correctly 
in their respective folders

<hr>

<h3>Logic</h3>
1. The program reads all the words that are present in ham and spam training emails and stores them in <em><strong>All_ham_words_array</strong></em> and <em><strong>All_spam_words_array</strong></em> respectively.<br>
<br>

2. Then the program creates <em><strong>var</strong></em> array that contains all the unique words that are present in <em><strong>All_ham_words_array</strong></em> and <em><strong>All_spam_words_array</strong></em>. Next, the program counts the number of times a unique word from <em><strong>var</strong></em> occured in <em><strong>All_ham_words_array</strong></em> and <em><strong>All_spam_words_array</strong></em> and stores the values in <em><strong>varHamCount</strong></em> and <em><strong>varSpamCount</strong></em> arrays<br>
<br>

3.<strong>Naive Bayes approach</strong><br>
Goal is to get P(ham |test file) and P(spam | test file) for all the files that are inside their respective folder.<br> <em>P(ham | test file) = probability that the given file is ham</em><br>

P(ham | test file) = P(ham | 'word1', 'word2', word3', ....) <br>
P(ham | test file) = (P('word1', 'word2', word3', .... | ham)) * P(ham)<br>
P(ham | test file) = (P('word1'| ham) * P('word2'| ham) * P('word3'| ham) * ....) * P(ham)<br>
<br>
ex: P('word1' | ham) = count of word1 occurance in <em><strong>All_ham_words_array</strong></em> + 1 / (size of <em><strong>All_ham_words_array</strong></em> + size of <em><strong>var</strong></em>)
<em>count of word1 occurance in <strong>All_ham_words_array</strong> is given by <strong>varHamCount</strong> array</em>

ex: P(ham) = number of ham traiing files / (number of ham training files + number of training spam)

After calculating <strongP('word1' | ham)</strong> = percentage of each word in Ham test file, I take abs(log10(pergentage), and add all the percentages of all words to get <strong>(P('word1', 'word2', word3', .... | ham))</strong>. Then I take log(P(ham)) and multiply it with (P('word1', 'word2', word3', .... | ham)) to get <strong>P(ham | test file)</strong>. I do this for all the files that are in ham test folder and store all the percentages of P(ham | test file) in <em><strong>AllPercentages array</em></strong>. <br>
<br>
Then I check each value in <em><strong>AllPercentages array</em></strong>, and consider it ham if value is greater than 50 not ham and if value is less than or equal to 50. This gives me number of ham files in ham folder. 

<strong>DO THE SAME WITH SPAM TEST FILES</strong>

The program outputs:


