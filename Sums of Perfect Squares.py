import math

# Taking the input from user
number = int(input("Enter the Number "))
sum_of_squares = 0
root = math.sqrt(number)
print(int(math.sqrt(number)))

def perfect_squares(number):
    lowest = 1
    highest = int(math.sqrt(number))
    return (n**2 for n in range(lowest, highest + 1))

print(perfect_squares(number))
#if int(root + 0.5) ** 2 == number:
#    sum_of_squares = 1
#else:
#    pass
#sum_of_all = 0
#new_num = 0
#while sum_of_all < number:
#    new_num = number - int(math.sqrt(number)) ** 2
#   print(new_num)
 #  sum_of_squares = sum_of_squares + 1

    #sum_of_all = sum_of_all + new_num
    #print(sum_of_all)
    #sum_of_squares = sum_of_squares + 1
    #print(new_num, sum_of_all)






#print(sum_of_squares)