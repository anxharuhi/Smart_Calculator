# write your code here
user_input = True
while user_input != '/exit':
    user_input = input()
    if user_input != '/exit':
        values = list(map(int, user_input.split()))
        if len(values) == 1:
            print(values[0])
        elif len(values) == 2:
            print(values[0] + values[1])
print('Bye!')