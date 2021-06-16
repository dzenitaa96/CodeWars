# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
# integers. No floats or non-positive integers will be passed. For example, when an array is passed like [19, 5, 42,
# 2, 77], the output should be 7.

# CodeWars accepted solution:
def sum_two_smallest_numbers(numbers):
    newNumbers = sorted(numbers)
    sumoftwo = 0
    for n in range(0, 2):
        sumoftwo = sumoftwo + int(newNumbers[n])
    return sumoftwo

# Another solution:
def sum_two_smallest_numbers(numbers):
    numbers = input('Enter some numbers: ').split(', ')
    numbers = [int(v) for v in numbers]
    # Create a sorted copy of existing list
    newNumbers = sorted(numbers)
    # print("New List", newNumbers, sep='\n')
    sumoftwo = 0
    for n in range(0, 2):
        sumoftwo = sumoftwo + int(newNumbers[n])
    print(sumoftwo)
sum_two_smallest_numbers('')

# Shortest way:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])