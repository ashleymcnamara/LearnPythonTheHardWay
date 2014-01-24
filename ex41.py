import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
                "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
                "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)":
                "class %%% has-a function names *** that takes self and @@@ parameters.",
        "*** = %%%()":
                "Set *** to an instance of class %%%.",
        "***.***(@@@)":
                "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
                "From *** get the *** attribute and set it to '***'."
}

# Do they want to drill phrases first?
# Line 30 Sets variable "PHRASE_FIRST" to False or under certian circumstances True 
# Line 31 Meaning you have to have passed at least two arguments to the program (cont)
# (the first being the program name itself), and said second argument has to be "english"
# Line 32 Resets "PHRASE_FIRST" to be true IF len(sys.argv) == 2 and sys.argv[1] == "english"
# Sys.argv is the command line arguments, starting with the name of the program, i.e. exercise_41.py
# English becomes ['exercise_41.py', 'english'], and said second argument (sys.argv[1]) has to be "english"
PHRASE_FIRST = False 
if len(sys.argv) == 2 and sys.argv[1] == "english": 
    PHRASE_FIRST = True 

# Load up the words from the website
# For word in URLOPEN(word_url).readlines():
# Use a for loop and a local copy of the word list
# For word in open 'words.txt', read
# Words.append [word.strip()
# Using list comprehensions. 
WORDS = [word.strip() for word in 
                        open('words.txt', 'r')]

# Line 47, define convert and give it snippet and phrase paramaters
# Lines 48 - 52, Return a list of random words for each "%%%" pattern in snippet string
# Capitalize each word in the list
# Return the list
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
     # Line 54, a number for each paramater placement
    for i in range(0, snippet.count("@@@")):
        # Line 56, insert 1 or 2 random words
        param_count = random.randint(1,3)
         # Line 58, Seperate the words by a comma. 
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    # Shortening the list, creating a new list with a reference to the contained objects
    # List (start:step:end)
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"
