#!/usr/bin/env python3
# This is a program for executing the Caesar cipher of shifing charcters
# 3 places alphabetically

""" Decoding and Encoding of Strings """
import string
# from string import *
# from random import randint
# import os
# from os import chdir
from os import getcwd
from os import listdir


def encode(text):
    """ Encode some text"""
    converted_text = ''
    for letter in text:
        if letter == ' ':
            converted_text = converted_text + ' '
        else:
            x_encode = LETTERS.index(letter) + SHIFT
            converted_text = converted_text + LETTERS[x_encode]
    return converted_text


def decode(text):
    """ Decode some text """
    converted_text = ''
    for letter in text:
        if letter == ' ':
            converted_text = converted_text + ' '
        else:
            x_encode = LETTERS.index(letter) - SHIFT
            converted_text = converted_text + LETTERS[x_encode]
    return converted_text


def do_nothing():
    """ Do nothing """
    x_step = getcwd()
    x_step = listdir(x_step)


SHIFT = 3
CONVERTED = ''
FLAG1 = True
FLAG2 = False
FLAG3 = False
LETTERS = string.ascii_letters + string.punctuation + string.digits

if __name__ == '__main__':
    while True:
        choice = input("\tWould you like to encode, decode or quit?").lower()
        CONVERTED = ''
        if choice == "encode":
            CONVERTED = encode(input('Enter text to encode:'))
        elif choice == "decode":
            CONVERTED = decode(input('Enter text to decode:'))
        elif choice == 'quit':
            break
        else:
            print(choice, 'is unknown command. Please enter a supported one.')
            continue
            # print('out of here')
        print('Conversion:', CONVERTED)
        if not FLAG1:
            print('dead')
        continue
        # do_nothing()

    if FLAG2 is True:
        print('more dead')
