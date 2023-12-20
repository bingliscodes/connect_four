
## ps9pr3.py ##
# Markov text generation #
import random
# Part 1: Create_dictionary
def create_dictionary(filename):
    """ takes a string representing filename and returns a dictionary of key_value
        pairs in which each word is encountered, and the corresponding value is
        a list of words that follow the key word"""
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()

    d = {}
    current_word = '$'

    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]

        if next_word[-1] in '. ? !':
            current_word = '$'
        else:
            current_word = next_word
    
    return d

# Part 2: generate_text:
def generate_text(word_dict, num_words):
    """ takes a dictionary created by create_dictionary and a positive int num_words
        to generate randomly generated text that follows the patterns of the original
        text.
    """
    # a variable to represent the key.  Starting with sentence starters
    word_reference = '$'
    
    # loop using num_words as a counter        
    while num_words > 0:  
        wordlist = word_dict[word_reference]
        next_word = random.choice(wordlist)
        print(next_word, end = ' ')
        word_reference = next_word
        num_words -= 1

        if next_word[-1] in '. ? !' or len(word_dict[next_word]) == 0:
            word_reference = '$'
        
        
        

        
        
                
        
