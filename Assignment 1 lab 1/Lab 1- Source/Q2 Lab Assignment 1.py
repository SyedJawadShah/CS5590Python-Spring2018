sentence= input("Please enter a sentence:") # ask user to enter a sentence
my_sentence= sentence.split() # split the string per words
word_count = [] # list that will contain the length of each word along with the word
longest_word =[] # list that will contain the tuple that will have longest word
a= int(len(my_sentence)) # getting the length of sentence and storing in a variable
b = int (a/2) # finding the middle of the sentence
if a % 2 == 0: # logic to see if the length of the sentence is even
    print("The Middle words are: ","[",my_sentence[b-1], "", my_sentence[b],"]") # if lenght is even then print middle two words
else:
    print("The Middle words are: [",my_sentence[b], "]") # if length of sentece is odd then print middle word
for x in my_sentence: # sotring each word along with its length in a list word_count
    word_count.append((len(x),x))
word_count.sort() # sorting the list to make the longest word go to the last position
longest_word= word_count[-1] # storing the longest word and its length tuple into a new list
print("Longest word is: ",longest_word[1]) # printing only the word from the longet tuple
reverse= ' '.join(m[::-1] for m in my_sentence) # reversing the order of the words in sentence
print("sentence with reverse words is: ",reverse) # printing reverse ordered words in the sentence