# Read a text file and count the occurrences of each word using a dictionary. 

def count_word_occurrences(file_path):
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    word = word.strip(".,!?()[]{}:;'")  # Remove punctuation
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1
    except FileNotFoundError:
        print("Error: File not found.")
        return {}
    
    return word_counts


def main():
    file_path = input("Enter the file path: ")
    word_counts = count_word_occurrences(file_path)
    
    if word_counts:
        print("\nWord occurrences:")
        for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()
