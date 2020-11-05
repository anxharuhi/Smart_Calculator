# the object_list has already been defined
# write your code here
from collections import Counter
from collections.abc import Hashable

# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]getattr()

hash_list = []
count_dict = {}
doppelganger = 0
for item in object_list:
    if isinstance(item, Hashable):
        hash_list.append(hash(item))
count_list = dict(Counter(hash_list))
for number in count_list.values():
    if number != 1:
        doppelganger += number
print(doppelganger)
