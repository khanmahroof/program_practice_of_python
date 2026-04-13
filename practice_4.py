#String Operations: wor  frequency Counter
item = "apple, banana, apple, CHEERY, apple!, orange"
word = item.split()

word_counts ={}

for word in word:
    word_counts[word] = word_counts.get(word,0) +1
print(word_counts)