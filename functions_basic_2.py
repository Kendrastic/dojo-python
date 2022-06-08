# Countdown, create a list (exex inpult is 5 and output list [5,4,3,2,1,0]

def countdown(countdown_from):
    # return [countdown_list for countdown_list in range(countdown_from, -1, -1)]
    #The solution I found above and changed for my code worked, but as I got to the lower excercises I needed to simplify this.
    countdown = []
    for i in range(countdown_from, -1, -1):
        countdown.append(i)
    return countdown

print(countdown(5))

#Print and Return- Function that takes in a list with two values. Print v1 and return v2.

def print_return(list):
    print(list[0])
    return list[1]

example_list = [1,2]
print(print_return(example_list))

#First Plus Length - Function takes in a list and returns first (first value + length)

def first_plus_length(another_list):
    total = another_list[0] + len(another_list)
    return total

list_3_ex = [1,2,3,4,5]
print(first_plus_length(list_3_ex))

# Values Greater than Second - not there yet

def vals_greater_than_second(some_list):
    if len(some_list) < 2:
        return False
    new_list = []
    for j in range(0,len(some_list)):
        if some_list[j] > some_list[1]: 
            new_list.append(some_list[j])
    print(len(new_list))
    return new_list

print(vals_greater_than_second([5,4,3,2,1]))
print(vals_greater_than_second([3]))


# This Length, That Value

def this_length_that_value(size, value):
    brand_new_list = []
    for k in range(0,size):
        brand_new_list.append(value)
    return brand_new_list

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))