#Given a histogram tally (one returned from either letter_histogram or word_summary), 
# print the top 3 words or letters.

import string

def remove_punctuation(str):
    updated_str = ""
    for s in str:
        if s not in string.punctuation:
            updated_str += s
    return updated_str

def count_the_words(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

phrase = input("Enter a phrase ")
word_count = count_the_words(remove_punctuation(phrase))
sorted_word_count = sorted(word_count, reverse=True)
sObject = slice(0, 3)
print(sorted_word_count[sObject])
#print(word_count)