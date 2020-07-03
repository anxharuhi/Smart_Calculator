# write your code here

class Calculator:

    def __init__(self, user_input=None):
        self.user_input = user_input

    def messages(self):
        pass

    def logic(self, input):
        self.user_input = input
        if self.user_input == '/help':
            print('The program calculates the sum of numbers')
        elif self.user_input == '':
            pass
        elif self.user_input != '/exit':
            values = list(self.user_input.split(' '))
            result = 0
            for number in values:
                if number == '+':
                    pass
                else:
                    result += int(number)
            print(result)
        else:
            print('Bye!')

    def simplify_operations(self):
        pass



if __name__ == '__main__':
    calc = Calculator()
    while calc.user_input != '/exit':
        calc.logic(input())
