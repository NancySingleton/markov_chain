from fetch_data import GetBookFromURL
from markov_python.cc_markov import MarkovChain
import random
import time
import re

def ListToSentence(word_list):
	# Turns a list of words into a sentence
  sentence = ""
  for word in word_list:
  	# For each word in the list:
    sentence = sentence + " " + word
      # Adds word to the sentence
  return sentence

def FormatSentence(sentence):
  letters_only = re.compile('[^a-zA-Z ]')
  sentence = letters_only.sub('', sentence)
    # Strips non letters
  sentence = sentence.replace("  ", " ")
    # Replaces double space with single (double space may have occurred if " was a word in the list)
  sentence = sentence.replace(" i ", " I ")
    # Capitalises single "i"  
  sentence = sentence.replace(" i.", " I.")
    # Capitalises single "i"
  sentence = sentence[1].upper() + sentence[2:] + ". "
    # Removes initial space, capitalises first letter, adds full stop
  return sentence

def GenerateSentence(markov_chain):
  length = random.randint(4,20)
    # Decides the length of the sentence
  word_list = markov_chain.generate_text(length)
    # Generates a list of words
  sentence = ListToSentence(word_list)
    # Changes list to sentence
  sentence = FormatSentence(sentence)
    # Formats the sentence
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
    sentence = GenerateSentence(mc)
      # Generates a sentence
    output += sentence
      # Adds it to the output
  return output

print "Hi! This program generates text based on a book of your choice from Project Gutenberg."
time.sleep(.5)
print "..."
time.sleep(.5)
print GenerateText()