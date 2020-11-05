# the list "walks" is already defined
# your code here
average = 0
for walk in walks:
    average += walk["distance"]
print(average // len(walks))
