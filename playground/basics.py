# lets get the basics right
name_string = f"Naveen is great indeed ravi"
print(name_string)

# string operations
print(f"the length of the string is {len(name_string)}")
split_strings = name_string.split(" ")
print(f"the split strings are {split_strings}")

for str in split_strings:
    print(str)
    print(f"isn't this amzing - the upper case is {str.upper()}")
# get the dictionries and process them
sample_dict = {"a": "naveen", "b": "balawat"}
num_dict = {"prod1": 200, "b": 400}
for (k, v) in sample_dict.items():
    print(f"the key is {k} - the value is {v}")

for rec in sample_dict.items():
    print(f"the tuple is {rec}")
    print(f"the key is {rec[0]} - the value is {rec[1]}")


def add_some_number(val):
    return val + 32


def filter_number(val):
    return val > 300 


new_values = list(map(add_some_number, num_dict.values()))
filtered_values = list(filter(filter_number, num_dict.values()))
print(f"The new values are {new_values}")
print(f" the filtered values are{filtered_values}")
# Lets do some lists and sets
num_lists = [1, 20, 40, 50, 400]
print(num_lists[:3])
print(num_lists[1:-1])
print(num_lists[-1])
for n in num_lists:
    print(n)

# Lets do some set operations
lfunc = lambda x, y: x + y

# Lets learn the kwargs and args thing
