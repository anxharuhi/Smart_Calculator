# write your code here
class Calculator:
    commands = {'/help': 'The program calculates the sum of numbers',
                '/exit': 'Bye!'}

    def __init__(self, user_input=None):
        self.user_input = user_input

    def messages(self):
        pass

    def __operation_list(self):
        return self.user_input.split(' ')
        # We can add later parenthesis by checking for them and converting
        # whatever it is between them to a list occupying that position

    def __calculate_sign(self, sign_string: str):
        sign_list = list(sign_string)
        sign = sign_list.pop()
        for signs in sign_list:
            if signs == '-' and sign == '+':
                sign = '-'
            elif signs == '-' and sign == '-':
                sign = '+'
        return sign

    def __solve(self, op_list: list):
        while len(op_list) > 1:
            if len(op_list) < 1:
                raise Warning('List of operations is smaller than 1 or Null') # Just a sanity check
            else:
                    sub_op = []
                    sub_op.append(int(op_list.pop())) # First and last from the operation are numbers, so typecast them
                    sub_op.append(op_list.pop()) # Get the first number and operand
                    while not sub_op[-1].isnumeric():
                        sub_op.append(op_list.pop()) # Then keep popping until you find anouther number
                    sub_op[-1] = int(sub_op[-1]) # Same deal here
                    if len(sub_op[1]) > 1:
                        sub_op = [sub_op[0], self.__calculate_sign(sub_op[1]), sub_op[-1]] # Calculate the sign of the operation
                    if sub_op[1] == '+':
                        op_list.append(sub_op[-1] + sub_op[0])
                    elif sub_op[1] == '-':
                        op_list.append(sub_op[0] - sub_op[-1])
        return op_list[0]

    def logic(self):
        if self.user_input == '':
            pass
        elif self.user_input in self.commands.keys():
            print(self.commands[self.user_input])
        elif self.user_input != '/exit':
            operation_list = list(self.__operation_list())
            operation_list.reverse()  # Invert the list so we start at the beginning
            result = self.__solve(operation_list)
            if result is not None:
                print(result)


if __name__ == '__main__':
    calc = Calculator()
    while calc.user_input != '/exit':
        calc.user_input = input()
        # calc.user_input = '3 + 2 + 1'
        calc.logic()
