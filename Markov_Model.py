#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:04:16 2024

@author: ayragulati
"""

#
#
# Markov text generation
import random

# Function 1
def create_dictionary(filename):
    """takes in a string representing a text file and returns a dictionary
    of key-value pairs."""
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
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    return d

# Function 2
def generate_text(word_dict, num_words):
    """takes in a dictionary of words and a positive integer to generate a 
    specific number of words based on the num_words given.
    """
    current_word = '$'
    for i in range(num_words):
        wordlist = word_dict[current_word]
        next_word = random.choice(wordlist)
        print(next_word, end=' ')
        if next_word[-1] in '.!?':
            current_word = '$'
        else:
            current_word = next_word
    print()
    
    
    
    
    
    
    