# write your code here
user_input = True
while user_input != '/exit':
    user_input = input()
    if user_input == '/help':
        print('The program calculates the sum of numbers')
    elif user_input == '':
        pass
    elif user_input != '/exit':
        values = list(map(int, user_input.split(' ')))
        result = 0
        for number in values:
            result += number
        print(result)
    else:
        print('Bye!')