def select_dates(potential_dates):
    date_names = ''
    for date in potential_dates:
        if date['age'] > 30 and date['city'] == 'Berlin' and 'art' in date['hobbies']:
            date_names += date['name'] + ', '
    return date_names[0:-2]
