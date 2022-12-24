# Виталий Милентьев

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.
# Examples
#
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# Урок 11, дз №1

def pig_it(text):
    zz = text.split()
    num1 = 0
    zz2 = zz[-1][-1]
    if bool(len(zz[-1]) == 1 and zz2 == '!' or zz2 == '?' or zz2 == '.'):
        xx2 = ' ' + zz[-1]
        zz.remove(zz[-1])
        num1 = 1
    elif zz2 == '!' or zz2 == '?' or zz2 == '.':
        xx = zz[-1]
        xx2 = zz[-1][-1]
        zz.remove(zz[-1])
        zz.append(xx[:len(xx)-1:])
        num1 = 1

    z = []
    x = ''
    x1 = ''
    x2 = 'ay'
    cnt = 0
    for c in range(0, len(zz)):
        for i in zz[c]:
            if cnt == 0:
                x = i
                cnt =+1
            elif cnt >= 1:
                x1 = x1 + i
                cnt = +1
        z.append(x1 + x + x2)
        cnt = 0
        x1 = ''
        x = ''
    z2 = ''
    for i in z:
        z2 = z2 + i + ' '

    if num1 == 0:
        return z2.rstrip(' ')
    else:
        return z2.rstrip(' ') + xx2

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
# become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
#
# You can assume that all values are integers. Do not mutate the input array/list.
# Урок 11, дз №2

def invert(lst):
    z = []
    for i in lst:
        if i > 0:
            z.append(i * -1)
        else:
            z.append(i * -1)
    return z

# In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples
# up to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever
# be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.
#
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the
# multiples of 2 up to 6.
# Урок 11, дз №3

def find_multiples(integer, limit):
    z = []
    for i in range(integer, limit+1, integer):
        z .append(i)
    return z

# This function should return an object, but it's not doing what's intended. What's wrong?
# Урок 11, дз №4

def mystery():
    results = {
    'sanity': 'Hello'}
    return results

# Create a function that returns the CSV representation of a two-dimensional numeric array.
#
# Example:
#
# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]]
#
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'
#
# Array's length > 2.
#
# More details here: https://en.wikipedia.org/wiki/Comma-separated_values
# Урок 11, дз №5

def to_csv_text(array):
    x = ''
    for i in array:
        z = ''
        for o in i:
            z = z + str(o) + ','
        x = x + z.rstrip(',') + '\n'
    return x.rstrip('\n')

# Debugging sayHello function
#
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard.
# It is your job to fix the code and get the program working again!
#
# Example output:
#
# Hello, Mr. Spock
# Урок 11, дз №6

def say_hello(name):
    return f"Hello, {name}"

# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#
# Define String.prototype.toAlternatingCase (or a similar
# function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see
# the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter
# becomes lowercase. For example:
#
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
#
# As usual, your function/method should be pure, i.e. it should not mutate the original string.
# Урок 11, дз №7

def to_alternating_case(string):
    z = ''
    for i in string:
        if i.isupper():
            z = z + i.lower()
        else:
            z = z + i.upper()
    return z

# Inspired by the development team at Vooza, write the function that
#
#     accepts the name of a programmer, and
#     returns the number of lightsabers owned by that person.
#
# The only person who owns lightsabers is Zach, by the way. He owns 18, which is an awesome number of lightsabers.
# Anyone else owns 0.
#
# Note: your function should have a default parameter.
#
# For example(Input --> Output):
#
# "anyone else" --> 0
# "Zach" --> 18
# Урок 11, дз №8

def how_many_light_sabers_do_you_own(name=''):
    if name == None:
        return 0
    elif name == 'Zach':
        return 18
    else:
        return 0

# Write a function that checks if a given string (case insensitive) is a palindrome.
# Урок 11, дз №9

def is_palindrome(s):
    s = s.lower()
    x = ''
    for i in s[::-1]:
        x = x + i
    return (s == x)

# Note: This kata is inspired by Convert a Number to a String!. Try that one too.
# Description
#
# We need a function that can transform a string into a number. What ways of achieving this do you know?
#
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an
# integral number.
# Examples
#
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7
# Урок 11, дз №10

def string_to_number(s):
    s = int(s)
    return s

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
# Урок 11, дз №11

def remove_exclamation_marks(s):
    z = ''
    for i in s:
        if i == '!':
            continue
        else:
            z = z + i
    return z
