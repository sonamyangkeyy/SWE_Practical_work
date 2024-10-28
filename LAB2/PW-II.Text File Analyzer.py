##Open and Read a Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:500])  # Print the first 500 characters

##Count the Number of Lines
def count_lines(content):
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

##Count Words
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")

##Find the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

            ##Calculate Average Word Length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")


            ##Combine Everything into a Main Function
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")

# Run the analysis
analyze_text('sample.txt')


#Exercises
def count_unique_words(text):
    text = text.lower()
    words = text.split()
    unique_words = set(words)
    return len(unique_words)
text = read_file('sample.txt')
unique_words_count = count_unique_words(text)
print(f"Number of unique words: {unique_words_count}")

def find_longest_words(text):
    words = text.split()
    longest_words = max(words, key=len)
    return longest_words
longest_words = find_longest_words(text)
print(f"The longest word is: '{longest_words}'")

def count_word_occurrencess(text, target_words):
    text = text.lower()
    target_words= target_words.lower()
    words = text.split()
    return words.count(target_words)

def calculate_average_word_length(text):
    words = text.split()
    if not words:
        return 0 
    total_length = sum(len(words)for words in words)
    return total_length / len(words)

def percentage_of_long_words(text):
    words = text.split()
    average_length = calculate_average_word_length(text)
    long_works = [words for words in words if len(words) > average_length]
    if not words:
        return 0
    return(len(long_works) / len(words)) * 100

text = read_file('sample.txt')
unique_words_count = count_unique_words(text)
print(f"Number of unique words: {unique_words_count}")
longest_words = find_longest_words(text)
print(f"The longest word is: '{longest_words}'")
target_words = "Technology"
word_occurrences = count_word_occurrencess(text, target_words)
print(f"the word '{target_words}' occurs {word_occurrences} times.")
long_word_percentage = percentage_of_long_words(text)
print(f"percentage of words longer than the average word length: {long_word_percentage: .2f}%")