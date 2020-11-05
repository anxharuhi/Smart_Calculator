# put your python code here
text = input().lower().split()
occurrences = {}

for word in text:
    occurrences[word] = occurrences.get(word, 0) + 1

{word: text_lower.count(word) for word in text_lower}

for word, occurrence in occurrences.items():
    print(word, occurrence)
