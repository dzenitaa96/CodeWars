# In this little assignment you are given a string of space separated numbers, and have to return the highest and
# lowest number.

def high_and_low(numbers):
    max_num = max(map(int, numbers.split(' ')))
    min_num = min(map(int, numbers.split(' ')))
    return '{} {}'.format(max_num, min_num)