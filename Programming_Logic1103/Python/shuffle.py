# shuffle.py
# random str char mixing
# demonstrate basic refactoring
import random

def shuffle_alpha(case):
    if case == 'upper':
        alpha_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        alpha_str = 'abdcefghijklmnopqrstuvwxyz'
    rand_str = shuffle_string(alpha_str)
    return rand_str

def shuffle_string(par_str):
    str_list = []
    # taking str and turning into list
    for i in range (0, len(par_str), 1):
        str_list.append(par_str[i])
        # print ('inside loop, string list', str_list)
    # print('string list is', str_list)

    #shuffling list
    random.shuffle(str_list)
    # print ('random shuffle is', str_list)

    #turining shuffled list back into str
    new_str = ''
    for i in range(0, len(str_list), 1):
        new_str = new_str + str_list[i]
        # print('  in loop new str', new_str)

    # print ('new str is', new_str)
    return new_str



# my_str = input('what is your string? ')
my_str = 'Hello world!'
print ('my string is', my_str)
random_str = shuffle_string(my_str)
print ('random str is', random_str)
random_str = shuffle_alpha('lower')
print ('random alphabet is', random_str)