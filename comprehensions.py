# this loop:
numbers = []
for i in range(1, 1001):
    numbers.append(i)
# becomes:
numbers = [i for i in range(1, 1001)]

# examples:
evens = [i for i in numbers if i % 2 == 0]
sixes = [i for i in numbers if "6" in str(i)]

text = "The slick slimy squid slithered through the slick seaweed."
words = len([char for char in text if char = " "])\

# double numbers less than 100, other wise subtract 100 from them
weird = [i * 2
        if i < 100
        else i - 100
        for i in numbers]