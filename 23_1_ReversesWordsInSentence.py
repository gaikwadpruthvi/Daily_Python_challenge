# Write a function that reverses words in a sentence while keeping word order.

def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Reverse each word and join them back together
    reversed_sentence = ' '.join(word[::-1] for word in words)
    return reversed_sentence

# Taking input from the user
user_input = input("Enter a sentence: ")
print("Reversed words sentence:", reverse_words(user_input))
