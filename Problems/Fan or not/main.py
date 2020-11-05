def add_viewer(name, fan_list=None):
    if fan_list is None:
        fan_list = []
    fan_list.append(name)
    return fan_list


# if __name__ == '__main__':
#     test1 = add_viewer('Harry', fan_list=['Mark', 'Joshua'])
#     test2 = add_viewer('Molly')
#     print('Test case 1: ', test1 == ['Mark', 'Joshua', 'Harry'])
#     print('List 1: ', test1)
#     print('Test case 2: ', test1 == ['Molly'])
#     print('List 2: ', test2)
=