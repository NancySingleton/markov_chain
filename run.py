from fetch_data import GetBookFromURL
from markov_python.cc_markov import MarkovChain
import random

def FormatSentence(word_list):
	# Turns a list of words into a formatted sentence
	# TO DO: GET RID OF ANY PUNCTUATION IN THE LIST
  sentence = ""
  for word in word_list:
  	# For each word in the list:
    sentence = sentence + " " + word
      # Adds each word to the sentence
  sentence = sentence[1].upper() + sentence[2:] + ". "
    # Removes initial space, capitalises first letter, adds full stop
  return sentence

def GenerateText():
  mc = MarkovChain()
    # Creates a Markov chain
  book = GetBookFromURL()
    # Gets book text
  mc.add_string(book)
    # Gives it to Markov chain
  number_of_sentences = raw_input("How many sentences would you like to generate? ")
    # Finds out how many sentences to output
    # TO DO: CHECK INPUT IS A NUMBER

  output = ""
  for x in range(int(number_of_sentences)):
  	# For each sentence:
    length = random.randint(4,20)
      # Decides the length of the sentence
    word_list = mc.generate_text(length)
      # Generates the sentence
    sentence = FormatSentence(word_list)
      # Formats the sentence
    output += sentence
  return output

print GenerateText()