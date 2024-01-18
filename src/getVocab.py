import re
import os

# Read file contents
with open('all.text', 'r') as f:
    content = f.read()

# Extract the words in the sentence
words = re.findall(r'\b\w+\b', content)

# Save words to txt file
existing_words = set()
if os.path.exists('existing_words.txt'):
    with open('existing_words.txt', 'r') as f:
        for line in f:
            existing_words.add(line.strip())

new_words = []
for word in words:
    if word not in existing_words:
        new_words.append(word)
        existing_words.add(word)

if new_words:
    with open('new_words.txt', 'a') as f:
        f.write('\n'.join(new_words))

# Create a new word file (if it does not exist)
if not os.path.exists('existing_words.txt'):
    with open('existing_words.txt', 'w') as f:
        f.write('\n'.join(existing_words))