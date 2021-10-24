# this loop:
numbers = []
for i in range(1, 1001):
    numbers.append(i)
# becomes:
numbers = [i for i in range(1, 1001)]

# examples:
evens = [i for i in numbers if i % 2 == 0]
sixes = [i for i in numbers if "6" in str(i)]

## format of a list comprehension:
#
# for _variable_ in _collection_:
#     if _condition_:
#         _output_
## becomes:
# [output for _variable_ in _collection_ if _condition_]

