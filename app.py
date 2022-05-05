import json
import re
size = tries = 5
vowel = ['a', 'e', 'i', 'o', 'u']
def count_vowels(word):
    # count unique vowels in a word
    count = 0
    for i in set(word):
        if i in vowel:
            count += 1
    return count

dicti = json.load(open('words_dictionary.json'))
#make list of all keys with size of 5
keys = [key for key in dicti.keys() if len(key) == size]
# make list of keys with count of vowels equal to 4
starters = [key for key in keys if count_vowels(key) == 4]
print('Starters: ',starters)
blklist = list(input("Input blacklisted words: "))
print(blklist)
whtlist = list(input("Input whitelisted words: "))
print(whtlist)
guess = input("Guess a word (use re): ")
#list all keys matching the regex
matching_keys = [key for key in keys if re.match(guess, key)]
#remove blacklisted alphabets
for i in blklist:
    matching_keys = [key for key in matching_keys if i not in key]
#only whiltelisted alphabets
for i in whtlist:
    matching_keys = [key for key in matching_keys if i in key]
print(matching_keys)
possible = open('possible_words.txt', 'r')
possible_words = possible.read().splitlines()
# select keys from possible words
possible_keys = [key for key in matching_keys if key in possible_words]

print("possible: ",possible_keys)