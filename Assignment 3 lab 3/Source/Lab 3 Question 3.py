import nltk
from nltk.tokenize import sent_tokenize,word_tokenize # importing tokenization
from nltk.util import ngrams # importing library for bigrams
from collections import Counter # importing counter to count the bigrams
from nltk.stem import WordNetLemmatizer # imporitng the Lemmatizer for lemmatization

# Read the file
file= (open('Q3inputfile').read()) # opening the file and reading it
senten_token = sent_tokenize(file) # tokenizing the file in sentences
word_token = [] # array that will store word tokenization that will be used for lemmatization
for a in senten_token:
    word_token.append(word_tokenize(file)) # word tokenization
# Using Lemmatization, apply lemmatization on the words
word_lematiz = [] # array that will store word tokenization
Lemintize=WordNetLemmatizer() # declaring the lemmatizer
for b in word_token: # logic for lemmatization
    for w in b:
        word_lematiz.append(Lemintize.lemmatize(w,'v')) # applying lemmatization on words in the text file
print('After applying lemmatization on the words, the rsult is: ', word_lematiz) # printing the results

#Apply the bigram on the text
bigram = [] # array that will hold bigrams
b_logic = ngrams(word_lematiz,2) # declearing a variable to implement bigram logic
for k in b_logic:
    bigram.append(k)
print('\n','After applying the bigram on the text, the reslt is :', bigram) # printing the bigrams

#Calculate the word frequency (bi-gram frequency) of the words(bi-grams)
bigram_count = nltk.FreqDist(bigram) # counting the frequencies of bigrams
bigram_freq= [] # array that will store all the bigrams with their frequencies
for h, r in bigram_count.items():
    bigram_freq.append((h,r))
print('\n', 'The bi-grams along with their respective frequencies are: ',bigram_freq) # printing the bigram frequencies
# Choose top five bi-grams that has been repeated most
bigram_5common= [] # array that will store the top 5 bi-grams
bigram_5common=bigram_count.most_common(5) # internal function to find out the top 5 bi-grams
print('\n','The top five bi-grams that has been repeated most are: ',bigram_5common) # printing the results
#Find all the sentences with those most repeated bi-grams
bigram_text = [] # creating an array for holding only the text portion of 5 common bigrams excluding their frequencies
for word in bigram_5common: # logic for extracting text from bigrams
    bigram_text.append(word[0])
print('The 5 common bigram text is :',bigram_text)  # printing the result
concatenate_list=[]
for k in file.splitlines(): # finding the lines that contains 5 common bi-gram
    for a in range(5):
        if bigram_text[a][0] in k.split() and bigram_text[a][1] in k.split(): # if the bi-gram is present in sentence
            concatenate_list.append(k) # concatenate the list with given sentence

print('The sentences that contain the 5 most common bi-gram are: ',concatenate_list)

