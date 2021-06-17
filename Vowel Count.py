# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# My solution:
def get_count(input_str):
    vowels = "aeiou"
    num_vowels = 0
    for c in input_str:
        if c in vowels:
            num_vowels += 1
    return num_vowels

# Other:
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# Or:
def getCount(s):
    return sum(c in 'aeiou' for c in s)