def tallest_people(**people):
    biggest_people = []
    max_height = 0
    for name, height in people.items():
        if height > max_height:
            biggest_people = []
            max_height = height
        if height >= max_height:
            biggest_people.append(name)
    biggest_people.sort()
    for name in biggest_people:
        print(name, ':', max_height)
