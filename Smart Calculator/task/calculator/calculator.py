# write your code here
class Calculator:
    commands = {'/help': 'The program calculates the sum of numbers',
                '/exit': 'Bye!'}

    def __init__(self, user_input=None):
        self.user_input = user_input

    def messages(self):
        pass

    def logic(self, input):
        self.user_input = input
        if self.user_input == '':
            pass
        elif self.user_input in self.commands.keys():
            print(self.commands[self.user_input])
        elif self.user_input != '/exit':
            values = list(self.user_input.split(' '))
            result = 0
            for number in values:
                if number == '+':
                    pass
                else:
                    try:
                        result += int(number)
                    except:
                        result = None
            if result is not None:
                print(result)

    def simplify_operations(self):
        pass


if __name__ == '__main__':
    calc = Calculator()
    while calc.user_input != '/exit':
        calc.logic(input())
