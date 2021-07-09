def odd_or_even(arr):
    sumArr = 0
    for i in arr:
        sumArr = sumArr + i
    if sumArr % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

arr = [0]
odd_or_even(arr)
