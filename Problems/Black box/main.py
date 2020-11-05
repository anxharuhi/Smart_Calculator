# use the function blackbox(lst) that is already defined

random_list = [1, 2, 3]
blackbox = blackbox(random_list)
if random_list is blackbox:
    print('modifies')
else:
    print('new')
