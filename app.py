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
guess = input("Guess a word (use re): ")
#list all keys matching the regex
matching_keys = [key for key in keys if re.match(guess, key)]
print(matching_keys, end=", ")