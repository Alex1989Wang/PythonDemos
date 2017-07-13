
# accessing an unkonwn key in a dictionary 
# raises an exception 
empty_dict = dict()
#print(empty_dict("Jiang"))

# setdefault 
jiang = empty_dict.setdefault("Jiang", "jiang")
print(jiang)

# defaultdict()
from collections import defaultdict
empty_dict = defaultdict(str)
print(empty_dict)
print(empty_dict["Jiang"])


from collections import defaultdict
food_counter = defaultdict(int)
for food in ["eggs", "eggs", "rice", "beef"]:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

