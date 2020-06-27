def check_email(string):
    if string.find(' ') != -1:
        return False
    index = string.find('@')
    return index != -1 and string[index + 1] != '.' and string[index:].find('.') != -1

# if __name__ == '__main__':
#     tests = ['a a@.com', 'aa@ .com', 'aa@. com', 'aa@com', 'aa.com', 'aa@a.com', '@.']
#     for test in tests:
#         print('Test case: ', test, ' Result: ', check_email(test))