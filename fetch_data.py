import urllib2
from bs4 import BeautifulSoup

def GetTextFromURL():
  input_url = raw_input("Enter a URL from Project Gutenberg: ") 
    # Asks for a URL from Project Gutenberg
  opened_url = urllib2.urlopen(input_url) 
    # urllib2 gets the html from the webpage
  html = opened_url.read()
    # Reads the thing urllib2 makes
  parsed_html = BeautifulSoup(html, features="lxml") 
    # BeautifulSoup parses the html
  text = parsed_html.get_text() 
    # Gets the text from the parsed html
  printable_text = text.encode("utf8") 
    # Deals with unprintable characters
  return printable_text 
    # returns the text from the webpage

def GetBookFromURL(): 
  text = GetTextFromURL()
    # Asks for a URL from Project Gutenberg
    # Gets text from that page
  start_text = "START OF THIS PROJECT GUTENBERG EBOOK"
    # Signifies beginning of book on Project Gutenberg pages
  end_text = "END OF THIS PROJECT GUTENBERG EBOOK"
    # Signifies end of book on Project Gutenberg pages
  first_slice = text.split(start_text)[1]
    # Slices text into two at the start text
    # Keeps the part after the start text
  second_slice = first_slice.split(end_text)[0]
    # Slices text into two at the end text
    # Keeps the part before the end text
  return second_slice
    # Returns the text with the intro and outro removed
    # So just the actual book remains