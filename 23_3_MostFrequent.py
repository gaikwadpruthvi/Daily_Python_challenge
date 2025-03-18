#	Create a function that returns the most frequent word in a string.

from collections import Counter

def most_frequent_word(text):
    # Split the text into words
    words = text.split()
    # Count the frequency of each word
    word_counts = Counter(words)
    # Find the most common word
    most_common_word, _ = word_counts.most_common(1)[0]
    return most_common_word

# Taking input from the user
user_input = input("Enter a sentence: ")
print("Most frequent word:", most_frequent_word(user_input))
